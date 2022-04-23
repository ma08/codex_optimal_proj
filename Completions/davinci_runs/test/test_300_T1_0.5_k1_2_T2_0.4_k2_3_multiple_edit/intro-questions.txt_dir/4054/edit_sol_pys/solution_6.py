#!/usr/bin/env python
# encoding: utf-8

from __future__ import division

import math
import numpy as np

import rospy
import tf
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import TwistStamped
from geometry_msgs.msg import Vector3Stamped
from mavros_msgs.msg import AttitudeTarget
from mavros_msgs.msg import Thrust
from mavros_msgs.srv import CommandBool
from mavros_msgs.srv import SetMode
from sensor_msgs.msg import Imu
from std_msgs.msg import Float32
from std_msgs.msg import Header
from tf.transformations import euler_from_quaternion


class PositionController(object):

    def __init__(self):
        self.rate = rospy.Rate(30)
        self.imu_sub = rospy.Subscriber("/mavros/imu/data", Imu, self.imu_callback)
        self.local_pos_sub = rospy.Subscriber("/mavros/local_position/pose", PoseStamped, self.local_pos_callback)
        self.local_vel_sub = rospy.Subscriber("/mavros/local_position/velocity_local", TwistStamped, self.local_vel_callback)
        self.att_target_pub = rospy.Publisher("/mavros/setpoint_raw/attitude", AttitudeTarget, queue_size=10)
        self.thrust_pub = rospy.Publisher("/mavros/setpoint_attitude/thrust", Thrust, queue_size=10)
        self.arming_client = rospy.ServiceProxy("/mavros/cmd/arming", CommandBool)
        self.set_mode_client = rospy.ServiceProxy("/mavros/set_mode", SetMode)

        self.local_pos = PoseStamped()
        self.local_vel = TwistStamped()
        self.attitude = Imu()
        self.thrust = 0.0

        self.Kp_xy = np.array([1.5, 1.5, 0.0])
        self.Kp_z = np.array([0.3, 0.3, 0.0])
        self.Kd_xy = np.array([1.0, 1.0, 0.0])
        self.Kd_z = np.array([0.2, 0.2, 0.0])
        self.Ki_xy = np.array([0.0, 0.0, 0.0])
        self.Ki_z = np.array([0.0, 0.0, 0.0])

        self.desired_pos = np.array([0.0, 0.0, 1.0])
        self.desired_vel = np.array([0.0, 0.0, 0.0])
        self.desired_acc = np.array([0.0, 0.0, 0.0])
        self.desired_yaw = 0.0

        self.error_pos = np.array([0.0, 0.0, 0.0])
        self.error_vel = np.array([0.0, 0.0, 0.0])
        self.error_acc = np.array([0.0, 0.0, 0.0])
        self.error_pos_prev = np.array([0.0, 0.0, 0.0])
        self.error_vel_prev = np.array([0.0, 0.0, 0.0])
        self.error_pos_sum = np.array([0.0, 0.0, 0.0])
        self.error_vel_sum = np.array([0.0, 0.0, 0.0])

        self.desired_attitude = AttitudeTarget()
        self.desired_attitude.thrust = 0.0
        self.desired_attitude.body_rate = Vector3Stamped()
        self.desired_attitude.orientation = Vector3Stamped()
        self.desired_attitude.type_mask = 7

        self.desired_thrust = Thrust()

        self.desired_yaw_rate = 0.0
        self.desired_pitch = 0.0
        self.desired_roll = 0.0
        self.desired_pitch_rate = 0.0
        self.desired_roll_rate = 0.0

    def imu_callback(self, data):
        self.attitude = data

    def local_pos_callback(self, data):
        self.local_pos = data

    def local_vel_callback(self, data):
        self.local_vel = data

    def run(self):
        while not rospy.is_shutdown():
            # Get current position, velocity and attitude
            curr_pos = np.array([self.local_pos.pose.position.x, self.local_pos.pose.position.y, self.local_pos.pose.position.z])
            curr_vel = np.array([self.local_vel.twist.linear.x, self.local_vel.twist.linear.y, self.local_vel.twist.linear.z])
            curr_attitude = euler_from_quaternion([self.attitude.orientation.x, self.attitude.orientation.y, self.attitude.orientation.z, self.attitude.orientation.w])

            # Get current yaw angle
            yaw = curr_attitude[2]

            # Calculate errors
            self.error_pos = self.desired_pos - curr_pos
            self.error_vel = self.desired_vel - curr_vel
            self.error_acc = self.desired_acc - (self.error_vel - self.error_vel_prev) * 30
            self.error_pos_sum += self.error_pos
            self.error_vel_sum += self.error_vel

            # Calculate control signal
            u_pos = self.Kp_xy * self.error_pos[0:2] + self.Kd_xy * self.error_vel[0:2] + self.Ki_xy * self.error_pos_sum[0:2]
            u_vel = self.Kp_z * self.error_pos[2] + self.Kd_z * self.error_vel[2] + self.Ki_z * self.error_pos_sum[2]

            # Calculate desired roll and pitch angles
            self.desired_roll = u_pos[1] * math.cos(yaw) + u_pos[0] * math.sin(yaw)
            self.desired_pitch = -u_pos[0] * math.cos(yaw) + u_pos[1] * math.sin(yaw)

            # Calculate desired roll rate and pitch rate
            self.desired_roll_rate = u_vel[1] * math.cos(yaw) + u_vel[0] * math.sin(yaw)
            self.desired_pitch_rate = -u_vel[0] * math.cos(yaw) + u_vel[1] * math.sin(yaw)

            # Calculate desired yaw rate
            self.desired_yaw_rate = self.desired_yaw

            # Calculate desired thrust
            self.thrust = u_vel[2]

            # Update previous errors
            self.error_pos_prev = self.error_pos
            self.error_vel_prev = self.error_vel

            # Publish control signals
            self.desired_attitude.orientation.x = self.desired_roll
            self.desired_attitude.orientation.y

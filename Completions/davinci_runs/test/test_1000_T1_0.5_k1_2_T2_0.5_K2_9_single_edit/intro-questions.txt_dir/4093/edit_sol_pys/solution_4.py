
#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import time
import getopt
import socket
import ConfigParser
import struct
import binascii
 
opts, args = getopt.getopt(sys.argv[1:], 'hH:p:', ['help'])
commandargs = {'host':'','port':'80'}
helpinfo = '''
    -h: help info
    -H: host ip
    -p: port
'''
for op, value in opts:
    if op == '-h':
        print helpinfo
        sys.exit()
    elif op == '-H':
        commandargs['host'] = value
    elif op == '-p':
        commandargs['port'] = value
 
host = commandargs['host']
port = int(commandargs['port'])
 
if host == '':
    print helpinfo
    sys.exit()
 
def socket_port(ip,port):
    """
    输入IP和端口号，扫描判断端口是否占用
    """
    try:
        if port >= 65535:
            print u'端口扫描结束'
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
        if result == 0:
            lock = 1
        else:
            lock = 0
        s.close()
    except:
        print u'端口扫描异常'
    return lock
 
def find_service(port,dict):
    """
    输入端口，找出对应的服务名
    """
    port = str(port)
    service = dict.get(port)
    if service:
        return service
    else:
        return "unknown"
 
def get_ip_status(ip,dict):
    """
    输入IP，扫描IP的0-65534端口情况
    """
    try:
        print u'开始扫描 %s' % ip
        start_time = time.time()
        for i in range(0,65534):
            sys.stdout.write(' ' + '\b')
            sys.stdout.flush()
            status = socket_port(ip,int(i))
            if status == 1:
                service = find_service(i,dict)
                print u'端口：%s \t 服务名：%s' % (i,service)
        print u'扫描端口完成，总共用时 ：%.2f' %(time.time()-start_time)
        raw_input("Press Enter to Exit")
    except:
        print u'扫描ip出错'
 
if __name__ == '__main__':
    config_file = "service-port.conf"
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    dict = {}
    for section in config.sections():
        for key,value in config.items(section):
            dict[key] = value
    get_ip_status(host,dict)

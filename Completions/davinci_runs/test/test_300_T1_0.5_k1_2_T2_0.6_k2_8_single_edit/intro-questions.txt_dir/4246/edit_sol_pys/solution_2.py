
import collections
import csv
import itertools
import os
import sys
import multiprocessing

import numpy as np
import tensorflow as tf

from util.default_util import *
from util.embedding_util import *
from util.model_util import *


def main(argv):
    # load the arguments
    args = default_parser().parse_args(argv[1:])

    if args.mode == 'train':
        train(args)
    elif args.mode == 'test':
        test(args)
    elif args.mode == 'predict':
        predict(args)
    elif args.mode == 'evaluate':
        evaluate(args)
    else:
        raise ValueError('Invalid mode: %s' % args.mode)


def train(args):
    data = Dataset(args)

    with tf.Graph().as_default():
        with tf.Session() as sess:
            # build the graph
            initializer = tf.random_uniform_initializer(-args.init_scale, args.init_scale)
            with tf.variable_scope('model', reuse=None, initializer=initializer):
                model = Model(args, is_training=True)

            # initialize
            tf.global_variables_initializer().run()

            # train
            for i in range(args.num_epoch):
                print('Training in epoch %d' % (i + 1))
                data.shuffle()
                epoch_size = data.get_num_batches(args.batch_size)
                for step in range(epoch_size):
                    x, y = data.next_batch(args.batch_size)
                    feed_dict = {model.input_data: x, model.targets: y}
                    _, loss, summary = sess.run([model.train_op, model.cost, model.merged], feed_dict=feed_dict)

                    if step > 0 and step % args.print_every == 0:
                        print('Epoch %d, step %d, loss = %.6f' % (i + 1, step, loss))

                if args.tensorboard:
                    model.writer.add_summary(summary, i)

                # save the model
                if (i + 1) % args.save_every == 0 or (i + 1) == args.num_epoch:
                    checkpoint_path = os.path.join(args.model_dir, 'model.ckpt')
                    model.saver.save(sess, checkpoint_path, global_step=model.global_step)


def test(args):
    data = Dataset(args)

    with tf.Graph().as_default():
        with tf.Session() as sess:
            # build the graph
            initializer = tf.random_uniform_initializer(-args.init_scale, args.init_scale)
            with tf.variable_scope('model', reuse=None, initializer=initializer):
                model = Model(args, is_training=False)

            # initialize
            tf.global_variables_initializer().run()

            # load the model
            model_path = os.path.join(args.model_dir, 'model.ckpt')
            ckpt = tf.train.get_checkpoint_state(args.model_dir)
            if ckpt and ckpt.model_checkpoint_path:
                print('Loading the model from %s' % ckpt.model_checkpoint_path)
                model.saver.restore(sess, ckpt.model_checkpoint_path)
            else:
                raise ValueError('No checkpoint file found in %s' % args.model_dir)

            # test
            print('Testing...')
            num_batches = data.get_num_batches(args.batch_size)
            for step in range(num_batches):
                x, y = data.next_batch(args.batch_size)
                feed_dict = {model.input_data: x, model.targets: y}
                loss = sess.run([model.cost], feed_dict=feed_dict)
                print('Batch %d, loss = %.6f' % (step, loss))


def predict(args):
    data = Dataset(args)

    with tf.Graph().as_default():
        with tf.Session() as sess:
            # build the graph
            initializer = tf.random_uniform_initializer(-args.init_scale, args.init_scale)
            with tf.variable_scope('model', reuse=None, initializer=initializer):
                model = Model(args, is_training=False)

            # initialize
            tf.global_variables_initializer().run()

            # load the model
            model_path = os.path.join(args.model_dir, 'model.ckpt')
            ckpt = tf.train.get_checkpoint_state(args.model_dir)
            if ckpt and ckpt.model_checkpoint_path:
                print('Loading the model from %s' % ckpt.model_checkpoint_path)
                model.saver.restore(sess, ckpt.model_checkpoint_path)
            else:
                raise ValueError('No checkpoint file found in %s' % args.model_dir)

            # predict
            print('Predicting...')
            num_batches = data.get_num_batches(args.batch_size)
            for step in range(num_batches):
                x, y = data.next_batch(args.batch_size)
                feed_dict = {model.input_data: x, model.targets: y}
                predictions = sess.run([model.predictions], feed_dict=feed_dict)
                print(predictions)


def evaluate(args):
    data = Dataset(args)

    with tf.Graph().as_default():
        with tf.Session() as sess:
            # build the graph
            initializer = tf.random_uniform_initializer(-args.init_scale, args.init_scale)
            with tf.variable_scope('model', reuse=None, initializer=initializer):
                model = Model(args, is_training=False)

            # initialize
            tf.global_variables_initializer().run()

            # load the model
            model_path = os.path.join(args.model_dir, 'model.ckpt')
            ckpt = tf.train.get_checkpoint_state(args.model_dir)
            if ckpt and ckpt.model_checkpoint_path:
                print('Loading the model from %s' % ckpt.model_checkpoint_path)
                model.saver.restore(sess, ckpt.model_checkpoint_path)
            else:
                raise ValueError('No checkpoint file found in %s' % args.model_dir)

            # evaluate
            print('Evaluating...')
            num_batches = data.get_num_batches(args.batch_size)
            for step in range(num_batches):
                x, y = data.next_batch(args.batch_size)
                feed_dict = {model.input_data:

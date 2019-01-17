"""
This file is an old learning file.
This is just for testing some things.
Please use the new keras learning one.
"""

import matplotlib.pyplot as plt
import numpy as np
import random as rand
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


def train_size(num):
    print('Total Training Images in Dataset = ', mnist.train.images.shape)
    print('-----------------------------------------------')
    x_train = mnist.train.images[:num, :]
    print('x_train Examples Loaded = ', x_train.shape)
    y_train = mnist.train.labels[:num, :]
    print('y_train Examples Loaded = ', y_train.shape)
    print('')
    return x_train, y_train


def test_size(num):
    print('Total Test Examples in Dataset = ', mnist.test.images.shape)
    print('-----------------------------------------------')
    x_test = mnist.test.images[:num, :]
    print('x_test Examples Loaded = ', x_test.shape)
    y_test = mnist.test.labels[:num, :]
    print('y_test Examples Loaded = ', y_test.shape)
    return x_test, y_test


def display_digit(num):
    print(y_train[num])
    label = y_train[num].argmax(axis=0)
    image = x_train[num].reshape([28, 28])
    plt.title('Example %d Label: %d' % (num, label))
    plt.imshow(image, cmap=plt.get_cmap('gray_r'))
    plt.show()


def display_mult_flat(start, stop):
    images = x_train[start].reshape([1, 784])
    for i in range(start + 1, stop):
        images = np.concatenate((images, x_train[i].reshape([1, 784])))
    plt.imshow(images, cmap=plt.get_cmap('gray_r'))
    plt.show()


# display_digit(rand.randint(0, x_train.shape[0]))

x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])
w = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, w) + b)  # matmul = matrix multiplication

# define cost function. cost higher => level of inaccuracy
cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

x_train, y_train = train_size(5500)
x_test, y_test = test_size(10000)
learning_rate = 0.05
train_steps = 2000

session = tf.Session()
init = tf.initialize_all_variables()
session.run(init)

training = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

for i in range(train_steps + 1):
    session.run(training, feed_dict={x: x_train, y_: y_train})
    if i % 100 == 0:
        print('Training Step:', [i], ' Accuracy =', session.run(accuracy, feed_dict={x: x_test, y_: y_test}), 'Loss =', session.run(cross_entropy, {x: x_train, y_: y_train}))

# for i in range(10):
    # plt.subplot(2, 5, i + 1)
    # weight = session.run(w)[:, i]
    # plt.title(i)
    # plt.imshow(weight.reshape([28, 28]), cmap=plt.get_cmap('seismic'))
    # frame1 = plt.gca()
    # frame1.axes.get_xaxis().set_visible(False)
    # frame1.axes.get_yaxis().set_visible(False)

# plt.show()

# x_train, y_train = train_size(1)
# display_digit(0)

# answer = session.run(y, feed_dict={x: x_train})
# print(answer.argmax())


def display_compare(num):
    # load one training example
    x_train = mnist.train.images[num, :].reshape(1, 784)
    y_train = mnist.train.labels[num, :]

    label = y_train.argmax()

    prediction = session.run(y, feed_dict={x: x_train}).argmax()

    plt.title('Prediction: %d Label: %d' % (prediction, label))
    plt.imshow(x_train.reshape([28, 28]), cmap=plt.get_cmap('gray_r'))
    plt.show()


for i in range(1000):
    display_compare(rand.randint(0, 55000))
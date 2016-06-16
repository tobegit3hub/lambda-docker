#!/usr/bin/env python

import tensorflow as tf 

print("Run TensorFlow to multiple numbers")

a = tf.placeholder("float")
b = tf.placeholder("float")
c = tf.mul(a, b)

with tf.Session() as sess:
  print("Multiple 1 with 2 to get:")
  print(sess.run(c, feed_dict={a: 1, b: 2})) # Assert 2

  print("Multiple 3 with 4 to get:")
  print(sess.run(c, feed_dict={a: 3, b: 4})) # Assert 12

print("End of TensorFlow")
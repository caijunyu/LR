#!/usr/bin/env python
# coding=utf-8

import math, random
import matplotlib.pyplot as plt
import min_square

__author__ = 'yhustc'

instance_list = []

instance_x_1 = []
instance_y_1 = []
r = 15
for x in range(-r, r+1):
    instance_x_1.append(x)
    instance_y_1.append(math.sqrt(pow(r, 2) - pow(x, 2)))
    instance_list.append((x, instance_y_1[-1]))
instance_x_2 = []
instance_y_2 = []
r = 10
for x in range(-r, r+1):
    instance_x_2.append(x)
    instance_y_2.append(math.sqrt(pow(r, 2) - pow(x, 2)))
    instance_list.append((x, instance_y_2[-1]))

plt.plot(instance_x_1, instance_y_1, 'o', color='r')
plt.plot(instance_x_2, instance_y_2, 'o', color='b')
plt.ylim(ymin=0, ymax=15)
#plt.show()

# 开始模型训练, y=theta0+theta1*x
random.shuffle(instance_list)
iteration = 100
model = min_square.fit(instance_list, 0.01, iteration)

x_list = []
y_1_list = []
y_2_list = []
y_3_list = []
for x in range(-15, 16):
    x_list.append(x)
    y_1_list.append(model[0][0] + model[0][1] * x)
    y_2_list.append(model[1][0] + model[1][1] * x)
    y_3_list.append(model[2][0] + model[2][1] * x)
plt.plot(x_list, y_1_list, '-.', color='y', linewidth=3.0, label=u'iter-0')
plt.plot(x_list, y_2_list, '-.', color='g', linewidth=3.0, label=u'iter-m')
plt.plot(x_list, y_3_list, '--', color='b', linewidth=3.0, label=u'iter-%d' % iteration)

plt.legend()
plt.show()
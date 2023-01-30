#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

source ~/code/2023/robotics/create3_examples_ws/install/local_setup.sh

ros2 launch create3_teleop teleop_joystick_launch.py joy_dev:=/dev/input/js1


https://github.com/iRobotEducation/create3_examples/tree/galactic/create3_teleop
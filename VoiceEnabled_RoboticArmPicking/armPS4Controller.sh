#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1
source /home/yuxiang/interbotix_ws/devel/setup.bash

roslaunch interbotix_xsarm_joy xsarm_joy.launch robot_model:=px100
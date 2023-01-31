#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1
source /home/yuxiang/interbotix_ws/devel/setup.bash

roslaunch interbotix_xsarm_joy xsarm_joy.launch robot_model:=px100
PID1=$PID1
echo $PID1

echo "recording for 15 seconds"
sleep 20
# kill ROSlaunch at the end. Same as control-C

kill $PID1
#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1
source /home/yuxiang/interbotix_ws/devel/setup.bash


# rosBag directory: interbotix_ros_manipulators/interbotix_ros_xsarms/examples/interbotix_xsarm_puppet/bag/
roslaunch interbotix_xsarm_puppet xsarm_puppet_single.launch robot_model:=px100 playback:=true &
PID1=$!
echo $PID1


echo "replaying for 10 seconds"
sleep 20
# kill ROSlaunch at the end. Same as control-C
echo "shutting down"

kill $PID1

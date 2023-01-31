#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1


# required debugging into the python code, better understanding, less backgrounds, rewatch video how to tune parameters, 
#  too easy to break, can't exit cleanly
source /home/yuxiang/interbotix_ws/devel/setup.bash

roslaunch interbotix_xsarm_perception xsarm_perception.launch robot_model:=px100 use_pointcloud_tuner_gui:=true use_armtag_tuner_gui:=true &

sleep 6



# Python program does not return any PID
echo "start execute pick and place"
python3 /home/yuxiang/interbotix_ws/src/interbotix_ros_manipulators/interbotix_ros_xsarms/interbotix_xsarm_perception/scripts/pick_place.py 
echo "finish executing pick and place"

PID2=$!
echo "PID2"
echo $PID2

echo "wait for PID2 $PID2"
wait $PID2

echo "kill PID2 $PID2"
kill $PID2
#!/bin/bash

name="AutoPlow"

echo "Hi Autoplow"
sleep 1

source /home/yuxiang/code/2023/env/bin/activate

python3 /home/yuxiang/code/2022/code/depthAI/depthai-experiments/gen2-yolo/device-decoding/customizedYolo7Spatial.py /home/yuxiang/code/2022/code/depthAI/depthai-experiments/gen2-yolo/device-decoding/autoplowoakdetectionweights_openvino_2021.4_6shave.blob

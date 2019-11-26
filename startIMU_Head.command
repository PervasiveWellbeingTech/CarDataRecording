#!/bin/bash

echo "IMU startup:"
printf "Participant ID: "
read participant
echo "$participant"

cd ~/Desktop/ParticipantData

mkdir "$participant"/IMU_Head

# start the IMU logger
python ~/Desktop/DataRecordingCode/imu_logger_head.py "$participant"/IMU_Head

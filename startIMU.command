#!/bin/bash

echo "IMU startup:"
printf "Participant ID: "
read participant
echo "$participant"

cd ~/Desktop/ParticipantData

mkdir "$participant"/IMU

# start the IMU logger
python ~/Desktop/DataRecordingCode/imu_logger.py "$participant"/IMU

#!/bin/bash

echo "IMU startup:"
printf "Participant ID: "
read participant
echo "$participant"

cd ~/Desktop/ParticipantData

mkdir "$participant"/BrakePedal

# start the IMU logger
python ~/Desktop/DataRecordingCode/BrakePedal.py "$participant"/BrakePedal

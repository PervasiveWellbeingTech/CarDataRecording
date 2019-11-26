import timeit
import os
import random
import sched, time
import sys





def promptDriverStart():
    # write the ask time to the file
    f.write(str(time.time()) + '\n')
    os.system('afplay ~/Desktop/DataRecordingCode/sounds/startBreathingExercise.m4a')

#def promptDriverStop():
    # write the ask time to the file
  #  f.write(str(time.time()) + '\n')
   # os.system('afplay ~/Desktop/DataRecordingCode/sounds/PleaseStopTheSlowBreathingExerciseNow.m4a')

def promptFinish():
    # write the ask time to the file
    f.write(str(time.time()) + '\n')
    os.system('afplay ~/Desktop/DataRecordingCode/sounds/stopBreathing.m4a')

	#os.system('afplay ~/Desktop/DataRecordingCode/sounds/howstressed.m4a')


# set up a file to log the question times and the answers [3]
f = open('PromptTimes_' + str(int(time.time())) + '.csv', 'w')
f.write('time\n')
print(os.getcwd())

# set up a scheduler to pick random times to say is now a good time [1]
s = sched.scheduler(time.time, time.sleep)

# do a test question
ask_time = 118
s.enter(ask_time, 1, promptDriverStart, ())
s.run()

#ask_time = 15
#s.enter(ask_time, 1, promptDriverStop, ())
#s.run()

ask_time = 116
s.enter(ask_time, 1, promptFinish, ())
s.run()
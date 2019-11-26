import timeit
import os
import random
import sched, time
import sys

def queryDriver():
    # write the ask time to the file
    f.write(str(time.time()) + '\n')
    os.system('afplay ~/Desktop/DataRecordingCode/sounds/breathingtime.m4a')


# set up a file to log the question times and the answers [3]
f = open('queryTimes_' + str(int(time.time())) + '.csv', 'w')
f.write('time\n')
print(os.getcwd())

# set up a scheduler to pick random times to say is now a good time [1]
s = sched.scheduler(time.time, time.sleep)

# do a test question
ask_time = 2
s.enter(ask_time, 1, queryDriver, ())
s.run()

while True:
    print(time.time())
    ask_time = random.randint(30,2*60) # wait time in seconds
    print(ask_time)
    s.enter(ask_time, 1, queryDriver, ())
    s.run()

# Resources
# [1] Event scheduling - https://docs.python.org/2/library/sched.html
# [2] Speech Recognition - https://pypi.python.org/pypi/SpeechRecognition/
# [3] Writing to files - https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# [4] Record Audio - http://people.csail.mit.edu/hubert/pyaudio/

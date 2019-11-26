import timeit
import os
import random
import sched, time
import sys





def promptMetal():
    # write the ask time to the file
    f.write(str(time.time()) + '\n')
    os.system('afplay ~/Desktop/DataRecordingCode/sounds/Jazz.m4a')




# set up a file to log the question times and the answers [3]
f = open('PromptTimes_' + str(int(time.time())) + '.csv', 'w')
f.write('time\n')
print(os.getcwd())

# set up a scheduler to pick random times to say is now a good time [1]
s = sched.scheduler(time.time, time.sleep)

# do a test question
ask_time = 10
s.enter(ask_time, 1, promptMetal, ())
s.run()

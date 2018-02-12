import subprocess
from sys import executable
from subprocess import Popen
import time
while True:
    p = Popen([executable, 'file_name.py']).wait()
    if p != 0:
        print "Restarting................1"
        time.sleep(1.0)
        print "Restarting................2"
        time.sleep(1.0)
        print "Restarting................3"
        time.sleep(1.0)
        continue
    else:
        print "Restarting fron error"
        time.sleep(5.0)
        continue

import os
import subprocess
from subprocess import Popen, PIPE, STDOUT, DEVNULL # py3k

def launch():
	print("launching influx")


	process = Popen(['sh', 'launch.sh', '&'], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)
	stdout, stderr = process.communicate()

	process = Popen(['sleep', '2'], stdin=PIPE, stdout=DEVNULL, stderr=STDOUT)
	stdout, stderr = process.communicate()




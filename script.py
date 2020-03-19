# testing script
import platform, os, subprocess
print('TEST SCRIPT RUN')

if platform.system()=="Windows":
	print('WINDOWS DETECTED')
	os.environ["GLPATH"] = "C:\\Program Files\\GridLAB-D\\bin;C:\\Program Files\\GridLAB-D\\etc;C:\\Program Files\\GridLAB-D\\lib;C:\\Program Files\\GridLAB-D\\samples;C:\\Program Files\\GridLAB-D\\rt;C:\\Program Files\\GridLAB-D\tmy"
	p = subprocess.Popen(['gridlabd', 'smsSingle.glm'])
	p.wait()
	print(p.returncode)
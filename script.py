# testing script
import platform, os, subprocess
print('TEST SCRIPT RUN')

def safe_call(cmdString):
	try:
		output = subprocess.check_output(
			cmdString, stderr=subprocess.STDOUT, shell=True,
			universal_newlines=True)
	except subprocess.CalledProcessError as exc:
		print(str(cmdString) + " Status : FAIL", exc.returncode, exc.output)
	else:
		print(str(cmdString) + " Output: \n{}\n".format(output))

if platform.system()=="Windows":
	print('WINDOWS DETECTED')
	# safe_call('cmd.exe //c RefreshEnv.cmd') #hangs travis
	print('PATH', os.getenv('PATH'))
	print('GLPATH', os.getenv('GLPATH'))
	print(os.listdir('C:\\Program Files\\GridLAB-D\\bin'))
	print(os.listdir('C:\\Program Files\\GridLAB-D\\lib'))
	safe_call(['gridlabd', '-h'])
	safe_call(['gridlabd', 'smsSingle.glm'])
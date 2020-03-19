# testing script
import platform, os, subprocess
print('TEST SCRIPT RUN')

if platform.system()=="Windows":
	print('WINDOWS DETECTED')
	print('PATH', os.getenv('PATH'))
	print('PATH', os.getenv('GLPATH'))
	print('RAW GLD RUN', os.system('gridlabd -h'))
	p = subprocess.Popen(['gridlabd', 'smsSingle.glm'])
	p.wait()
	print(p.returncode)
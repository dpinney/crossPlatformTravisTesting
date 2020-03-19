# testing script
import platform, os, subprocess
print('TEST SCRIPT RUN')

if platform.system()=="Windows":
	print('WINDOWS DETECTED')
	print('PATH', os.getenv('PATH'))
	print('GLPATH', os.getenv('GLPATH'))
	saneOut = subprocess.check_output(['gridlabd', '-h'])
	print('Just open gld:', saneOut)
	realOut = subprocess.check_output(['gridlabd', 'smsSingle.glm'])
	print('Running GLM:', realOut)
# testing script
import platform, os
print('TEST SCRIPT RUN')

if platform.system()=="Windows":
	print('WINDOWS DETECTED')
	print(os.system("gridlabd smsSingle.glm"))

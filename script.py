# testing script
import platform, os
print('TEST SCRIPT RUN')

if platform.system()=="Windows":
	os.system("gridlabd smsSingle.glm")
import platform, os
#  install script
print('INSTALL RUNNING')

# macos brew testing
if platform.system()=="Darwin": # MacOS
	os.system("brew install wget ffmpeg git graphviz octave mdbtools")
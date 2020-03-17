import platform, os
#  install script
print('INSTALL RUNNING')

# macos brew testing
if platform.system()=="Darwin": # MacOS
	# os.system("brew install wget ffmpeg git graphviz octave mdbtools")
	# os.system("brew install wget ffmpeg git graphviz octave mdbtools; brew link --overwrite python3")
	os.system("HOMEBREW_NO_AUTO_UPDATE=1 brew install wget ffmpeg git graphviz octave mdbtools")

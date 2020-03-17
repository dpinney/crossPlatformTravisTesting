import platform, os
#  install script
print('INSTALL RUNNING')

# macos brew testing
if platform.system()=="Darwin": # MacOS
	# os.system("brew install wget ffmpeg git graphviz octave mdbtools") # fails, kills python
	# os.system("brew install wget ffmpeg git graphviz octave mdbtools; brew link --overwrite python3") # works, extra 5 minutes
	os.system("HOMEBREW_NO_AUTO_UPDATE=1 brew install wget ffmpeg git graphviz octave mdbtools") # works, fast
	# SPLAT TEST
	os.system("wget https://www.qsl.net/kd2bd/splat-1.4.2-osx.tgz")
	os.system("sudo tar -xvzf splat-1.4.2-osx.tgz")
	os.system('''sed -i '' 's/ans=""/ans="2"/g' splat-1.4.2/configure''')
	os.system("spawn sudo bash splat-1.4.2/configure")
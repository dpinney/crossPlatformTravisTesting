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
	os.system('''
		expect <<'END'
		spawn sudo bash splat-1.4.2/configure
		expect "Your choice: "
		send "2"
		expect "Your choice: "
		send "1"
		expect eof
		END
		''')
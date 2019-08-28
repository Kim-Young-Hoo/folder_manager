import os
import shutil
import numpy as np

os.chdir("D:/torrent_downloaded/")


while True:
	
	dir_bool = [os.path.isdir(i) for i in os.listdir()]
	dir_list = np.array(os.listdir())[dir_bool]


	if len(os.listdir(os.getcwd())) == 0:
		break


	for upper_folder in os.listdir(os.getcwd()):
		for lower_folder in os.listdir(os.getcwd() + "\\" + upper_folder):
			if os.path.isdir(os.getcwd() + "\\" + upper_folder + "\\" + lower_folder):
				shutil.move(os.getcwd() + "\\" + upper_folder + "\\" + lower_folder, lower_folder)

	for file in os.listdir(os.getcwd()):
		if file.endswith(("mp4", "mkv", "avi")):
			shutil.move(os.getcwd() + "\\" + file, '../videos')    

	for direc in dir_list:
		for file in os.listdir(direc):
			if file.endswith(("mp4", "mkv", "avi")):
				shutil.move(os.getcwd() + "\\" + direc + "\\" + file, '../videos')    

			elif file.endswith(("srt", "smi")):
				shutil.move(os.getcwd() + "\\" + direc + "\\" + file, '../subtitles/' + direc + file)

			elif file.endswith("txt"):
				os.remove(os.getcwd() + "\\" + direc + "\\" + file)

			elif file.endswith("mp3"):
				pass
				
	for folder in os.listdir(os.getcwd()):
		if len(os.listdir(os.getcwd() + "\\" + folder)) == 0:
			os.rmdir(os.getcwd() + "\\" + folder)


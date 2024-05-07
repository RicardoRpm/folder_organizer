from shutil import copytree, ignore_patterns, move, copy
import os

sourceFolder = "C:\\Users\\juset\\Downloads"
destinationFolderMusic = "C:\\Users\\juset\\Music"
destinationFolderImage = "C:\\Users\\juset\\Pictures"
destinationFolderImage = "C:\\Users\\juset\\Pictures"

#copy(sourceFolder, destinationFolder);

listFiles = os.listdir(sourceFolder)

for file in listFiles:
    if  (file.endswith(".mp3")) or  (file.endswith(".wav")):

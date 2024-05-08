from shutil import move, copy
import os

SRC_FOLDER = "C:\\Users\\juset\\Downloads"
DST_FOLDER_MUSIC = "C:\\Users\\juset\\Music\\Downloaded"
DST_FOLDER_IMAGE = "C:\\Users\\juset\\Pictures\\Downloaded"
DST_FOLDER_DOCUMENTS = "C:\\Users\\juset\\Documents\\Downloaded"
DST_FOLDER_VIDEOS = "C:\\Users\\juset\\Videos\\Downloaded"


countMusic = 0
countImage = 0
countDocuments = 0
countVideos = 0


listFiles = os.listdir(SRC_FOLDER)
 
for file in listFiles:
    if  (file.endswith(".mp3")) or (file.endswith(".wav")):
        move(file, DST_FOLDER_MUSIC)
        countMusic = countMusic + 1
    elif (file.endswith(".mp4")): 
        os.mkdir(DST_FOLDER_VIDEOS)
        move(SRC_FOLDER + "\\" + file, DST_FOLDER_VIDEOS)
        print(file)
        countVideos = countVideos + 1
    else:
        continue

print("RESUMO DOS ARQUIVOS MOVIDOS")
print("VIDEOS: ", countVideos)
print("IMAGES: ", countImage)
print("DOCUMENTS: ", countDocuments)
print("MUSICAS: ", countMusic)

from shutil import copytree, ignore_patterns, move, copy
import os

SRC_FOLDER = "C:\\Users\\juset\\Downloads"
DST_FOLDER_MUSIC = "C:\\Users\\juset\\Music\\Downloaded"
DST_FOLDER_IMAGE = "C:\\Users\\juset\\Pictures\\Downloaded"
DST_FOLDER_DOCUMENTS = "C:\\Users\\juset\\Documents\\Downloaded"
DST_FOLDER_VIDEOS = "C:\\Users\\juset\\Documents\\Videos"

countMusic = 0
countImage = 0
countDocuments = 0
countVideos = 0

listFiles = os.listdir(SRC_FOLDER)

for file in listFiles:
    if  (file.endswith(".mp3")) or (file.endswith(".wav")):
        move(SRC_FOLDER, DST_FOLDER_MUSIC)
        countMusic = countMusic + 1
    elif (file.endswith(".mp4")): 
        move(SRC_FOLDER, DST_FOLDER_VIDEOS)
        countVideos = countVideos + 1
    elif (file.endswith(".png")) or  (file.endswith(".jpg")) or (file.endswith(".jpeg")): 
        move(SRC_FOLDER, DST_FOLDER_IMAGE)
        countImage = countImage + 1
    elif (file.endswith(".pdf")) or (file.endswith(".doc")) or (file.endswith(".txt")) or (file.endswith(".docx")) or (file.endswith(".rtf")) or (file.endswith(".pptx")): 
        move(SRC_FOLDER, DST_FOLDER_DOCUMENTS)
        countDocuments = countDocuments + 1
    else:
        continue

print("RESUMO DOS ARQUIVOS MOVIDOS")
print("VIDEOS: ", countVideos)
print("IMAGES: ", countImage)
print("DOCUMENTS: ", countDocuments)
print("MUSICAS: ", countMusic)

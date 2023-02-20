from pytube import YouTube
import os
#Funcion para descargar VIDEO
def downloadMP4(link, path):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    try:
        ytObject.download(output_path= path)
    except:
        print("Ha ocurrido un error")
    print("La descarga de video se hizo de forma exitosa")

#Funcion para descargar AUDIO
def downloadMP3(link, path):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_audio_only()
    try:
        download = ytObject.download(output_path= path)
    except:
        print("Ha ocurrido un error")
    base, ext = os.path.splitext(download)
    downloadRenamed = base + '.mp3'
    os.rename(download, downloadRenamed)
    print("La descarga de audio se hizo de forma exitosa")
    
#base, ext = os.path.splitext(download)
#downloadRenamed = base + '.mp3'
#os.rename(download, downloadRenamed)
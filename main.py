from pytube import YouTube

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
        ytObject.download(output_path= path)
    except:
        print("Ha ocurrido un error")
    print("La descarga de audio se hizo de forma exitosa")
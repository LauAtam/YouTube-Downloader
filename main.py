from pytube import YouTube

def download(link):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    try:
        ytObject.download()
    except:
        print("Ha ocurrido un error")
    print("La descarga se hizo de forma exitosa")
    
link = input("Ingrese la URL del video: ")
download(link)
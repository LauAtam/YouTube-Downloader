from pytube import YouTube

def download(link, path):
    ytObject = YouTube(link)
    ytObject = ytObject.streams.get_highest_resolution()
    try:
        ytObject.download(output_path= path)
    except:
        print("Ha ocurrido un error")
    print("La descarga se hizo de forma exitosa")

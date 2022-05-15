import youtube_dl

def run():
    video_url = input("Url : ")
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    filename = f"{video_info['title']}.mp3"
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Téléchargement complété : {}".format(filename))
    confirm()

def confirm():
    r = input("\nTélécharger une autre musique ? (Y/N) :")
    if r == "n" or r == "N":
        return
    elif r == "y" or r == "Y":
        run()
    else:
        return

if __name__=='__main__':
    run()

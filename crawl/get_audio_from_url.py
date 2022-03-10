import youtube_dl
from multiprocessing import Pool
from utils.utils import readFile, writeFile


def run(video_url):
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=video_url, download=False
        )
        filename = f"data/data_raw/thanhmai/{video_info['title'].replace('/', ' ')}.mp3"
        options = {
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': filename,
            'download_archive': filename
        }

        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([video_info['webpage_url']])

        print("Download complete... {}".format(filename))
        writeFile('done.txt', f'{video_url}')
    except:
        writeFile('error.txt', f'{video_url}')


if __name__ == '__main__':
    lst_url = readFile('data/data_url/thanhmai.txt')
    with Pool(20) as p:
        p.map(run, lst_url)

import argparse
from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Youtube Video")
    parser.add_argument("-url", "--url", type=str, help="Enter Video URl", required=True)
    args = parser.parse_args()
    Download(args.url)
# Whiper Testing

### Youtube Video Downloader
python youtube-video-downloader.py --url "https://youtu.be/CocEMWdc7Ck"

### Extract Audio
ffmpeg -i test.mp4 -map 0:a -acodec copy audio.mp4

### Generate Caption
whisper audio.flac audio.mp3 audio.wav --model medium
whisper japanese.wav --language Japanese

### Translate
whisper japanese.wav --language Japanese --task translate

### References
https://github.com/openai/whisper
https://www.baeldung.com/linux/ffmpeg-audio-from-video
https://github.com/jdepoix/youtube-transcript-api
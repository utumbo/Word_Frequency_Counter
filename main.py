import requests
import moviepy.editor as mp
import speech_recognition as sr
import re
from collections import Counter
import os

def dovnload_video(video_url, video_file):
    #download video by url
    response = requests.get(video_url)
    with open(video_file, 'wb') as file:
        file.write(response.content)

def extract_audio(video_file, audio_file):
    #extract audio by video
    video = mp.VideoFileClip(video_file)
    video.audio.write_audiofile(audio_file)

def transcribe_audio(audio_file):
    # Распознавание речи из аудио
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    return text
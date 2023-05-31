import openai
import os
import argparse
import whisper
from whisper import load_audio
import time

from dotenv import load_dotenv, find_dotenv  # need local .env file
_ = load_dotenv(find_dotenv())

openai.api_key  = os.getenv('OpenAI_Key')
# model = whisper.load_model("base")

def transcribe_wav(audio):
#    mel = whisper.log_mel_spectrogram(load_audio(audio))
#    options = whisper.DecodingOptions()
#    results = whisper.decode(model, mel, options)
#    audio_file= open(audio, "rb")
#    transcript = openai.Audio.transcribe("whisper-1", audio_file, language='ja')
    time_mark = time.asctime()
    file_name = f"./recordings/interim_wav_{time_mark}.wav"

    with open(file_name, "bx") as f:
        f.write(audio)
    with open(file_name, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file, language='ja')
    print(transcript.text)
    return transcript.text

#    audio_file= open(audio, "rb")
#    audio_file = audio
#    transcript = openai.Audio.transcribe("whisper-1", audio_file, language='ja')
#    return transcript.text

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('audio', help='Source audio file')
    args = parser.parse_args()
    transcribe_wav(args.audio)





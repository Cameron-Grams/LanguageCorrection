# Language Lab for correcting spoken Japanese

The purpose of this program is to correct a sample of spoken Japanese. This is done by creating a recording and then passing the transcribed text 
to the ChatGPT API. The transcription is managed using OpenAI's Whisper API. The app requires an environmental variable `OpenAI_Key` with your key for OpenAI's API [reference](https://platform.openai.com/docs/api-reference)

The prompt for this program is focused on correcting the speach and providing a corrected example in Hiragana and common Kanji, and identifying 
grammatical errors. Japanese is selected on the whisper API and specified in the prompt.  Another language could be corrected if the prompt and 
Whisper settings are changed.  ChatGPT does make errors in both the transcription and translation.  Grammar correction seems to be more reliable. 

The recordings are stored as .wav file in the `./recordings` directory.  There is a utility program `remove_recordings.py` which will delete all the 
recordings in the directory if there is no need to save them. 

There is also a Docker image for the application:
`docker container run -e OpenAI_Key -p 8501:8501 cgrams/languagelab:v1`

It is a large image and takes some time to download and space on your drive.  It also requires your `OpenAI_Key` environmental variable with your personal key.

There are some known problems:
- The rendering of the Streamlit Audio Recorder components initially sends a recording with size 0 bytes to Whisper: Solution is to reset and repeat. 
- ChatGPT has returned responses based on more literal rendering of sounds.  Solution is to trust but verify.  

A docker image...

## Resources Used:
- [OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text)
- [OpenAI ChatGPT](https://platform.openai.com/docs/guides/chat)
- [Streamlit](https://streamlit.io/)
- [Streamlit Audio Recorder](https://github.com/stefanrmmr/streamlit_audio_recorder)

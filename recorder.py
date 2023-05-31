# Audio recording components adopted from:
# streamlit_audio_recorder by stefanrmmr (rs. analytics) - version January 2023
# https://github.com/stefanrmmr/streamlit_audio_recorder/tree/main

import streamlit as st
from st_custom_components import st_audiorec
from transcribe import transcribe_wav
import time

# Original formating choices
st.set_page_config(page_title="streamlit_audio_recorder")
# Design move app further up and remove top padding
st.markdown('''<style>.css-1egvi7u {margin-top: -3rem;}</style>''',
            unsafe_allow_html=True)
# Design change st.Audio to fixed height of 45 pixels
st.markdown('''<style>.stAudio {height: 45px;}</style>''',
            unsafe_allow_html=True)
# Design change hyperlink href link color
st.markdown('''<style>.css-v37k9u a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # darkmode
st.markdown('''<style>.css-nlntq9 a {color: #ff4c4b;}</style>''',
            unsafe_allow_html=True)  # lightmode
# -------------------------


def audiorecorder():
    """
    Function to record input using the default frontend configuration
    and send as input to OpenAI Whisper. 

    Return:
    - Japanese text from OpenAI Whisper
    """

    text = None
    
    st.title('Correction for spoken Japanese')
    st.write('\n\n')

    wav_audio_data = st_audiorec() 

    if wav_audio_data is not None:
        print(type(wav_audio_data))
        col_info, col_space = st.columns([0.57, 0.43])
        with col_info:
            st.write('\n')  # add vertical spacer
            st.write('\n')  # add vertical spacer
            st.write('What you said:')
            st.write('\n')  # add vertical spacer

        text = transcribe_wav(wav_audio_data)

    return text


if __name__ == '__main__':
    # call main function
    audiorecorder()

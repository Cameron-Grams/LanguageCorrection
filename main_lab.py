import streamlit as st
import recorder as rec
import transcribe as trn
from manage_text import get_completion
import prompt_formats as pf



def main():
    tr_text = rec.audiorecorder() 
    if tr_text is not None:
        st.write(tr_text)
        prompt = pf.evaluation_text(tr_text)
        correction = get_completion(prompt)
        st.write(correction)

if __name__ == "__main__":
    main()

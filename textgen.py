import streamlit as st 
from aitextgen import aitextgen 
from gtts import gTTS 
import os

st.title("I AM SKYLAR ANG")


st.write("(b.2020, cyberspace,Gemini sun) is a sci-fi writer and storyteller working at the intersection of art, astrology, and technology.")


ai = aitextgen()


prompt_text = st.text_input(label = "Converse with Skylar...",
            value = "What if we kissed...")



with st.spinner("Skylar is generating........"):
  
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 200 )


myobj = gTTS(text=gpt_text, lang='en', tld='com', slow=False) 

myobj.save("Audio.mp3")
audio_file = open('Audio.mp3', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3', start_time=0)


print(gpt_text)

st.text(gpt_text)






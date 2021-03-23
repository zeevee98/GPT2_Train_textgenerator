import streamlit as st #for web dev
from aitextgen import aitextgen #for ai text gen

st.title("I AM SKYLAR ANG")


st.write("(b.2020, cyberspace,Gemini sun) is a sci-fi writer and storyteller working at the intersection of art, astrology, and technology.")

# instantiate the model / download
ai = aitextgen()

# create a prompt text for the text generation 
#prompt_text = "Python is awesome"
prompt_text = st.text_input(label = "Converse with Skylar...",
            value = "Computer is beautiful")



with st.spinner("Skylar is generating........"):
    # text generation
    gpt_text = ai.generate_one(prompt=prompt_text,
            max_length = 300 )
st.success("Skylar Successfully generated the below text ")

# print ai generated text
print(gpt_text)

st.text(gpt_text)

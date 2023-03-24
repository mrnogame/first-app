from tkinter import Image
import streamlit as st

print ('funziona?')
st.text('jhshssjshsjsj hemnghre u goooohklhlhk fgufvuy')

st.title('GO')
st.text('i don charge my energey')
st.text('i no get time for enemy')
from PIL import Image
image1= Image.open('luffy.png')

st.image(image1, caption='Luffy')


import numpy as np

audio_file = open('Burna.mp3','rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/mp3 start',)
# sample_rate = 44100  # 44100 samples per second
# seconds = 2  # Note duration of 2 seconds
# frequency_la = 440  # Our played note will be 440 Hz
# # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
# t = np.linspace(0, seconds, seconds * sample_rate, False)
# # Generate a 440 Hz sine wave
# note_la = np.sin(frequency_la * t * 2 * np.pi)

# st.audio(note_la, sample_rate=sample_rate)
     


picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download={filename}.pdf">Download file</a>'

# if export_as_pdf=="Yes":
#         pdf = FPDF()
#         for fig in figs:
#             pdf.add_page()
#             with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
#                     fig.savefig(tmpfile.name,bbox_inches="tight")#)
#                     pdf.image(tmpfile.name)
#         html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Resultatfil")
#         st.markdown(html, unsafe_allow_html=True)




# primaryColor="#F63366"
# backgroundColor="#FFFFFF"
# secondaryBackgroundColor="#F0F2F6"
# textColor="#262730"
# font="sans serif"


import pandas as pd

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget":  True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)

st.dataframe(df, use_container_width=True)
import streamlit as st
from datetime import datetime
import pytz

st.write(datetime(2020, 1, 10, 10, 30, tzinfo=pytz.timezone("EST")))
# Outputs: 2020-01-10 10:30:00-05:00

df = pd.DataFrame({
  'first column': [1, 2, 3, 4, 7, 90],
  'second column': [10, 20, 30, 40,8,98]
})

st.dataframe(df)




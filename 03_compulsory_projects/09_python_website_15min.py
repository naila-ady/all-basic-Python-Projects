import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Website", page_icon=":tada:🧿", layout="wide")

# Function to load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Correct animation URL (JSON-based)
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_1pxqjqps.json")  # Developer animation

# Top Section
with st.container():
    st.subheader("Hi, I am ------")
    st.title("A web developer, AI enthusiast, and student at GIAIC")
    st.write("Passionate about agentic AI.")
    st.write("Learn more about me 👉 [Click Here](https://your-link.com)")

# What I Do Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write(
            """
            Welcome to my personal website! I'm a passionate web developer and an AI enthusiast currently 
            pursuing my studies at GIAIC. With a keen interest in agentic AI, I am driven to explore and 
            develop intelligent systems that can automate tasks, make decisions, and provide solutions to 
            real-world problems. My journey in technology has been incredibly exciting, and I continuously 
            strive to learn, grow, and apply my skills in both AI and web development. If you'd like to 
            learn more about my work and projects, feel free to explore further by clicking the link above. 
            I'm always open to new opportunities and collaborations!
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

import streamlit as st
from PIL import Image
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(current_dir, "assetsforwebsite")

st.set_page_config(page_title="My Website", page_icon=":tada:🧿", layout="wide")

         

# Top Section
with st.container():
    st.subheader("HI, I AM NAILA ADNAN")
    st.title("A web developer, AI enthusiast, and student at GIAIC")
    st.write("Passionate about agentic AI & Excited about creating innovative solutions through web development")
    st.write("Learn more about me 👉 [Click Here](https://newpf-three.vercel.app/)")

# What I Do Section
with st.container():
    st.write("---")
    left_column, right_column = st.columns((1,1))
    with left_column:
        st.markdown("# What I'm Passionate About")
        st.markdown(
            """
            <div style="font-size:26px;">
            Welcome to my personal website! I'm a passionate web developer and an AI enthusiast currently 
            pursuing my studies at GIAIC. With a keen interest in agentic AI, I am driven to learn HTML ,CSS,TYPESCRIPT,
            NExtJS,JAVASCRIPT,FIGMA ,PYTHON and to explore and 
            develop intelligent systems that can automate tasks, make decisions, and provide solutions to 
            real-world problems. My journey in technology has been incredibly exciting, and I continuously 
            strive to learn, grow, and apply my skills in both AI and web development. If you'd like to 
            learn more about my work and projects, feel free to explore further by clicking the link above. 
            I'm always open to new opportunities and collaborations!
            """ , unsafe_allow_html=True
 
        )
    with right_column:
        image_path = os.path.join(assets_dir, "developer_image.png")
        image = Image.open(image_path)
        st.image(image, caption='Web developer and AI enthusiast',use_container_width=True)
        
# projects
with st.container():
    st.write("------")
    st.header("MY PROJECTS")
    st.write("##")
    st.header("About My Projects")
    st.markdown("""My projects showcase a blend of creativity and technical skill, ranging from interactive
                web apps to AI-powered tools. I've worked with technologies like Python, Streamlit, 
                and MongoDB to build solutions that are both functional and visually engaging. Whether it's
                designing a personal portfolio, creating intelligent automation, or developing data-driven applications, 
                each project reflects my passion for learning and building with purpose.""")

    # --- Streamlit Project Section ----
    st.subheader("MY STREAMLIT PROJECT")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image_path = os.path.join(assets_dir, "lib_image.png")
        image = Image.open(image_path)
        st.image(image, caption='Library Mangement', use_container_width=True)
         
    with text_column:
        st.header("LIBRARY MANAGEMENT SYSTEM")
        st.write("Check out my latest project built with Streamlit: an interactive Library Management System.")
        st.markdown("[Watch my Streamlit Project](https://naila-ady-libraray-managementsysytem-library-management-acxkwq.streamlit.app/)")

    # --- Next.js Project Section ---
    st.subheader("MY NEXTJS PROJECT")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        image_path = os.path.join(assets_dir, "ai_website.png")
        image = Image.open(image_path)
        st.image(image, caption='Agentia AI', use_container_width=True)
        

    with text_column:
        st.header("AGENTIA AI WEBSITE")
        st.write("Check out my latest project built with Next.js: the interactive AgentiaOne website.")
        st.markdown("[Watch my Next.js Project](https://agentiaone.vercel.app/)")
    
    
    # CONTACT
    with st.container():  
        st.write("-------")
        st.header("Get In Contact With Me:")
        st.write("##")
    contact_form = """
        <style>
        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
            font-family: Arial, sans-serif;
            max-width: 400px;
        }
        label {
            font-weight: bold;
            margin-bottom: 5px;
        }
        input, textarea {
            padding: 10px;
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
            resize: vertical;
        }
        textarea {
            height: 120px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #45a049;
        }
        </style>

        <form action="https://formspree.io/f/mqapwegv" method="POST">
        <input type="hidden" name="captcha" value="false">

        <label>Your name:</label>
        <input type="text" name="name" required>

        <label>Your phone:</label>
        <input type="text" name="phone">

        <label>Your email:</label>
        <input type="email" name="email" required>

        <label>Your message:</label>
        <textarea name="message" required></textarea>

        <button type="submit">Send</button>
        </form>
        """

    left_column, right_column = st.columns((1, 2))
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    st.caption("Made by 'Naila Adnan''Web Developer 🧿 ")

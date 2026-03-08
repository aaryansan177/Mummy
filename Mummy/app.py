import streamlit as st

st.markdown(
"""
<style>
.stApp {
    background-color: #0000FF;
}
h1, h2, h3 {
    text-align: center;
}
</style>
""",
unsafe_allow_html=True
)

st.set_page_config(page_title="Happy Women's Day Mom ❤️", layout="centered")

# session control
if "page" not in st.session_state:
    st.session_state.page = "welcome"

# -----------------------
# WELCOME PAGE
# -----------------------

if st.session_state.page == "welcome":

    st.title("🌸 Happy Women's Day Mom 🌸")
    st.write("I made something special for you ❤️")

    st.image("photos/pic1.jpeg")

    if st.button("Start the Surprise 🎁"):
        st.session_state.page = "questions"
        st.rerun()


# -----------------------
# QUESTIONS
# -----------------------

elif st.session_state.page == "questions":

    st.header("Mom Test 😄")

    q1 = st.radio(
        "What do you call me at home?",
        ["Aaryan", "Rohith", "Aarya"]
    )

    q2 = st.text_input(
        "What is the first thing I say to you on call?"
    )

    q3 = st.radio(
        "What is my most played movie in the T.V.?",
        ["Salaar", "ZNMD", "ENE"]
    )

    if st.button("Submit Answers"):
        st.session_state.page = "result"
        st.rerun()


# -----------------------
# RESULT
# -----------------------

elif st.session_state.page == "result":

    st.success("🎉 You passed the Mom Test!")

    st.balloons()

    st.write("Of course you did... you're the best mom ever ❤️")

    if st.button("See Our Memories"):
        st.session_state.page = "timeline"
        st.rerun()


# -----------------------
# MEMORY TIMELINE
# -----------------------

elif st.session_state.page == "timeline":

    st.header("📖 Our Memories")

    st.write("blewblewblew")
    st.image("photos/pic1.jpeg")

    st.write("blebleble")
    st.image("photos/pic2.jpeg")

    st.write("blablabla")
    st.image("photos/pic3.jpeg")

    if st.button("Open Photo Gallery"):
        st.session_state.page = "gallery"
        st.rerun()


# -----------------------
# PHOTO GALLERY
# -----------------------

elif st.session_state.page == "gallery":

    st.header("📸 Our Favorite Photos")

    col1, col2 = st.columns(2)

    with col1:
        st.image("photos/pic1.jpeg")
        st.image("photos/pic3.jpeg")

    with col2:
        st.image("photos/pic2.jpeg")
        st.image("photos/pic4.jpeg")

    st.info("One more surprise left 👀")

    if st.button("Unlock Final Surprise"):
        st.session_state.page = "password"
        st.rerun()


# -----------------------
# PASSWORD PROTECTION
# -----------------------

elif st.session_state.page == "password":

    st.header("🔒 Enter the Secret Code")

    password = st.text_input("Hint: Birthday", type="password")

    if password == "181180":  # change this
        st.session_state.page = "video"
        st.rerun()

    if password:
        st.error("Wrong password 😄 Try again!")


# -----------------------
# FINAL VIDEO
# -----------------------

elif st.session_state.page == "video":

    st.header("💖 A Message For You Mom")

    st.balloons()

    video_file = open("assets/message.mp4", "rb")
    video_bytes = video_file.read()

    st.video(video_bytes)

    st.write("Thank you for everything. Happy Women's Day ❤️")
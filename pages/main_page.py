import streamlit as st
from PIL import Image
import os
import test_page as tp
import faq_page as faq
import map_page as mp
import web_crawling as wc

def youtube_video(youtube_url):
    """YouTube 동영상을 자동 재생 및 자동 재시작 기능과 함께 삽입합니다."""
    video_id = ""
    if "v=" in youtube_url:
        video_id = youtube_url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in youtube_url:
        video_id = youtube_url.split("youtu.be/")[1].split("?")[0]

    if video_id:
        autoplay_loop_url = f"https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&start=2"
        iframe_code = f"""
            <iframe
                width="1"
                height="1"
                src="{autoplay_loop_url}"
                frameborder="0"
                allowfullscreen
                allow="autoplay; encrypted-media; gyroscope; picture-in-picture"
            ></iframe>
        """
        st.markdown(iframe_code, unsafe_allow_html=True)
    else:
        st.error("유효한 YouTube URL이 아닙니다.")

# 페이지 설정
st.set_page_config(page_title="메인 페이지", layout="wide")

# 세션 상태 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'intro'

# 인트로 페이지
if st.session_state.page == 'intro':
    # CSS로 페이드인 효과 추가
    st.markdown("""
        <style>
            .fade-in {
                opacity: 0;
                animation: fadeIn 2s forwards;
            }
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
        </style>
    """, unsafe_allow_html=True)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "main_image.jpg")
    st.image(image_path)
    image = Image.open(image_path)

    # 클릭 유도 버튼
    if st.button("시작하기 👉"):
        st.session_state.page = '나의 성향 Test'
# 메인 페이지들
else:

    link = "https://www.youtube.com/watch?v=s3moreyqeow"
    youtube_video(link)
    
    # 사이드바
    with st.sidebar:
        st.markdown("### 메뉴")

        
        if st.button("나의 성향 Test"):
            st.session_state.page = "나의 성향 Test"
        if st.button("FAQ"):
            st.session_state.page = "FAQ"
        if st.button("실시간 투표"):
            st.session_state.page = "실시간 투표"

        wc.main()


    # 본문
    if st.session_state.page == "나의 성향 Test":
        tp.main()

    elif st.session_state.page == "FAQ":
        faq.main()

    elif st.session_state.page == "실시간 투표":
        mp.main()
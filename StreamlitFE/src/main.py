import streamlit as st
import base64

st.set_page_config(layout="wide") # 화면 구성 wide

# base64로 인코딩된 이미지를 반환하는 함수
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 상단 배경 이미지를 설정하는 함수
def set_background(png_file):
    bin_str = get_base64(png_file)
    css = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(255, 255, 255, 0.5), rgba(255, 255, 255, 0.5)), 
                    url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .title {{
        display: flex;
        justify-content: center;
        align-items: center;
        height: 60px;
        color: black;
        font-size: 3rem;
        font-weight: bold;
    }}
    .content {{
        display: grid;
        justify-content: center;
        align-items: center;
        height: 80vh;
        color: black;
        font-size: 2rem;
        font-weight: bold;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


def main():
    # 이미지 파일 경로 설정
    image_path = '../static/images/battleground1.png'
    # 배경 이미지 설정 함수 호출
    set_background(image_path)
    # 상단에 배경 이미지를 설정한 헤더 추가
    st.markdown('<div class="title">Whitezone Analysis Report</div>', unsafe_allow_html=True)
    st.markdown('<div class="content">Battle Anywhere</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)




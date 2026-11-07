
import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="환영합니다!",
    page_icon="🎉",
    layout="centered"
)

# 세션 상태 초기화
if "entered" not in st.session_state:
    st.session_state.entered = False

# CSS 디자인
st.markdown("""
<style>
/* 전체 배경 */
.stApp {
    background-color: #191970;
}

/* 기본 글씨 색상 */
.stApp, .stApp p, .stApp h1, .stApp h2,
.stApp h3, .stApp label {
    color: white !important;
}

/* 버튼 디자인 */
.stButton > button {
    background-color: #87CEFA;
    color: #191970 !important;
    border: none;
    border-radius: 10px;
    padding: 12px 35px;
    font-size: 20px;
    font-weight: bold;
}

/* 버튼 마우스 올렸을 때 */
.stButton > button:hover {
    background-color: #ADD8E6;
    color: #191970 !important;
    border: none;
}

/* 버튼 클릭 시 */
.stButton > button:active {
    background-color: #6495ED;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# 시작 화면
if not st.session_state.entered:

    st.markdown(
        "<p style='text-align:center; font-size:20px; "
        "margin-top:200px;'>아래 버튼을 눌러 시작해 보세요!</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 1, 1])

    with col2:
        if st.button("들어가기", use_container_width=True):
            st.session_state.entered = True
            st.rerun()


# 버튼 클릭 후 화면
else:

    st.markdown(
        "<h1 style='text-align:center; margin-top:150px;'>"
        "🎉 환영합니다! 🎉</h1>",
        unsafe_allow_html=True
    )

    st.balloons()

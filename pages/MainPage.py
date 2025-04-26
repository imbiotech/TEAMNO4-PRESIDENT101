import streamlit as st
from PIL import Image
import os
import TestPage as tp
import FAQPage as faq
import MapPage as mp

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

    # 이미지 파일 경로 지정
    # image_path = "../images/intro.png"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "image1.png")
    st.image(image_path)
    image = Image.open(image_path)

    # # 이미지 로드 및 표시
    # try:
    #     st.markdown(
    #         f'<img src="image_path" class="fade-in" style="width:100%;height:auto;">',
    #         unsafe_allow_html=True
    #     )
    # except FileNotFoundError:
    #     st.error("이미지를 찾을 수 없습니다. 경로를 확인해주세요.")

    # 클릭 유도 버튼
    if st.button("시작하기 👉"):
        st.session_state.page = '나의 성향 Test'

# 메인 페이지들
else:
    # 사이드바
    with st.sidebar:
        st.title('나의 성향 Test')
        st.markdown("### 메뉴")
        if st.button("나의 성향 Test"):
            st.session_state.page = "나의 성향 Test"
        if st.button("FAQ"):
            st.session_state.page = "FAQ"
        if st.button("실시간 투표"):
            st.session_state.page = "실시간 투표"

    # 본문
    if st.session_state.page == "나의 성향 Test":
        # st.title("나의 성향 Test")

        # question_1 = st.selectbox("질문 1: 당신은 어떤 활동을 선호하나요?", ["활발한 활동", "조용한 활동"])

        # if st.button('결과 보기'):
        #     if question_1 == "활발한 활동":
        #         st.success("성향: 활발한 성향")
        #     else:
        #         st.success("성향: 조용한 성향")

        tp.main()

    elif st.session_state.page == "FAQ":
        # st.title("❓ FAQ 페이지")
        # faq_dict = {
        #     "1. 25년 대선 얼마나 남았나요?": "25년 대선은 2025년 12월 1일에 진행될 예정입니다.",
        #     "2. 25년 대선은 공휴일이 아니라고요? 헐...": "맞습니다, 평일입니다.",
        #     "3. 우리회사에선 선거 당일 '정상 출근'하라고 합니다. 정당한가요?": "투표시간 보장이 필요합니다.",
        #     "4. 그럼 투표는 언제 하나요? 이번에도 사전투표를 할 수 있나요": "사전투표 가능합니다.",
        #     "5. 나는 투표 대상일까요?": "만 18세 이상 대한민국 국민이면 가능합니다.",
        #     "6. 대통령이 당선되면 임기는?": "임기는 5년, 재선 불가입니다.",
        #     "7. 독감 때문에 투표 걱정되는데, 방역은?": "마스크, 손세정제 사용 예정입니다.",
        #     "8. 독감이 급증해도 선거 진행하나요?": "예정대로 진행됩니다.",
        #     "9. 선거부정 막는 방법은?": "선관위, 경찰 감시와 처벌.",
        #     "10. 선거기간 중 주의할 점은?": "허위사실, 불법 선거운동 금지.",
        #     "11. 지난 대선 구별 결과는?": "선관위 자료 참고.",
        #     "12. 최근 여론조사 결과 확인은?": "여론조사 기관, 뉴스 참고.",
        #     "13. 선거 결과가 한국 정치에 미치는 영향은?": "5년간 정책 영향."
        # }

        # for question, answer in faq_dict.items():
        #     with st.expander(question):
        #         st.write(answer)

        faq.main()

    elif st.session_state.page == "실시간 투표":
        # st.title("🗳️ 실시간 투표 페이지")
        # st.write("아직 실시간 투표 기능은 준비 중입니다. 🚧")
        mp.main()
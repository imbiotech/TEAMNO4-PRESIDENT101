import streamlit as st
import os
import sys
import json
import candidate_sorting as cs
import candidate_matching as cm

def set_session_state():
    if "answers" not in st.session_state:
        st.session_state.answers = []

    if "questions" not in st.session_state:
        # st.session_state.questions = []
        st.session_state.questions = cs.read_promise_only()
        # st.write(questions)


# 버튼 공통 스타일
def render_button(label, selected):
    color = "red" if selected else "#E0E0E0"
    return f"""
    <button style="
        background-color: {color};
        width: 50px;
        height: 40px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
        color: black;
        cursor: pointer;
    ">{label}</button>
    """

def answer_to_questions(current_q_idx):
    # 질문 출력
    for idx in range(current_q_idx + 1):
        if idx < len(st.session_state.questions):
            selected = st.session_state.answers[idx] if idx < len(st.session_state.answers) else ""

            col1, col2, col3 = st.columns([7, 1, 1])
            with col1:
                st.markdown(
                    f"<div style='font-size:16px; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;'>Q{idx+1}. {st.session_state.questions[idx]}</div>",
                    unsafe_allow_html=True
                )
            with col2:
                if selected == "Yes":
                    if st.button(f"Yes", key=f"yes_{idx}", type="primary"):
                        st.session_state.answers[idx] = ""
                        st.rerun()
                elif selected == "":
                    if st.button(f"Yes", key=f"yes_{idx}", type="secondary"):
                        if len(st.session_state.answers) == idx:
                            st.session_state.answers.append("Yes")
                            st.rerun()
                        else:
                            st.session_state.answers[idx] = "Yes"
                            st.rerun()
                elif selected == "No":
                    if st.button(f"Yes", key=f"yes_{idx}", type="secondary"):
                        st.session_state.answers[idx] = "Yes"
                        st.rerun()
            with col3:
                if selected == "No":
                    if st.button(f"No", key=f"no_{idx}", type="primary"):
                        st.session_state.answers[idx] = ""
                        st.rerun()
                elif selected == "":
                    if st.button(f"No", key=f"no_{idx}", type="secondary"):
                        if len(st.session_state.answers) == idx:
                            st.session_state.answers.append("No")
                            st.rerun()
                        else:
                            st.session_state.answers[idx] = "No"
                            st.rerun()
                elif selected == "Yes":
                    if st.button(f"No", key=f"no_{idx}", type="secondary"):
                        st.session_state.answers[idx] = "No"
                        st.rerun()

def Save_Answer():
    result = {}
    # ★ 응답 저장
    for i, answer in enumerate(st.session_state.answers):
        result[st.session_state.questions[i]] = answer
    return result

def show_result(result):
    # 모든 질문 완료 시
    if len(st.session_state.answers) == len(st.session_state.questions):
        st.markdown("---")
        center = st.columns(3)
        with center[1]:
            if (st.button("나와 딱 맞는 대통령 보러가기 🚀")):
                

                # result를 JSON 파일로 저장
                current_dir = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(current_dir, "MySelection.json")
                with open(file_path, "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=4)

                # 후보자 정렬 및 매칭 함수 호출
                most_frequent_candidates, max_count = cm.select_most_matching_candidates(result)

                isMoreThanOne = len(most_frequent_candidates) > 1
                if isMoreThanOne:
                    st.write("후보자들:", most_frequent_candidates)
                else:
                    st.write("후보자:", most_frequent_candidates[0])
            

# ★ 디버깅용 결과 확인 (원하면 주석처리 가능)
# st.write(result)


def main():
    
    # 페이지 제목
    st.markdown("<h2>대통령과 케미찾기💕</h2>", unsafe_allow_html=True)

    set_session_state()

    # ★ result 변수 추가
    result = {}

    current_q_idx = len(st.session_state.answers)

    answer_to_questions(current_q_idx)

    result = Save_Answer()
    
    show_result(result)

    



if __name__ == "__main__":
    main()
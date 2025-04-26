import os

def create_folder_structure(base_path):
    """
    Streamlit 프로젝트 폴더 구조를 생성하는 함수
    """

    folders = [
        "data",         # 데이터 파일 (CSV, JSON 등)
        "pages",        # Streamlit 페이지 파일
        "utils",        # 유틸리티 함수
        "api",          # API 관련 코드
        "assets",       # 이미지 등 정적 파일
        "tests",        # 테스트 코드
        "config",       # 설정 파일
    ]

    # 기본 폴더 생성
    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # 각 페이지에 해당하는 Streamlit 파이썬 파일 생성
    page_files = {
        "pages/MainPage.py": "# Main Page\nimport streamlit as st\n\nst.title('Main Page')",
        "pages/TestPage.py": "# Test Page\nimport streamlit as st\n\nst.title('Test Title')",
        "pages/FAQPage.py": "# FAQ Page\nimport streamlit as st\n\nst.title('FAQ')",
        "pages/MapPage.py": "# Map Page\nimport streamlit as st\n\nst.title('Location Title')",
    }

    for page_file, initial_content in page_files.items():
        path = os.path.join(base_path, page_file)
        with open(path, "w") as f:
            f.write(initial_content)
        print(f"Created file: {path}")

if __name__ == "__main__":

    base_path = os.getcwd()

    create_folder_structure(base_path)

    print("\n프로젝트 폴더 구조 생성 완료!")
    print(f"프로젝트 폴더: {base_path}")
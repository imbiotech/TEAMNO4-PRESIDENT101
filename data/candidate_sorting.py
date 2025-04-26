import json
import os

def read_promise_json(filename="promise.json"):
  """
  동일 경로에 있는 JSON 파일을 읽어와 데이터를 반환합니다.

  Args:
    filename (str, optional): 읽어올 JSON 파일 이름. 기본값은 "promise.json".

  Returns:
    dict or list or None: JSON 파일의 데이터 (딕셔너리 또는 리스트).
                         파일이 없거나 JSON 디코딩에 실패하면 None을 반환합니다.
  """
  try:
    # 현재 스크립트 파일의 디렉토리 경로를 얻습니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 파일 경로를 조합합니다.
    file_path = os.path.join(current_dir, filename)

    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
      return data
  except FileNotFoundError:
    print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
    return None
  except json.JSONDecodeError:
    print(f"오류: '{filename}' 파일의 JSON 형식이 올바르지 않습니다.")
    return None
  except Exception as e:
    print(f"예상치 못한 오류가 발생했습니다: {e}")
    return None

# 함수 사용 예시
if __name__ == "__main__":
  promise_data = read_promise_json()
  if promise_data:
    print("promise.json 데이터:")
    print(json.dumps(promise_data, indent=2, ensure_ascii=False))
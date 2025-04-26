import json
import os
import random

def read_promise_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "promise.json")
    with open(file_path, "r", encoding="utf-8") as f:
        promise_data = json.load(f)
        return promise_data
    
def create_promise_vs_candidate_json(promise_data):
    data = {}

    for promise in promise_data:
        policy_name = promise["정책"]
        direction = promise["의견"]
        candidate = promise["후보"]

        # 정책: {의견: [후보자들]} 방식으로 데이터 구조화
        if policy_name not in data:
            data[policy_name] = {}
        if direction not in data[policy_name]:
            data[policy_name][direction] = []
        if candidate not in data[policy_name][direction]:
            data[policy_name][direction].append(candidate)
            
    return data

def call_candidate_sorting():
    # promise.json 파일 읽기
    promise_data = read_promise_json()
    
    if promise_data is None:
        return

    # 후보자 정렬 데이터 생성
    candidate_sorting_data = create_promise_vs_candidate_json(promise_data)

    return candidate_sorting_data

def read_promise_only():
    prinmises = []
    promise_date = read_promise_json()

    if promise_date is None:
        return
    
    for promise in promise_date:
        if promise["정책"] not in prinmises:
            prinmises.append(promise["정책"])

    prinmises = list(set(prinmises))

    # 무작위 섞기
    random.shuffle(prinmises)

    return prinmises
import candidate_sorting as cs
import json
import os
import random

def read_mySelection():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "my_selection.json")
    with open(file_path, "r", encoding="utf-8") as f:
        promise_data = json.load(f)
        return promise_data

def select_most_matching_candidates(candidates):
    promise_data = cs.call_candidate_sorting()
    mySelection = read_mySelection()
    
    matching_candidates = []

    for question, user_answer in mySelection.items():
        user_answer = "Y" if user_answer == "Yes" else "N"
        if question in promise_data and user_answer in promise_data[question]:
            candidates = promise_data[question][user_answer]
            for candidate in candidates:
                matching_candidates.append(candidate)

    result_list = sorted(matching_candidates)

    candidate_counts = {}
    for candidate in result_list:
        if candidate in candidate_counts:
            candidate_counts[candidate] += 1
        else:
            candidate_counts[candidate] = 1

    max_count = 0
    most_frequent_candidates = []
    for candidate, count in candidate_counts.items():
        if count > max_count:
            max_count = count
            most_frequent_candidates = [candidate]
        elif count == max_count:
            most_frequent_candidates.append(candidate)

    return most_frequent_candidates, max_count

def get_random_policy_line(data, candidate_name):
  """
  주어진 데이터에서 특정 후보의 한줄 정책을 랜덤하게 가져옵니다.

  Args:
    data (list): 정책 정보가 담긴 딕셔너리 리스트.
    candidate_name (str): 한줄 정책을 가져올 후보 이름.

  Returns:
    str or None: 해당 후보의 랜덤한 한줄 정책. 후보가 없으면 None 반환.
  """
  candidate_policies = [item["한줄 정책"] for item in data if item["후보"] == candidate_name]
  if candidate_policies:
    return random.choice(candidate_policies)
  else:
    return None
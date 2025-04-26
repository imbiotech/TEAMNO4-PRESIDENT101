import candidate_sorting as cs
import json
import os


def read_mySelection():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "MySelection.json")
    with open(file_path, "r", encoding="utf-8") as f:
        promise_data = json.load(f)
        print("promise_data:", promise_data)
        return promise_data

def select_most_matching_candidates(candidates):
    promise_data = cs.call_candidate_sorting()
    mySelection = read_mySelection()

    print("mySelection:", mySelection)
    
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
'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source: 2020 KAKAO BLIND RECRUITMENT "오픈채팅방"
'''

def solution(record):
    dic = {}
    for r in record:
        if r[0] == "E":
            lt = r.split(" ")
            dic[lt[1]] = lt[2]

        if r[0] == "C":
            lt = r.split(" ")
            dic[lt[1]] = lt[2]

    answer = []
    for r in record:
        if r[0] == "E":
            lt = r.split(" ")
            answer.append(dic[lt[1]] + "님이 들어왔습니다.")
        if r[0] == "L":
            lt = r.split(" ")
            answer.append(dic[lt[1]] + "님이 나갔습니다.")

    return answer

# Example
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
expected_result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

print(solution(record))
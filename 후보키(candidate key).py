'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : 2020 KAKAO BLIND RECRUITMENT "후보키"
comment : index를 부여하는 알고리즘을 combination을 여러번 써서 구할 수도 있지만
powerset 알고리즘을 구현하여 로직을 작성하였다.
'''


def check_min(v, candidate_key):
    for k in candidate_key:
        if all(i in v for i in k):
            return False
    return True


def check_uniq(v, relation):
    dic = {}
    for tup in relation:
        key = tuple(tup[i] for i in v)
        if key in dic:
            return False
        dic[key] = 1
    return True


def solution(relation):
    n_col = len(relation[0])
    s = [i for i in range(n_col)]
    powerset = []
    # column에 index를 부여하여, index로 구성된 부분집합을 구함
    for i in range(1, 1 << n_col):
        powerset.append([s[j] for j in range(n_col) if i & 1 << j])
    powerset.sort(key=lambda x: len(x))
    candidate_key = []
    for v in powerset:
        if len(v) > 1:
            if not check_min(v, candidate_key):
                continue
        if check_uniq(v, relation):
            candidate_key.append(v)
    print("candidate_key :", candidate_key)
    return len(candidate_key)

# Example
relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]
expected_result = 2
print(solution(relation))
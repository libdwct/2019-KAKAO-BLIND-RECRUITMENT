'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : 2020 KAKAO BLIND RECRUITMENT "실패율"
'''

def solution(N, stages):
    # [x, y]에서 x는 클리어 실패 수, y는 스테이지 도달 수
    dic = {}
    denominator = len(stages)
    max_stage = max(stages)
    for stage in range(1, max_stage + 1):
        if stage > N:
            break
        n_stop = stages.count(stage)
        dic[stage] = n_stop / denominator
        denominator -= n_stop
    answer = sorted(dic, key=lambda x: dic[x], reverse=True)

    if max_stage < N:
        answer += list(range(max_stage + 1, N + 1))

    return answer

# Example1
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
expected_result = [3,4,2,1,5]
print(solution(N, stages))

# Example2
N = 4
stages = [4,4,4,4,4]
expected_result = [4,1,2,3]
print(solution(N, stages))
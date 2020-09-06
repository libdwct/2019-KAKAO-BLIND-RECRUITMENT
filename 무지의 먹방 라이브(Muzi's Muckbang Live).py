'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : 2020 KAKAO BLIND RECRUITMENT "무지의 먹방 라이브"
comment : 처음엔 효율성을 의식해서 한 바퀴 단위로 while문을 돌렸는데도 불구하고 효율성 테스트를 통과하지 못하여,
          음식을 없앨 수 있는 시간 차(gap)를 주기로 잡고 돌렸더니 통과하였다.
'''

from collections import Counter


def solution(food_times, k):
    # wave : 사이클의 수, wave_len : 한 사이클에 남아 있는 음식의 수
    wave = 0
    wave_len = len(food_times)
    cnt = Counter(food_times)
    cnt_key = sorted(cnt.keys(), reverse=True)

    while True:
        new_wave = cnt_key.pop()
        gap = (new_wave - wave) * wave_len
        if gap > k:     # 다음 음식을 없앨 수 없는 경우
            wave += k // wave_len
            k %= wave_len
            break
        wave = new_wave
        k -= gap
        wave_len -= cnt[wave]
        if wave_len == 0:
            return -1

    idx = 0
    while True:
        if idx == len(food_times):
            return -1
        if food_times[idx] > wave:
            k -= 1
        if k < 0:
            return idx + 1
        idx += 1

# Example
food_times = [3, 1, 2]
k = 5
expect_result = 1
print(solution(food_times, k))
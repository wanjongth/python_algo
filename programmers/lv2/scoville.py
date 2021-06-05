# 매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해
# Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
# Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
# Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해
# 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

# # 시간초과, 테스트케이스 불통과
# from collections import deque
# def solution(scoville, K):
#     scoville.sort()
#     scoville = deque(scoville)
#     cnt = 0

#     while min(scoville) <= K:
#         if min(scoville) == 0:
#             return -1

#         scoville.appendleft(scoville.popleft()+(scoville.popleft()*2))
#         cnt += 1
#     return cnt

# print(solution([1, 2, 3, 9, 10, 12], 7))

# 힙 사용, 테스트케이스 적용

from collections import deque
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 0:
        if scoville[0] >= K:
            return answer
        a = heapq.heappop(scoville)
        if scoville != []:
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + (b * 2))
        answer += 1
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))


# 큐로 다시 구현 시도 - 시간은 줄고, 테스트케이스 아직 통과 못함


def solution(scoville, K):
    scoville = deque(scoville)
    cnt = 0

    while len(scoville) > 0:
        scoville.sort()
        if scoville[0] >= K:
            return cnt
        a = scoville.popleft()
        if len(scoville) != 0:
            b = scoville.popleft()
            scoville.appendleft(a + (b*2))
        cnt += 1

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))

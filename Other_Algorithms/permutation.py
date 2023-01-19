# 순열
# 1 ~ 4까지의 수 중 2개를 뽑아 한 줄로 세우는 모든 경우
import itertools

data = [1, 2, 3 ,4]

for x in itertools.permutations(data, 2):
    print(list(x), end=' ')
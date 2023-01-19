# 조합
# 1 ~ 3까지의 수 중 서로 다른 2개를 뽑는 경우의 수
import itertools

data = [1, 2, 3]

for x in itertools.combinations(data, 2):
    print(list(x), end=' ')
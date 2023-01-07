# 피보나치 함수를 Memoization방식(Top-down approach, 재귀, 캐싱)으로 구현

# 한 번 계산된 결과를 Memoization하기 위한 리스트 초기화
d = [0] * 100

def fibo(x):
    # 종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 점화식애 따라서 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
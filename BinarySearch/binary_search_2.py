# 이진 탐색 소스 코드 구현(반복문 이용)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 원소의 개수와 target 입력 받기
n, target = map(int, input().split())

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("찾고자 하는 원소가 존재하지 않습니다")
else:
    print("찾고자 하는 원소는 " + str((result+1)) + "번째에 있습니다.")
    
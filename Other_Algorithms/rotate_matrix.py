# 2차원 리스트 시계 방향 90도 회전
def roate_a_matrix_by_90_degree(arr):
    n = len(arr) # 행 길이
    m = len([arr[0]]) # 열 길이

    result = [[0] * n for _ in range(m)] # 결과 리스트

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]

    return result
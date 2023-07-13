'''
7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
1 2  # 다음 8개의 줄에 연결 정보를 제공
1 3
2 4
2 5
4 6
5 6
6 7
3 7
-> 인접행렬로 정리하라
'''

V, E = map(int, input().split())

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

# 출력
for i in range(V+1):
    print(adj_matrix[i])

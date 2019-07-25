N,M=map(int,input().split())#N은 정점, M은 간선의 수

adj_list=[[] for i in range(N)]
for i in range(M):
    #간선을 입력받은 후 무방향그래프의 인접리스트를 추가해줌
    sub=list(map(int,input().split()))
    adj_list[sub[0]].append(sub[1])
    adj_list[sub[1]].append(sub[0])
    
visited=[False]*N

def dfs(v):
    visited[v]=True#방문 표시
    print(v,' ',end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
        
print('인접 리스트 : ',adj_list)

print('DFS 방문순서 : ')

for i in range(N):
    if not visited[i]:
        dfs(i)

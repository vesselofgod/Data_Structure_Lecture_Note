N,M=map(int,input().split())#N은 정점, M은 간선의 수

adj_list=[[] for i in range(N)]
for i in range(M):
    #간선을 입력받은 후 무방향그래프의 인접리스트를 추가해줌
    sub=list(map(int,input().split()))
    adj_list[sub[0]].append(sub[1])
    adj_list[sub[1]].append(sub[0])
    
visited=[False]*N
CCList=[]

def dfs(v):
    visited[v]=True#방문 표시
    cc.append(v)
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)
        
for i in range(N):
    if not visited[i]:
        cc=[]
        dfs(i)
        CCList.append(cc)

print('연결성분 리스트 : ')

print(CCList)

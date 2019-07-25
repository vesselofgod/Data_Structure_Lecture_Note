N,M=map(int,input().split())#N은 정점, M은 간선의 수

adj_list=[[] for i in range(N)]
for i in range(M):
    #간선을 입력받은 후 무방향그래프의 인접리스트를 추가해줌
    sub=list(map(int,input().split()))
    adj_list[sub[0]].append(sub[1])
    adj_list[sub[1]].append(sub[0])
    
visited=[False]*N

def bfs(i):
    queue=[]
    visited[i]=True
    queue.append(i)
    while len(queue)!=0:
        v=queue.pop(0)#맨 앞의 원소를 빼냄
        print(v,' ',end='')
        for w in adj_list[v]:
            if not visited[w]:
                visited[w]=True
                queue.append(w)



print('BFS 방문순서 : ')

for i in range(N):
    if not visited[i]:
        bfs(i)

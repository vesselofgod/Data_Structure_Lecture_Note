N,M,K=map(int,input().split())

adj_list=[[] for i in range(N+1)]
for i in range(M):
    sub=list(map(int,input().split()))
    adj_list[sub[0]].append(sub[1])
    adj_list[sub[1]].append(sub[0])
    
for i in range(1,N+1):
    adj_list[i].sort()
    
def bfs(i):
    queue=[]
    visited[i]=True
    queue.append(i)
    while len(queue)!=0:
        v=queue.pop(0)
        print(str(v)+' ',end='')
        for w in adj_list[v]:
            if not visited[w]:
                visited[w]=True
                queue.append(w)

def dfs(v):
    visited[v]=True
    print(str(v)+' ',end='')
    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)

visited=[False]*(N+1)
dfs(K)
visited=[False]*(N+1)
print()
bfs(K)

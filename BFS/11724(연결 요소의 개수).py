N,M=map(int,input().split())

adj_list=[[] for i in range(N+1)]
for i in range(M):
    sub=list(map(int,input().split()))
    adj_list[sub[0]].append(sub[1])
    adj_list[sub[1]].append(sub[0])
    
visited=[False]*(N+1)

def bfs(i):
    queue=[]
    visited[i]=True
    queue.append(i)
    while len(queue)!=0:
        v=queue.pop(0)
        for w in adj_list[v]:
            if not visited[w]:
                visited[w]=True
                queue.append(w)

count=0

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)

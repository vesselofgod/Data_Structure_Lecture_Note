N=int(input())
for i in range(N):
    String= input()
    List=[]

    List.append(String[0])
    i=1
    j=0
    while i<len(String):
        if String[i]== '(' or String[i]== '{':
            List.append(String[i])
            i=i+1
        elif len(List)==0:
            print('NO')
            j=j+1
            break
        else:
            Right=List.pop()
            if (not (String[i]==')' and Right=='(' or String[i]=='}' and Right=='{')):
                print('NO')
                j=j+1
                break
            else:
                i=i+1

            
    if len(List)==0 and j==0:
        print('YES')
    elif j==0:
        print('NO')

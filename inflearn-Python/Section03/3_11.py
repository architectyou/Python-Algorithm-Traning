import sys
sys.stdin = open("input.txt", "r")

a = [list(map(int, input().split())) for _ in range(7)]

# 회문 : 앞에서 읽으나 뒤에서 읽으나 같은 것

# for i in range(7):
#     for j in range(7):
#         a[i][j]


## solution
        
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1

        for k in range(2):
            if a[i+k][j] != a[i+5-k-1][j]:
                break

        else : 
            cnt += 1


print(cnt)
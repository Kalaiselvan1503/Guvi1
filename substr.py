#jhfsjdhfhljs
n=int(input())
arr = []
a = 0
for q in range(n):
    arr.append(input())
for i in range(min([len(x) for x in arr])):
    temp = [arr[y][i] for y in range(n)]
    if len(set(temp)) == 1:
        a += 1
    else:
        break
print(arr[0][:a])

Copy
n = int(input())
res = 0
for _ in range(n):
    res += 1 if input()[1] == "+" else -1
print(res)

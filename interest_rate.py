A = int(input())
p = int(input())
n = int(input())

for i in range(n):
    A += A * p / 100

print(A)
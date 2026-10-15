uoc = []
def pt(a):
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            uoc.append(i)
            if i != a // i:
                uoc.append(a // i)

n = int(input())
pt(n)

ans = set()

def pt2(a, b):
    for i in range(1, int(a**0.5) + 1):
        if a % i == 0:
            k = a // i
            if i <= k:
                ans.add((b * i * (i + k), b * k * (i + k)))
for d in uoc:
    pt2(d, n // d)
for x, y in sorted(ans):
    print(x, y)
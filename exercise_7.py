a, b, c = map(int ,input().split())
if a <  c and b < c:
    print(c)
elif c < a and b < a:
    print(a)
elif a < b and c < b:
    print(b)
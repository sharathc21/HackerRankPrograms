x = int(input())

t = {}

for i in range(x):
    text = input().split()
    t[text[0]] = text[1]

while True:

    temp = input()
    if temp in t:
        print(temp + "=" + t[temp])
    else:
        print("Not found")

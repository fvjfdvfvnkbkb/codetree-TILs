inp = input()
arr = inp.split()
a = int(arr[0])
b = int(arr[1])

# 조건에 따라 결과를 출력합니다
if a > b:
    print(a * b)
elif a < b:
    print(b // a)
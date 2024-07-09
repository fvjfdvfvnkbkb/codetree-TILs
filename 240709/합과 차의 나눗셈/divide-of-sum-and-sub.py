# 두 정수를 입력받습니다
a = 10
b = 3

# 합과 차를 계산합니다
sum_ab = a + b
diff_ab = a - b

# 합을 차로 나눈 값을 계산합니다
if diff_ab != 0:
    result = sum_ab / diff_ab
else:
    result = float('inf')  # 차가 0인 경우 무한대를 반환

# 결과를 반올림하여 소수점 둘째 자리까지 출력합니다
print(f"{result:.2f}")
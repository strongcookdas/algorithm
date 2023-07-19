# 1개만 있는 숫자 출력
nums = [1, 2, 1, 3, 2]
answer = 0
for num in nums:
    # xor 연산
    answer ^= num
print(answer)

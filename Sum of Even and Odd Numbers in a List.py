numbers = [1, 2, 3, 4, 5, 6]
sum_even = 0
sum_odd = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
result = (sum_even, sum_odd)
print("Result tuple:", result)

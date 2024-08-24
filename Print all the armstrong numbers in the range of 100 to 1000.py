


# Print all the armstrong numbers in the range of 100 to 1000

for num in range(100,1000):
    hundred_digit = num // 100
    ten_digit = (num//10)%10
    one_digit = num %10
    sum_digit = (hundred_digit ** 3)+ (ten_digit **3)+ (one_digit ** 3)
    if sum_digit == num:
        print(num)
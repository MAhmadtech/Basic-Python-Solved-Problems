
# Print first 25 prime numbers
count = 0
num = 2
while count < 25:
    is_prime = True
    for i in range (2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
        count = count +1
    num = num + 1            





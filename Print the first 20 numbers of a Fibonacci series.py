



# Print the first 20 numbers of a Fibonacci series

a = 0 
b = 1
print(a)
print(b)
for i in range(18):
    c = a + b
    print(c)
    a = b 
    b = c
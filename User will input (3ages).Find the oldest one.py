

# User will input (3ages).Find the oldest one
Age1 = int(input("Enter youe first age :"))
Age2 = int(input("Enter youe second age :"))
Age3 = int(input("Enter youe third age :"))
if Age1 > Age2 and Age2 > Age3:
    oldest = Age1
elif Age2 > Age1 and Age2 > Age3:
    oldest = Age2
else:
    oldest = Age3
print ("Yoour oldest Age is :",oldest)            


# Extract username from a given email. 
# Eg if the email is ahmadbadar3635@gmail.com then the username should be ahmadbadar3635
email =(input("Entrer your email: "))
position = 0
for i in range(len(email)):
    if email[i] == '@':
        position=i
        break
username = email[:position]
print(f"The username is: {username}")


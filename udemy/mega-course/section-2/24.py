password = "Sample@123"

password_prompt = "Enter your Password: "
user_password = input(password_prompt)

while user_password != password:
    user_password = input(password_prompt)

print("Successful Login!")

# If method (Sudhansu's own)
# if (user_password == password):
#     print("Login Successful!")
# else:
#     print("Password failed, Retry again")

count = 0
while count != 6:
    count += 1
    print(count)

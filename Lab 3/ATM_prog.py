#ATM Example

password = 1234

print("Welcome to SBI ATM!")
print("Please insert your card")

upass = input("Enter your password: ")
upass = int(upass)

if upass == password:
    print("Your transaction is successful")

if upass != password:
    print("Password does not match\n")
    print("Please try again later")

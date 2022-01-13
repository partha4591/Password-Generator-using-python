# To generate a password firstly we have to import only 2 modules which is in-built in python,i.e, string and r.random
import string as st
import random as r

# Creating an empty password set
passwordSet = []

# Exception handling if the user uses some gibberish words
print('This is your new password generator!!!')
while True:
    try:
        # Asking the user to set password length
        password_length = int(input("Enter your password length: "))
        break

    except:
        print("Please give only number")

# Including all the letters(small and Capital) and symbols to the list by using string module function
passwordSet.extend(st.ascii_letters)
passwordSet.extend(st.digits)
passwordSet.extend(st.punctuation)

# Shuffling the list using shuffle method present in random module
r.shuffle(passwordSet)

# After shuffling we finally generate the new password of user-length and prints it by using join method... if we don't use join method, then it will be printed as a list
new_password = "".join(passwordSet[0:password_length])

print("Your newly generated password is\n" + new_password)

a = input()
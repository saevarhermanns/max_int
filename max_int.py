user_input= int(input("Input a number: "))

max_int=0

while user_input > 0:
    user_input=int(input("Input a number: "))
    if user_input>max_int:
        max_int=user_input


print("The maximum is", max_int)
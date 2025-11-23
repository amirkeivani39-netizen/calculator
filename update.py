while(True):
    user_input_1 = float(input("Enter the first number: "))
    user_input_2 = float(input("Enter the second number: "))
    user_input_3 = input("Enter operator: ")

    if(user_input_3 == "*") :
        print("Zarb!")
        print(user_input_1 , "zarb dar" , user_input_2 , ":" , user_input_1 * user_input_2)

    elif(user_input_3 == "+") :
        print("Be alave!")
        print(user_input_1 , "be alave" , user_input_2 , ":" , user_input_1 + user_input_2)

    elif(user_input_3 == "-") :
        print("Menha!")
        print(user_input_1 , "menhaye" , user_input_2 , ":" , user_input_1 - user_input_2)

    elif(user_input_3 == "/") :
        print("Taghsim!")
        print(user_input_1 , "taghsim bar" , user_input_2 , ":" , user_input_1 / user_input_2)

    else:
        print("Wrong entrance!")
        break
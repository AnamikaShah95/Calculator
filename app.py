try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))

    print("What kind of Operation do you want to perform.\n Press + for Addition \n Press - for Subtraction \n Press * for multipliction \n Press / for Devision")

    o = input("Enter the Operation to be performed: ")
    match o:
        case "+":
            print(f"The result is: {a + b}")
        case "-":
            print(f"The result is: {a - b}")
        case "*":
            print(f"The result is: {a * b}")
        case "/":
            print(f"The result is: {a / b}")
        case default:
            print("There was an error")
except Exception as e:
    print("Enter a valid value of a and b")
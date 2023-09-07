from calc import Calculator

'''


'''
def start_calc():
    while True:
        try:
            input_1 = int(input("Enter the first number: "))
            input_2 = int(input("Enter the second number: "))
            break
        except:
            print('The entered is not numbers')
    print("The entered first and second numbers are : ")
    print(input_1, input_2)
    my_instance = Calculator()
    choice=1
    while choice!=0:
        print("0. Exit")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        choice=int(input("Enter your choice... "))
        if choice==1:
            print("The computed addition result is : ",my_instance.sum(input_1, input_2))
        elif choice==2:
            print("The computed subtraction result is : ",my_instance.sub(input_1, input_2))
        elif choice==3:
            print("The computed product result is : ",my_instance.mul(input_1, input_2))
        elif choice==4:
            print("The computed division result is : ",round(my_instance.div(input_1, input_2),3))
        # elif choice==5:
        #     print("The last: ", my_instance.last())
        # elif choice==6:
        #     print("The history: ", my_instance.history())
        elif choice==0:
            print("Exit")
        else:
            print("Sorry, invalid choice!")
    print()


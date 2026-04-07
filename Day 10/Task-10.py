# Functions without return
def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    formatted_f_name = f_name.title()
    formatted_l_name = (l_name.title()) 

    print(f"{formatted_f_name} {formatted_l_name}")
    return(f"{formatted_f_name} {formatted_l_name}")


format_name( f_name="angela", l_name="AngelA")


# Functions with a return
def format_name(f_name, l_name):
    # print(f_name.title())
    # print(l_name.title())
    formatted_f_name = f_name.title()
    formatted_l_name = (l_name.title()) 
    return(f"{formatted_f_name} {formatted_l_name}")


fromated_string = format_name( f_name="angela", l_name="AngelA")
print(format_name( f_name="angela", l_name="AngelA"))
print(format_name)



#Return
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return (f"Result: {formated_f_name} {formated_l_name}")

print(format_name(input("what is your first name? "), input("What is your last name? ")))


exercise ( This is a difficult challenge!(Leap Year))

#Duck string
"""exercise ( This is a difficult challenge!(Leap Year))""" 
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

print(is_leap_year(2000))


#Calculator Exercise

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2


calculator_operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():

    num1 = float(input("What is the first numnber?: "))
    should_accumulate = True
    while should_accumulate:
        for symbol in calculator_operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next numnber?: "))

        answer = calculator_operations[operation_symbol](num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, OR type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator() # recursion

calculator()

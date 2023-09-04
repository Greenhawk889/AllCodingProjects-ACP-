#This is generally a simple calculator so I decided to make it for fun.
def adding(x, y):
    return x + y

def multiplication(x, y):
    return x*y

def division(x, y):
#With division, YOU CANNOT DIVIDE BY 0 
    if y == 0:
        print("I'm sorry, you can't divide by zero, (¬_¬)")
        return 0
    
    return x/y


def subtraction (x,y):
    return x - y

def exponents (x,y):
    return x**y

#Use while statements in order to make the process of the program repetitive until the user says otherwise

while True:
    print("You could've gone to your phone for a calculator but you chose this one: (¬_¬)")
    
    print("Fine, what do you want to do?:")
    
    print("Add(Type in 'A' for add)")
    
    print("Subtract(Type in 'S' for subtract)")
    print("Multiply(Type in 'M' for multiply)")
   
    print("Divide(Type in 'D' for divide)")
    print("Exponents(Type in 'E' for exponents)")
    print("If you want to quit(which seems pretty smart to do), type in 'Q'")
    
    calc_choice = input("Make it quick, I'm getting bored:")
    
    if calc_choice == "Q":
        print("Your smart, there's definitely way more better alternatives than this one!")
        break
    
    elif calc_choice in ("A", "S", "M", "D", "E"):
        h = float(input("First #:"))
        g = float(input("Second #:"))
        
        if calc_choice == "A":
            print("Here (¬_¬): ", adding(h, g))
            
        if calc_choice == "S":
            print("Here (¬_¬): ", subtraction(h, g))
            
        if calc_choice == "M":
            print("Here (¬_¬): ", multiplication(h, g))
            
        if calc_choice == "D":
            print("Here (¬_¬): ", division(h, g))
            
        if calc_choice == "E":
            print("Here (¬_¬): ", exponents(h, g))
            
    else:
        print("Look I get it, but the programmable robot doesn't!")
            
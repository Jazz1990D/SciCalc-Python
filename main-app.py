from calculator import Calculator


def getTwoNumbers():
    a = float(input("first number? "))
    b = float(input("second number? "))
    return a, b


def displayResult(x: float):
    print(x, "\n")

def performCalcLoop(calc):
    state = 0
    while True:
        print(state)
        user=input()
        user= user. split()
        if user[0]=="C":
            state=0
        elif user(0)=="Err":
            continue
        elif user[0]=="+":
            num = float(user[1])
            state = calc.add(state,num)
        elif user[0]== "/":
            num = float(user[1])
            state = calc.divide(state,num)
        elif user[0]=="-":
            num = float(user[1])  
            state = calc.sub(state,num)
        elif user[0]=="*":
            num = float(user[1])
            state = calc.multiply(state,num) 
        elif user [0]=="sqr":
              num = float(user[1])  
              state = calc.square(state, num)
        elif user [0]=="sqrt":
              num = float(user[1])
              state = calc.squareroot(state, num)
        elif user[0]=='quit':
            break
        else:
            state = "Err"



            
        

           
# main start
def main():
    calc = Calculator()
    performCalcLoop(calc)
    print("Done Calculating.")


if __name__ == '__main__':
    main()
 
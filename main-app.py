from calculator import Calculator

def displayResult(state, mode):
    if state == 'Err':
        print(state)
        return
    match mode:
        case "decimal":
            print(float(state))
        case "binary":
            print(bin(state))
        case "octal":
            print(oct(state))
        case "hexadecimal":
            print(hex(state))
    return

def switchMode(mode):
    match mode:
        case "decimal":
            print("Switching to hexadecimal")
            return "hexadecimal"
        case "hexadecimal":
            print("Switching to binary")
            return "binary"
        case "binary":
            print("Switching to octal")
            return "Octal"
        case "Octal":
            print("switching to decimal")
            return "decimal"

def performCalcLoop(calc):
    state = 0
    mode = "decimal"
    while True:
        displayResult(state, mode)
        user=input()
        user= user.split()
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
 
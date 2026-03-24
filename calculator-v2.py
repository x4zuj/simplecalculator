while True: # we keep it running cause you might want to calculate more often
    print("Hey :)! Wanna calculate two numbers?")
    
    def begin_calc(): # function cause its more elegant, returns result string
        try:
            a = float(input("First number to calculate: ")) 
            b = float(input("Second number to calculate: "))
            # float otherwise cant calc decimals + converts to int
            
            # request operator
            print("Great! Would you like to use any of the following operators?")
            op = input("[+, -, *, /]: ")
            
            # same logic begins
            if op == "+":
                result = a + b # result variable instead of print statements everywhere
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if a or b == 0: # this prevents having 2 error messages
                    return "Division by 0 is not allowed >:(" 
                    #       ^ we get angry and return this string instead
                result = a / b
            else:
                return "That isn't an operator >:(" # we get angry again
            
            return f"Your result is: {result} :D" # happy :)
        
        except ValueError: # if python ValueError:
            return "Enter actual numbers >:(" # and angry again
    
    print(begin_calc()) # because function returns result string, print
    input("Press any key to restart. CTRL+C to terminate.") # cosmetic

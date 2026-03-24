ex_count = 1

while True: # we keep it running cause you might want to calculate more often
    if ex_count == 1:
        ex_count = ex_count + 1
        print("Hey :)! Wanna calculate two numbers?")
    else: 
        print("You again :D! I know what you want to do.")
    def begin_calc(): # function cause its more elegant, returns result string
        try:
            a = float(input("First number to calculate: ")) 
            b = float(input("Second number to calculate: "))
            # float otherwise cant calc decimals + converts to int*
            #
            # *nerdy:
            # only ints work because int is a valid float
            # strings aren't valid floats, so entering letters raises ValueError
            
            # request operator
            print("Great! Would you like to use any of the following operators?")
            op = input("[+, -, *, /]: ")
            
            # same logic begins
            if op == "+":
                result = a + b # result var instead of prints everywhere
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if 0 in (a, b): # this prevents having 2 error messages 
                       # ^ (only {b} is relevant in div but we still check {a} for your education)
                    return f"{a} divided by {b} is not allowed >:(" 
                    #      ^ we get angry and return this string instead
                result = a / b
            else:
                return "That isn't an operator >:(" # we get angry again
            
            return f"Your result is: {result} :D" # happy :)
        
        except ValueError: # if python ValueError:
            return "Enter actual numbers >:(" # and angry again
    
    print(begin_calc()) # because function returns result string, print
    input("Press any key to restart. CTRL+C to terminate.") # cosmetic

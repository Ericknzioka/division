import os
try:
    numerator = int(input("Enter a number to divide:"))
    denominator = int(input("Enter a  number to divide by: "))
    result = numerator / denominator
    print(result) 
except ZeroDivisionError as e:
    print(e)
    print("You cant divide by zero stupid kumamaye!")    

    print("something went wrong :(")   
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("this will always execute")        
        
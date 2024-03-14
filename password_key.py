import random

capitol_let = "QWERTYUIOPASDFGHJKLZXCVBNM"
small_let = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
special_char = "?,.<>!%$}(*|#@)"

upper,lower,digits,odd =True,True,True,True 

finalpass = ""
if upper:
    finalpass += capitol_let
if lower:
    finalpass += small_let
if digits:
    finalpass += numbers
if odd:
    finalpass += special_char    

length = 15
howmuch = 10

for x in range(howmuch):
    password = "".join(random.sample(finalpass,length))
    print(password)
    

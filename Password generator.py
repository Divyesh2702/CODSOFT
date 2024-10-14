import random
import string
length = int(input("Enter the length of password: "))  
lowerstr = string.ascii_lowercase
upperstr = string.ascii_uppercase
number = string.digits
symbols = string.punctuation
passall = lowerstr+upperstr+number+symbols
password = "".join(random.sample(passall,length)) 
print(f"The generated password is: {password}")
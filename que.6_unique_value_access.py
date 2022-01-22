
import json

my_file={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
 }
a=json.dumps(my_file,indent=3)
print(a)



# a=int(input("enter the number"))
# last_digit=a%10
# if 3 is last_digit:
#     print("yes")
# if 3 is not last_digit:
#     print("no")
# if last_digit%3==0:
#     print("it is divisible")
# else:
#     print("it is not divisible")
import json
x={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
sorted_string=json.dumps(x,indent=2,sort_keys=True)
print(sorted_string)
print(type(sorted_string))



# sort_keys=True



# a=str(input('enter:'))

# if 'ly' in a:
#     print(a+'ing')
# elif 'ing' in a:
#     print(a+'ly')
# else:
#     print('ly'+'ing')





# a=int(input("enter angle"))
# b=int(input("enter angle"))
# c=180-(a+b)
# print("third angle",c)



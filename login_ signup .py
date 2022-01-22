import json
import re
print("Login page")
myRL = input("Login or signup?:")
if myRL == "signup":
    Username = input("inter your Username:") 
    Pno=input("inter your pno:") 
    description = input("description:") 
    age=int(input("inter your age"))
    PW = input(" inter your Password:")
    if re.fullmatch(r'[A-Z a-z 0-9 @#$%^&*+=]{8,}',PW):
    # if re.fullmatch("[a-z][A-Z][0-9][!@#\$%\^&\*])(?=.{8,})"):
        print("strong password")
        PW1 = input("Confirm Password:")
        if PW1==PW:
            print("right password")
            dic ={"Username":Username,"Pno":Pno,"description":description,"PW":PW,"age":age,"PW":PW}
            if(PW == PW1):
                print("Registration successfully.")
                with open('Login_System_Data.json', 'w') as f:      
                    json .dump(dic,f,indent=4)
    else:
        print("Registration failed! Please confirm your Password correctly.") 

elif myRL == "Login":
    User = input(" inter your Username:") 

    Pno=input("inter your pno:") 
    description = input("description:")

    age=int(input("inter your age"))
    PW = input("Password:")

    with open('Login_System_Data.json', 'r') as f: 
        b = json.load(f)
        e=open("Login_System_Data.json","r")
        c=e.read()
        print(c)
        e.close()
        for i in b:
                if b[i]==PW or b[i]==Pno or b[i]==age or b[i]==description or b[i]==User:
                    print("login successfully")
                    break
                else:
                    print("Login failed. Wrong Username or Password .")   
                    break
else:               
    print("wrong info")



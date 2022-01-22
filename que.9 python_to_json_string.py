import json
list1=["neelam","programer","24","2400"]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]
keys=["name","disgination","age","salary"]
a={}
b={}
c={}
d={}
dic={"a":a,"b":b,"c":c,"d":d}
for i in range(len(list1)):
    a.update({keys[i]:list1[i]})
for j in range(len(list2)):
    b.update({keys[j]:list2[j]})
for k in range(len(list3)):
    c.update({keys[k]:list3[k]})
for l in range(len(list4)):
    d.update({keys[l]:list4[l]})
my_file=open("jyoti.json","w")
json.dump(dic,my_file,indent=4)
# print(my_file)

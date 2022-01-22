import json
c={"shopping_list":
 { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}
J=input("inter the items")
S=int(input("inter the quantity"))
for i in c:
    for j in c[i] :
        if J in c[i]:
            if j==c and int(c[i][j])>=S:
                print(c[i][j])
                b=int(c[i][j])-S
                c[i][j]=str(b)
                break
            elif j!=J:
                print("not available")
                break
with open("shopping.json","w") as f:
    json.dump(c,f,indent=4)
with open("shopping.json","r") as y:
    k=y.read()
print(k)
print(type(k))





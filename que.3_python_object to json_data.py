import json

my_file={
    'name': 'David', 
    'class': 'I', 
    'age': 6
}
with open("sapna.json","w") as f:
    json.dump(my_file,f ,indent=3)
# print(json.dumps(my_file))


# with open("sapna.json","r") as g:
#     json.load(g)



import json
file="text.txt"
dict={}
with open(file) as f:
    for a in f:
        key,b=a.strip().split(None ,1)
        dict[key]=b.strip()
my_file=open("jaya.json","w")
json.dump(dict,my_file)
my_file.close()
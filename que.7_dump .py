import json
dict1 ={
    "emp1": {
        "name": "Lisa",
        "designation": "programmer",
        "age": "34",
        "salary": "54000"
    },
    "emp2": {
        "name": "Elis",
        "designation": "Trainee",
        "age": "24",
        "salary": "40000"
    },
}
my_file = open("myfile.json", "w")
  
json.dump(dict1, my_file, indent = 3)
  
my_file.close()
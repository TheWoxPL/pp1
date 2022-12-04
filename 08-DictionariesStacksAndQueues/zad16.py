import json

with open("students.json", "r") as original:
    original=json.load(original)
    new_arr=[]
    for i in original:
        new_arr.append({
            "first name":i["name"],
            "last name":i["surname"],
            "student id":i["student ID"]
        })
with open("limited.json", "w") as new:
    json.dump(new_arr, new, indent=4)
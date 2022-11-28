import json

student = {
    "name": "Jan",
    "surname": "Nowak",
    "age": 20,
    "yearsOfStudying": 2,
    "fieldsOfStudy":
    {
        "UEK": "Administracja europejska",
        "AGH": "Aerospace engineering"
    },
    "hobby": ["swimming", "singing", "gym"]
}

with open("student.json", "w") as file:
    json.dump(student, indent=4, fp=file)
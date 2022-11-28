import json

dict={
    "title":"Shrek",
    "yearOfProduction":2001,
    "genre":"comedy, animation",
    "language":"english",
    "time":"95 minutes"
}

with open("favourite.json", "w") as file:
    json.dump(dict, indent=4, fp=file)
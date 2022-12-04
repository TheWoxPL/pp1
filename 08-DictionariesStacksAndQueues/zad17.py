import json

with open("euro.json", "r") as file:
    file=json.load(file)
    print("Date\t\tBuying Rate\t\tSelling Rate")
    print("==================================")
    for i in file["rates"]:
        print(f"{i['effectiveDate']}\t\t{i['bid']}\t\t{i['ask']}")
class Cell_Phone:
    def __init__(self, brand, model, phone_number):
        self.brand=brand
        self.model=model
        self.phone_number=phone_number

    def start_calling(self, destination_phone_number):
        print(f"{self.brand} {self.model} {self.phone_number} is calling to {destination_phone_number}... bzzzz.. bzz..")

    def use_light(self):
        print(f"{self.brand} {self.model} {self.phone_number} flashbangs you SURPRISE")

    def __str__(self):
         return (f"{self.brand} {self.model} {self.phone_number}")

phone=Cell_Phone("Samsung", "galaxy s22", 530530530)
print(phone)
phone.start_calling(123123132)
phone.use_light()
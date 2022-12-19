class Student:
    uni="UEK Kraków"
    id_counter=100_000
    
    def __init__(self, name, surname, field_of_study):
        self.name=name
        self.surname=surname
        self.field_of_study=field_of_study
        self.id=Student.id_counter
        Student.id_counter+=1

    def __str__(self):
        return f"{self.name} {self.surname} ({self.id}), {self.field_of_study}, {Student.uni}"

student1=Student("Anna", "Maj", "applied Informatics")
student2=Student("Karolina", "Kowalska", "Rachunkowość i finanse")
student3=Student("Łukasz", "Nowak", "Stosunki zagraniczne")
print()
print(student1)
print(student2)
print(student3)
print()
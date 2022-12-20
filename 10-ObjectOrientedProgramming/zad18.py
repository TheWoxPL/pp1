class Contact:
    def __init__(self,name,email,telephone):
        self.name=name
        self.email=email
        self.telephone=telephone

class Contact_List:
    def __init__(self):
        self.list=[]

    def add_contact(self, item):
        self.list.append(item)

    def display(self):
        for i in self.list:
            print(f"{i.name}\t{i.email}\t{i.telephone}")

contact1=Contact("John Brown", "brown@onet.pl", 555234000)
contact2=Contact('Anna May','am@o2.pl',232000199)
contact3=Contact('George Small','smallg@google.pl',222999100)
contact_list=Contact_List()
contact_list.add_contact(contact1)
contact_list.add_contact(contact2)
contact_list.add_contact(contact3)
contact_list.display()
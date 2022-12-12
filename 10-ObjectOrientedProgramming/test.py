class Test:
    lista=[]
    test_name=""
    def printList(self):
        print(self.lista)
    def printName(self):
        print(self.test_name)

test1=Test()
test2=Test()
test1.lista.append("test")

test1.printList()
test2.printList()

test1.test_name="Thomas"

test1.printName()
test2.printName()
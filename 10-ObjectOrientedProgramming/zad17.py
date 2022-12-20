class Statistics:
    def __init__(self):
        self.numbers=[]
        self.greatest=None
        self.smallest=None
        self.arithemtic_mean=None
        self.median=None

    def add_number(self):
        x=input("Enter number: ")
        self.numbers.append(x)

    def determine_greatest(self):
        print(len(self.numbers))
        # if len(self.numbers)>0:
        greatest=self.numbers[0]
        for i in range(1, len(self.numbers)):
            if i>greatest:
                greatest=i

    def determine_smallest(self):
        if len(self.numbers)>0:
            smallest=self.numbers[0]
            for i in range(1, len(self.numbers)):
                if i<smallest:
                    smallest=i

statistics=Statistics()
statistics.numbers.append(5)
statistics.numbers.append(2)
statistics.numbers.append(4)
print(statistics.numbers)
statistics.determine_greatest()
statistics.determine_smallest()
print(statistics.greatest)
# statistics.add_number()
# statistics.add_number()
# statistics.add_number()
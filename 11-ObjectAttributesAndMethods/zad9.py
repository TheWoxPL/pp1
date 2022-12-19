class Arrays():

    @staticmethod
    def print_in_col(array):
        for c in array:
            print(c)
            
    @staticmethod
    def array_of_given_number(number_of_array_elements, value_of_array_elements):
        array=[]
        for i in range(number_of_array_elements):
            array.append(value_of_array_elements)
        return array

    @staticmethod
    def array_of_given_number_in_range(number_of_array_elements, value_from, value_to):
        import random
        array=[]
        for i in range(number_of_array_elements):
            array.append(random.randint(value_from, value_to))
        return array

    @staticmethod
    def determines_the_number_of_elements(array, m,n):
        counter=0
        for i in array:
            if i>=m and i<=n:
                counter+=1
        return counter

my_array = [4,1,8,7,2]
# Arrays.print_in_col(my_array)
print(Arrays.array_of_given_number(5,3))
print(Arrays.array_of_given_number_in_range(7,1,4))
print(Arrays.determines_the_number_of_elements(my_array, 1,4))


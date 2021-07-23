############## CODE #################

class MyClass:

    def __init__(self, att):
        self.my_atribute1 = "Hello World!"
        self.my_atribute2 = att

    def my_method_1(self):
        print("\nI'm in method!\n")

    def my_method_2(self, num, mult):
        return num * mult
    

############## TESTING ################

test = MyClass("Atribute 2 testing! :)")

test.my_method_1()

method_result = test.my_method_2(3 ,2)
print(method_result)

atribute_1_result = test.my_atribute1
print("\n" + atribute_1_result)

atribute_2_result = test.my_atribute2
print("\n" + atribute_2_result)
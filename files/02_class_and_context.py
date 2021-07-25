############## ClASSES CODES #################

class MyClass:

    def __init__(self, att):
        self.my_atribute1 = "Hello World!"
        self.my_atribute2 = att

    def my_method_1(self):
        print("I'm in method!\n")

    def my_method_2(self, num, mult):
        return str(num * mult)

    def my_method_3(self):
        print("\n" + self.my_atribute1)
        print("\n" + self.my_atribute2)


class RemoteControl:

    def __init__(self, television_device, room):
        self.television_device = television_device
        self.room = room
    
    def forward_channel(self):
        print("Forward channel.")

    def back_channel(self):
        print("\nBack channel.")
        
    def choose_channel(self, channel):
        print("\nThe {} is the chosed channel!" .format(channel))


################# TESTS ####################

print("\n############## MY 1º CLASSES AND METHODS TEST ################\n")

test = MyClass("My Instance testing! :)")

test.my_method_1()

method_result = test.my_method_2(3 ,2)
print(method_result)

atribute_1_result = test.my_atribute1
print("\n" + atribute_1_result)

atribute_2_result = test.my_atribute2
print("\n" + atribute_2_result)

method_3_result = test.my_method_3()
method_3_result

print("\n############## TELEVISION CONTROL CLASS TEST ################\n")

living_room = RemoteControl("LG", "living room")

print(living_room.television_device + "\n")
print(living_room.room + "\n")

living_room.forward_channel()
living_room.back_channel()
living_room.choose_channel(6)
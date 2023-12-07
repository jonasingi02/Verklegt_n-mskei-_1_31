from model.planes import Planes
from .input_validators import *
from logic.logic_wrapper import Logic_wrapper

class planesUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print("Hvað má bjóða þér að gera:\n\n1: birta allar flugvélar\n2: bæta við flugvél\n3: uppfæra flugvél\nQ: Hætta\nB: til baka")

    
    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur:")
            command = command.lower()
            if command == "1":
                pass
            elif command == "2":
                p = Planes()
                while True:
                    p.name = input("nafn vélar (string): ")
                    try:
                        validate_name(p.name)
                        break
                    except NameLengthException:
                        pass
                    except:
                        print("some error")
                while (True):
                    p.type = input("tegund vélar (string): ")
                    try:
                        validate_name(p.type)
                        break
                    except NameLengthException:
                        pass
                    except:
                        print("some error")
                p.numseats = input("fjöldi sæta (int):")
                while(True):
                    p.manufacturer = input("framleiðandi vélar (string):")
                    try:
                        validate_name(p.type)
                        break
                    except NameLengthException:
                        pass
                    except:
                        print("some error")
                self.logic_wrapper.create_plane(p)
            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")
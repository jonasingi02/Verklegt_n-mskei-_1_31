from model.planes import Planes
from .input_validators import ValidatePlaneInfo
from logic.logic_wrapper import Logic_wrapper


class planesUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta allar flugvélar\n2: Bæta við flugvél\n3: Uppfæra flugvél\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttareitur: ")
            command = command.lower()

            if command == "1":
                result = self.logic_wrapper.get_all_planes()
                for elem in result:
                    print(f"Tegund: {elem.manufacturer}, {elem.type}, nafn: {elem.name}")
            
            elif command == "2":
                p = Planes()
                input_field = True
                while input_field:
                    validate_planes = ValidatePlaneInfo()
                    p.name = validate_planes.get_validated_string("Nafn vélar: ")
                    p.type = validate_planes.get_validated_string("Tegund vélar: ")
                    p.numseats = validate_planes.validate_num_seats()
                    p.manufacturer = validate_planes.get_validated_string("Framleiðandi vélar: ")

                    self.logic_wrapper.create_plane(p)
                    print(f"\nÞú hefur bætt við flugvélinni: {p.name}, {p.type}, fjöldi sæta {p.numseats}\n\n")
                    input_field = False

            elif command == "3":
                pass

            elif command == "q":
                return "q"

            elif command == "b":
                return "b"

            else:
                print("Virkaði ekki, reyndu aftur.")

from logic.logic_wrapper import Logic_wrapper
from model.FMVoyage import FMvoyage
from .input_validators import ValidateFMVoyageInfo


class FMVoyageUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta öll hálfkláraðar vinnuferðir\n2: Bæta við hálfkláraðri vinnuferð\n3: Uppfæra hálfkláraðar vinnuferðir\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        Validator = ValidateFMVoyageInfo(self.logic_wrapper)
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur:")
            command = command.lower()
            if command == "1":
                pass
            elif command == "2":
                v = FMvoyage()

                v.id = 1
                result = self.logic_wrapper.get_all_fmvoyages()

                for elem in result:
                    if int(elem.id) + 1 > int(v.id):
                        v.id = int(elem.id) + 1
                    v.id = str(v.id)

                while v.airport == "" :
                    print("allir áfangastaðir í kerfinu:")
                    result = self.logic_wrapper.get_all_destinations()
                    for elem in result:
                        print(elem)
                    v.airport = Validator.validate_voyage_dest(input("hvaða áfangastað (flugvöll):"))

                while v.plane == "" :
                    print("allar flugvélar í kerfinu:")
                    result = self.logic_wrapper.get_all_planes()
                    for elem in result:
                        print(elem)
                    v.plane = Validator.validate_voyage_plane(input("hvaða flugvél villt þú nota (nafn):"))

                v.date = input("Brottfarartími(01-01-01 12:00):")
                
                self.logic_wrapper.create_fmvoyage(v)
            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

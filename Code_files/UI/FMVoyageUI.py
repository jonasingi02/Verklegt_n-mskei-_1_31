from logic.logic_wrapper import Logic_wrapper
from model.FMVoyage import FMvoyage
from .input_validators import ValidateFMVoyageInfo
from prettytable import PrettyTable


class FMVoyageUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta allar hálfkláraðar vinnuferðir\n2: Bæta við hálfkláraðri vinnuferð\n3: Uppfæra hálfkláraðar vinnuferðir\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        Validator = ValidateFMVoyageInfo(self.logic_wrapper)
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                pass
            elif command == "2":
                v = FMvoyage()
                v.id = 1
                result = self.logic_wrapper.read_all_fmvoyages()

                for elem in result:
                    if int(elem.id) + 1 > int(v.id):
                        v.id = int(elem.id) + 1
                    v.id = str(v.id)

                while v.airport == "" :
                    print("Allir áfangastaðir í kerfinu: ")
                    result = self.logic_wrapper.get_all_destinations()
                    
                    destination_table = PrettyTable()
                    destination_table.field_names = ["Land", "Flugvöllur", "Flugtími", "Vegalengd", "Nafn tengiliðs", "Sími tengliðs"]
                    
                    for elem in result:
                        destination_table.add_row([elem.country, elem.airport, elem.flighttime, elem.distance, elem.name, elem.phone])
                    
                    destination_table.align = "l"
                    print(destination_table)

                    v.airport = Validator.validate_voyage_dest(input("Hvaða flugvöllur: "))

                while v.plane == "" :
                    plane_table = PrettyTable()
                    plane_table.field_names = ["Nafn", "Tegund", "Fjöldi sæta", "Framleiðandi"]
                    print("Allar flugvélar í kerfinu: ")
                    result = self.logic_wrapper.get_all_planes()
                    for elem in result:
                        plane_table.add_row([elem.name, elem.type, elem.numseats, elem.manufacturer])
                    plane_table.align = "l"
                    print(plane_table)
                    v.plane = Validator.validate_voyage_plane(input("Hvaða flugvél vilt þú nota (nafn): "))

                v.date = input("Dagsetning(01-01-01): ")
                time = input("Brottfarartími(00:00): ")
                validation = Validator.validate_time_of_takeoff(v.date ,time)
                taken_times_table = PrettyTable()
                taken_times_table.field_names = ["Vinnuferð til", "Dagsetning", "Tími"]
                taken_times_table.align = "l"

                valid = True
                while valid:
                    if validation == None:
                        v.time = time
                        valid = False
                    else:
                        for elem in validation:
                            taken_times_table.add_row([elem.airport, elem.date, elem.time])
                        print(taken_times_table)
                        print("Þessi brottfarartími er ekki laus. Veldu annan")
                        time = input("Brottfarartími(00:00): ")
                        validation = Validator.validate_time_of_takeoff(v.date ,time)
                
                self.logic_wrapper.create_fmvoyage(v)
                print(f"\nÞú hefur bætt við vinnuferðinni:\nFlugvöllur: {v.airport}\nFlugvél: {v.plane}\nDagsetning: {v.date}\nBrottfarartími: {v.time}")

            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

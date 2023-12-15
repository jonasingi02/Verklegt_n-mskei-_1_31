from logic.logic_wrapper import Logic_wrapper
from model.FMVoyage import FMvoyage
from .input_validators import ValidateFMVoyageInfo
from prettytable import PrettyTable


class FMVoyageUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("\nVelkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta allar ómannaðar vinnuferðir\n2: Bæta við vinnuferð\n3: Uppfæra upplýsingar vinnuferðar\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        Validator = ValidateFMVoyageInfo(self.logic_wrapper)
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                # Print all unmanned voyages.
                all_voyages:list = self.logic_wrapper.get_unmanned_voyages()
                all_voyages_table = PrettyTable()
                all_voyages_table.field_names = ["ID", "Dagsetning", "Brottfarartími", "Flugvél", "Flugvöllur"]

                for elem in all_voyages:
                    all_voyages_table.add_row([elem.id, elem.date, elem.time, elem.plane, elem.airport])

                all_voyages_table.align = "l"
                print(all_voyages_table)

            elif command == "2":
                # Add new unmanned voyage to system.
                print("Þú hefur valið að bæta við vinnuferð.\n")
                v = FMvoyage()
                v.id = 1
                result = self.logic_wrapper.read_all_fmvoyages()

                for elem in result:
                    if int(elem.id) + 1 > int(v.id):
                        v.id = int(elem.id) + 1
                    v.id = str(v.id)

                while v.airport == "" :
                    print("\nAllir áfangastaðir í kerfinu: ")
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
                    
                    print("\nAllar flugvélar í kerfinu: ")
                    result = self.logic_wrapper.get_all_planes()
                    
                    for elem in result:
                        plane_table.add_row([elem.name, elem.type, elem.numseats, elem.manufacturer])
                    
                    plane_table.align = "l"
                    print(plane_table)
                    v.plane = Validator.validate_voyage_plane(input("Hvaða flugvél vilt þú nota (nafn): "))

                v.date = input("\nDagsetning (DD-MM-ÁÁ): ")
                time = input("\nBrottfarartími(00:00): ")
                validation = Validator.validate_time_of_takeoff(v.date ,time)
                
                taken_times_table = PrettyTable()
                taken_times_table.field_names = ["Vinnuferð til", "Dagsetning", "Tími", "Flugnúmer"]
                taken_times_table.align = "l"

                valid = True
                while valid:
                    #Check if take-off time is available
                    if validation == None:
                        v.time = time
                        valid = False
                    else:
                        for elem in validation:
                            taken_times_table.add_row([elem.airport, elem.date, elem.time, elem.id])
                        
                        print(taken_times_table)
                        print("Þessi brottfarartími er ekki laus. Veldu annan.")
                        
                        time = input("Brottfarartími (00:00): ")
                        validation = Validator.validate_time_of_takeoff(v.date ,time)
                
                self.logic_wrapper.create_fmvoyage(v)
                print(f"\nÞú hefur bætt við vinnuferðinni:\n\nFlugvöllur: {v.airport}\nFlugvél: {v.plane}\nDagsetning: {v.date}\nBrottfarartími: {v.time}\n")

            elif command == "3":
                # Update info for a flight in the system.
                validating_input = ValidateFMVoyageInfo(self.logic_wrapper)
                voyage_list = self.logic_wrapper.read_all_fmvoyages()
                
                print("\nÞú hefur valið að uppfæra upplýsingar um flug.")
                id = id = validating_input.validate_voyage_id(voyage_list)

                print("Hvað má bjóða þér að uppfæra við flugið?\n\n")
                print("1. Dagsetning \n2. Tímasetning \n3. Flugvél \n4. Flugvöllur")
                user_input = int(input("\nInnsláttarreitur: "))

                if user_input == 1:
                    info = "dagsetning"    
                    column_to_update = 1
                    new_info = validating_input.get_validated_date()
                elif user_input == 2:
                    info = "tími"
                    column_to_update = 2
                    new_info = validating_input.get_validated_time()
                elif user_input == 3:
                    info = "flugvél"
                    column_to_update = 3
                    new_info = validating_input.validate_voyage_plane()
                elif user_input == 4:
                    info = "flugvöllur"
                    column_to_update = 4
                    new_info = validating_input.validate_voyage_dest()

                print(f"\nÞú hefur uppfært eftirfarandi: {info}, við flugið {id}.\n")
                self.logic_wrapper.update_flight_info(id, column_to_update, new_info)
            
            elif command == "q":
                return "q"
            
            elif command == "b":
                return "b"
            
            else:
                print("Virkaði ekki, reyndu aftur.")

from logic.logic_wrapper import Logic_wrapper
from model.FMVoyage import FMvoyage
from model.voyagexpilots import voyagexpilots
from model.employee import Employee
from .input_validators import ValidateFMVoyageInfo
from model.voyagexattendant import voyagexattendant
from prettytable import PrettyTable

class VoyageUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n vaktstjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta allar vinnuferðir\n2: Bæta við vinnuferð\n3: Uppfæra vinnuferðir\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        Validator = ValidateFMVoyageInfo(self.logic_wrapper)
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                  # Print all voyages.
                all_voyages:list = self.logic_wrapper.read_all_fmvoyages()
                all_voyages_table = PrettyTable()
                all_voyages_table.field_names = ["ID", "Dagsetning", "Brottfarartími", "Flugvél", "Flugvöllur"]

                for elem in all_voyages:
                    all_voyages_table.add_row([elem.id, elem.date, elem.time, elem.plane, elem.airport])

                all_voyages_table.align = "l"
                print(all_voyages_table)

            elif command == "2":

                v = FMvoyage()
                id = v.id
                while id == "":
                    result = self.logic_wrapper.get_unmanned_voyages()
                
                    voyage_table = PrettyTable()
                    voyage_table.field_names = ["ID", "Dagsetning", "Flugvél", "Flugvöllur"]
                    
                    for elem in result:
                        voyage_table.add_row([elem.id, elem.date, elem.plane, elem.airport])
                    
                    voyage_table.align = "l"
                    print(voyage_table)
                    
                    id = Validator.validate_voyage(input("\nHvaða vinnuferð viltu manna? (Id dæmi: 1)"), result)
                    print(f"Þú hefur valið að uppfæra vinnuferð {id}")

                v = self.logic_wrapper.find_voyage_by_id(id)

                voyage_list = self.logic_wrapper.same_date_voyage(v.date)

                pilotnumber = Validator.validate_number_of_staff_on_voyage("flugmanna")
                pilot = ""
                while pilot == "" :
                    print("\nAllir tiltækir flugmenn:")
                    pilots_list = self.logic_wrapper.pilots_not_in_voyage(voyage_list)
                    
                    available_pilots = PrettyTable()
                    available_pilots.field_names = ["Nafn", "Kennitala"]
                    
                    for i in pilots_list:
                        available_pilots.add_row([i.name, i.kt])
                    
                    available_pilots.align = "l"
                    print(available_pilots)
                
                    pilot = Validator.validate_voyage_staff(input("\nVeldu Yfirflugmann (kt): "), pilots_list)
                
                vxp = voyagexpilots()
                vxp.id = v.id
                vxp.kt = pilot
                vxp.main_pilot = True
                self.logic_wrapper.create_voyagexpilot(vxp)


                for _ in range(pilotnumber - 1):
                    pilot = ""
                    while pilot == "" :
                        print("\nAllir tiltækir flugmenn:")
                        pilots_list = self.logic_wrapper.pilots_not_in_voyage(voyage_list)
                        
                        available_pilots = PrettyTable()
                        available_pilots.field_names = ["Nafn", "Kennitala"]
                        
                        for i in pilots_list:
                            available_pilots.add_row([i.name, i.kt])
                        
                        available_pilots.align = "l"
                        print(available_pilots)
                    
                        pilot = Validator.validate_voyage_staff(input("\nVeldu flugmann (kt): "), pilots_list)
                    
                    vxp = voyagexpilots()
                    vxp.id = v.id
                    vxp.kt = pilot
                    self.logic_wrapper.create_voyagexpilot(vxp)

                
                
                flight_attendant_number = Validator.validate_number_of_staff_on_voyage("flugþjóna")

                print("\nAllir tiltækir flugþjónar:\n")
                flight_attendant_list = self.logic_wrapper.flight_attendants_not_in_voyage(voyage_list)
                
                available_attendants = PrettyTable()
                available_attendants.field_names = ["Nafn", "Kennitala"]
            
                for i in flight_attendant_list:
                    available_attendants.add_row([i.name, i.kt])
                
                available_attendants.align = "l"
                print(available_attendants)
                
                flight_attendant = Validator.validate_voyage_staff(input("\nVeldu Yfirflugþjón (kt): "), flight_attendant_list)
            
                vxf = voyagexattendant()
                vxf.id = v.id
                vxf.kt = flight_attendant
                vxf.main_attendant = True
                self.logic_wrapper.create_voyagexattendant(vxf)

                for _ in range(int(flight_attendant_number - 1)):
                    print("\nAllir tiltækir flugþjónar:\n")
                    flight_attendant_list = self.logic_wrapper.flight_attendants_not_in_voyage(voyage_list)
                    
                    available_attendants = PrettyTable()
                    available_attendants.field_names = ["Nafn", "Kennitala"]
                
                    for i in pilots_list:
                        available_attendants.add_row([i.name, i.kt])
                    
                    available_attendants.align = "l"
                    print(available_attendants)
                    
                    flight_attendant = Validator.validate_voyage_staff(input("\nVeldu flugþjón (kt): "), flight_attendant_list)
                
                    vxf = voyagexattendant()
                    vxf.id = v.id
                    vxf.kt = flight_attendant
                    self.logic_wrapper.create_voyagexattendant(vxf)
                
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

                print(f"\nÞú hefur uppfært eftirfarandi: {info}, við flugið {id}\n.")
                self.logic_wrapper.update_flight_info(id, column_to_update, new_info)

            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

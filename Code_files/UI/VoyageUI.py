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
        print("Velkomin/n ferðastjóri")
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
                pass
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
                    
                    id = Validator.validate_voyage(input("Hvaða vinnuferð viltu manna? (Id dæmi: 1)(b: til baka)"), result)

                    if id == "b" or id == "B":
                        return
                    

                    print(f"Þú hefur valið að uppfæra vinnuferð {id}")

                v = self.logic_wrapper.find_voyage_by_id(id)

                voyage_list = self.logic_wrapper.same_date_voyage(v.date)

                pilotnumber = Validator.validate_number_of_staff_on_voyage("flugmanna")
                for _ in range(pilotnumber):
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
                    
                        pilot = Validator.validate_voyage_staff(input("Veldu flugmann (kt)(b: til baka):"), pilots_list)

                        if pilot == "b" or pilot == "B":
                            return
                    vxp = voyagexpilots()
                    vxp.id = v.id
                    vxp.kt = pilot
                    self.logic_wrapper.create_voyagexpilot(vxp)

                flight_attendant_number = Validator.validate_number_of_staff_on_voyage("flugþjóna")
                for _ in range(int(flight_attendant_number)):
                    print("\nAllir tiltækir flugþjónar:\n")
                    flight_attendant_list = self.logic_wrapper.flight_attendants_not_in_voyage(voyage_list)
                    
                    available_attendants = PrettyTable()
                    available_attendants.field_names = ["Nafn", "Kennitala"]
                
                    for i in pilots_list:
                        available_attendants.add_row([i.name, i.kt])
                    
                    available_attendants.align = "l"
                    print(available_attendants)
                    
                    flight_attendant = Validator.validate_voyage_staff(input("Veldu flugþjón (kt)(b: til baka):"), flight_attendant_list)

                    if flight_attendant == "b" or flight_attendant == "B":
                        return
                
                vxf = voyagexattendant()
                vxf.id = v.id
                vxf.kt = flight_attendant
                self.logic_wrapper.create_voyagexattendant(vxf)
                
            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

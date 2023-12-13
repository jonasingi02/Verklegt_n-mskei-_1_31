from logic.logic_wrapper import Logic_wrapper
from model.FMVoyage import FMvoyage
from model.voyagexpilots import voyagexpilots
from model.employee import Employee
from .input_validators import ValidateFMVoyageInfo


class VoyageUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n Ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: birta allar vinnuferðir\n2: bæta við vinnuferð\n3: uppfæra vinnuferðir\nQ: Hætta\nB: til baka"
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
                while v.id == "":
                    print("\nAllar hálfkláraðar vinnuferðir:")
                    result = self.logic_wrapper.get_all_fmvoyages()
                    for elem in result:
                        print(f"id:{elem.id}, dagsetning: {elem.date}, flugvél: {elem.plane}, flugvöllur: {elem.airport}")
                        print("")
                    v = Validator.validate_voyage(input("hvaða Vinnuferð villtu uppfæra (id)?"))

                pilotnumber = input("hvað eiga margir flugmenn að vinna?")
                for i in pilotnumber:
                    pilot = ""
                    while pilot == "" :
                        print("\nAllir tiltækir flugmenn:")
                        pilots_list = []
                        voyage_list = []
                        voyage = self.logic_wrapper.get_all_fmvoyages()
                        for elem in voyage:
                            if elem.date != voyage.date:
                                voyage_list.append(elem.id)
                        
                        vxp = self.data_wrapper.get_all_voyagexpilots()
                        for elem in vxp:
                            for j in voyage_list:
                                if elem.id == voyage_list[j]:
                                    pilots_list.append(elem.kt)

                        input_validator_list = []
                        pilots = self.data_wrapper.get_all_pilots()
                        for elem in pilots:
                            for j in pilots_list:
                                if elem.kt != pilots_list.kt:
                                    input_validator_list.append(elem.kt)
                                    print(f"kt: {elem.kt} nafn: {elem.name}")
                    
                        pilot = Validator.validate_pilot(input("veldu flugmann (kt):"), input_validator_list)

                    

            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

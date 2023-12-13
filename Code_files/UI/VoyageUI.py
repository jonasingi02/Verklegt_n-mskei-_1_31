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
                id = v.id
                while id == "":
                    print("\nAllar hálfkláraðar vinnuferðir:")
                    result = self.logic_wrapper.read_all_fmvoyages()
                    for elem in result:
                        print(f"id:{elem.id}, dagsetning: {elem.date}, flugvél: {elem.plane}, flugvöllur: {elem.airport}")
                        print("")
                    id = Validator.validate_voyage(input("hvaða Vinnuferð villtu uppfæra (id)?"))
                    print(id)

                v = self.logic_wrapper.find_voyage_by_id(id)
                pilotnumber = input("hvað eiga margir flugmenn að vinna?")
                for _ in range(int(pilotnumber)):
                    pilot = ""
                    while pilot == "" :
                        print("\nAllir tiltækir flugmenn:")
                        pilots_list = []
                        voyage_list = []
                        voyage = self.logic_wrapper.read_all_fmvoyages()
                        for elem in voyage:
                            if elem.date == v.date:
                                voyage_list.append(elem.id)
                        
                        vxp = self.logic_wrapper.get_all_voyagexpilots()
                        for elem in vxp:
                            for j in voyage_list:
                                if elem.id == j:
                                    pilots_list.append(elem.kt)

                        input_validator_list = []
                        pilots = self.logic_wrapper.get_all_pilots()
                        for i in pilots:
                            bool = True
                            for j in pilots_list:
                                if i.kt == j:
                                    bool = False
                            if bool == True:
                                input_validator_list.append(i.kt)
                                print(f"kt: {i.kt} nafn: {i.name}")
                    
                        pilot = Validator.validate_pilot(input("veldu flugmann (kt):"), input_validator_list)
                    vxp = voyagexpilots()
                    vxp.id = v.id
                    vxp.kt = pilot
                    self.logic_wrapper.create_voyagexpilot(vxp)

                    

            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

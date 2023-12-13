from logic.logic_wrapper import Logic_wrapper
from model.FMVoyage import FMvoyage
from model.voyagexpilots import voyagexpilots
from model.employee import Employee
from .input_validators import ValidateFMVoyageInfo
from model.voyagexattendant import voyagexattendant


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
                    print("\nAllar hálfkláraðar vinnuferðir:\n")
                    unmanned_voyages = self.logic_wrapper.get_unmanned_voyages()
                    for elem in unmanned_voyages:
                        print(f"id:{elem.id}, dagsetning: {elem.date}, flugvél: {elem.plane}, flugvöllur: {elem.airport}")
                        print("")
                    id = Validator.validate_voyage(input("hvaða Vinnuferð villtu uppfæra (id)?"), unmanned_voyages)
                    print(id)

                v = self.logic_wrapper.find_voyage_by_id(id)

                voyage_list = self.logic_wrapper.same_date_voyage(v.date)

                pilotnumber = input("hvað eiga margir flugmenn að vinna?")
                for _ in range(int(pilotnumber)):
                    pilot = ""
                    while pilot == "" :
                        print("\nAllir tiltækir flugmenn:")
                    
                        pilots_list = self.logic_wrapper.pilots_not_in_voyage(voyage_list)

                        for i in pilots_list:
                            print(f"kt: {i.kt} nafn: {i.name}")   
                    
                        pilot = Validator.validate_pilot(input("veldu flugmann (kt):"), pilots_list)
                    vxp = voyagexpilots()
                    vxp.id = v.id
                    vxp.kt = pilot
                    self.logic_wrapper.create_voyagexpilot(vxp)

                flight_attendant_number = input("hvað eiga að vera margir flugþjónar?")
                for _ in range(int(flight_attendant_number)):
                    print("\n Allir tiltækir flugþjónar:\n")

                    flight_attendant_list = self.logic_wrapper.flight_attendants_not_in_voyage(voyage_list)

                    for i in flight_attendant_list:
                        print(f"kt: {i.kt} nafn: {i.name}")

                    flight_attendant = Validator.validate_flight_attendant(input("veldu flugþjón (kt):"), flight_attendant_list)
                vxa = voyagexattendant()
                vxa.id = v.id
                vxa.kt = flight_attendant
                self.logic_wrapper.create_voyagexattendant(vxa)


                    

            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

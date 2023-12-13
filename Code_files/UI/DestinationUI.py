from .input_validators import *
from logic.logic_wrapper import Logic_wrapper
from model.destination import destination


class destinationUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera:\n\n1: Birta alla áfangastaði\n2: Bæta við áfangastað\n3: Uppfæra upplýsingar um áfangastað\nQ: Hætta\nB: til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                #TODO: PrettyTable()
                result = self.logic_wrapper.get_all_destinations()
                for elem in result:
                    print(f"country: {elem.country}, airport: {elem.airport}")
            elif command == "2":
                d = destination()
                d.country = input("nafn áfangastaðs (string): ")
                d.airport = input("nafn flugvallar (string): ")
                d.flighttime = input("flugtími (datetime hours): ")
                d.distance = input("vegalengd í km (int): ")
                d.name = input("nafn tengiliðs (string): ")
                d.phone = input("símanúmer tengiliðs (int): ")
                self.logic_wrapper.create_destination(d)
            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

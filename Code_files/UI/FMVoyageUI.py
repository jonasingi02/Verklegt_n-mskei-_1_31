from logic.logic_wrapper import Logic_wrapper
from model.destination import destination


class destinationUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: birta öll hálfkláraðar vinnuferðir\n2: bæta við hálfkláraðri vinnuferð\n3: uppfæra hálfklárðar vinnuferðir\nQ: Hætta\nB: til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur:")
            command = command.lower()
            if command == "1":
                pass
            elif command == "2":
                d = destination()
                d.country = input("Nafn áfangastaðs:")
                d.airport = input("Nafn flugvallar (string):")
                d.flighttime = input("Flugtími (datetime hours):")
                d.distance = input("Vegalengd í km (int):")
                d.name = input("Nafn tengiliðs (string):")
                d.phone = input("Símanúmer tengiliðs (int):")
                self.logic_wrapper.create_destination(d)
            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

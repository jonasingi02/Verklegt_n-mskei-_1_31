from .PlanesUI import planesUI

class FlightManagerUI:
    def __init__(self):
        pass

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print("Hvað má bjóða þér að gera:\n\n1: uppfæra vinnuferðir\n2: uppfæra áfangastaðalista\n3: uppfæra flugvélaflota\nQ: Hætta\nB: til baka")

    
    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur:")
            command = command.lower()
            if command == "1":
                pass
            elif command == "2":
                pass
            elif command == "3":
                uip = planesUI()
                menu = uip.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")
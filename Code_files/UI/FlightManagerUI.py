from .PlanesUI import planesUI
from .DestinationUI import destinationUI
from .FMVoyageUI import FMVoyageUI
from logic.logic_wrapper import Logic_wrapper
from .ascii_art import AsciiArt

class FlightManagerUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        AsciiArt.airport_1_ascii()
        print("Velkomin/n ferðastjóri")
        print("Hvað má bjóða þér að gera?\n\n1: Uppfæra vinnuferðir\n2: Uppfæra áfangastaðalista\n3: Uppfæra flugvélaflota\nQ: Hætta\nB: Til baka")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                
                uiv = FMVoyageUI(self.logic_wrapper)
                menu = uiv.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "2":
                uid = destinationUI(self.logic_wrapper)
                menu = uid.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "3":
                uip = planesUI(self.logic_wrapper)
                menu = uip.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

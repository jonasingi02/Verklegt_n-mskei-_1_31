from .EmployeeUI import EmployeeUI
from .ShiftManagerUI import ShiftManagerUI
from .FlightManagerUI import FlightManagerUI
from .ascii_art import AsciiArt
from .CrewUI import CrewUI

class StartUI:
    def __init__(self):
        pass

    def menu_output(self):
        AsciiArt.nan_logo()
        print(f"{'Where dividing by zero makes sense!':^50}\n")

        print(
            "\nHvað má bjóða þér að sjá?\n\n1: Flugáhöfn\n2: Vaktstjóri\n3: Ferðastjóri\n4. Helstu styrktaraðilar\nQ: Hætta"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                uie = CrewUI()
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "2":
                uie = ShiftManagerUI()
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "3":
                uie = FlightManagerUI()
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "4":
                AsciiArt.pepsi_max()
            elif command == "q":
                AsciiArt.airplane_3_ascii()
                print(f"Njóttu dagsins!\n")
                break
            else:
                print("Virkaði ekki, reyndu aftur.")

from .EmployeeUI import EmployeeUI
from .ShiftManagerUI import ShiftManagerUI
from .FlightManagerUI import FlightManagerUI
from .ascii_art import AsciiArt


class StartUI:
    def __init__(self):
        pass

    def menu_output(self):
        AsciiArt.nan_logo()

        print(
            "Hvað má bjóða þér að sjá:\n1: Flugáhöfn\n2: Vaktstjóri\n3: Ferðastjóri\nQ: Hætta"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                uie = EmployeeUI()
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
            elif command == "q":
                break
            else:
                print("Virkaði ekki, reyndu aftur.")

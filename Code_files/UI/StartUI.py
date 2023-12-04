from .EmployeeUI import EmployeeUI
from .ShiftManagerUI import ShiftManagerUI
from .FlightManagerUI import FlightManagerUI


class StartUI:
    def __init__(self):
        pass

    def menu_output(self):
        print("\n███    ██  █████  ███    ██      █████  ██ ██████")
        print("████   ██ ██   ██ ████   ██     ██   ██ ██ ██   ██")
        print("██ ██  ██ ███████ ██ ██  ██     ███████ ██ ██████  ")
        print("██  ██ ██ ██   ██ ██  ██ ██     ██   ██ ██ ██   ██ ")
        print("██   ████ ██   ██ ██   ████     ██   ██ ██ ██   ██ \n")
        print(
            "Hvað má bjóða þér að sjá:\n1: Flugáhöfn\n2: Vaktstjóri\n3: Ferðastjóri\nQ: Hætta"
        )

    def input_prompt(self):
        self.menu_output()
        while True:
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                uie = EmployeeUI()
                return uie
            elif command == "2":
                uie = ShiftManagerUI()
                return uie
            elif command == "3":
                uie = FlightManagerUI()
                return uie
            elif command == "q":
                break
            else:
                print("Virkaði ekki, reyndu aftur.")

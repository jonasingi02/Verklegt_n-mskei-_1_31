from UI.EmployeeUI import EmployeeUI
from UI.ShiftManagerUI import ShiftManagerUI
from UI.FlightManagerUI import FlightManagerUI

class StartUI:
    def __init__(self):
        pass

    def menu_output(self):
        print("hvað má bjóða þér að sjá:\n1: Flugáhöfn\n2: Vaktstjóri\n3: Ferðastjóri\nq: hætta")
    
    def input_prompt(self):
        self.menu_output()
        while True:
            command = input("\nInsláttarreitur:")
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
                print("virkaði ekki, reyndu aftur")

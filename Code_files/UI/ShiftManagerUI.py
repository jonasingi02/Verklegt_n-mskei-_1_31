from .EmployeeUI import EmployeeUI
from logic.logic_wrapper import Logic_wrapper


class ShiftManagerUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        print("Velkomin/n Vaktstjóri")
        print(
            "Hvað má bjóða þér að gera:\n\n1: uppfæra starfsmenn\n2: uppfæra vinnuferðir\n3: uppfæra x\nQ: Hætta\nB: til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur:")
            command = command.lower()
            if command == "1":
                uie = EmployeeUI(self.logic_wrapper)
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "q":
                return "q"
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

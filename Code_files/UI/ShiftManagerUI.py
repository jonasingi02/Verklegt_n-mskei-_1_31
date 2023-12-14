from .EmployeeUI import EmployeeUI
from .VoyageUI import VoyageUI
from logic.logic_wrapper import Logic_wrapper
from .ascii_art import AsciiArt
from .ShiftOverviewUI import ShiftOverviewUI 

class ShiftManagerUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        AsciiArt.airplane_2_ascii()
        print("Velkomin/n Vaktstjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Uppfæra starfsmenn\n2: Uppfæra vinnuferðir\n3: Birta alla starfsmenn \n4: Skoða vaktir \nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            
            if command == "1":
                uie = EmployeeUI(self.logic_wrapper)
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            
            elif command == "2":
                uiv = VoyageUI(self.logic_wrapper)
                menu = uiv.input_prompt()
                if menu == "q":
                    return "q"
            
            elif command == "3":
                pass
            elif command == "4":
                uie = ShiftOverviewUI(self.logic_wrapper)
                menu = uie.input_prompt()
            elif command == "q":
                return "q"
            
            elif command == "b":
                return "b"
            
            else:
                print("Virkaði ekki, reyndu aftur.")

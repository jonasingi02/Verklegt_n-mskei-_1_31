from .EmployeeUI import EmployeeUI
from .VoyageUI import VoyageUI
from logic.logic_wrapper import Logic_wrapper
from .ascii_art import AsciiArt
from prettytable import PrettyTable

class ShiftManagerUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        AsciiArt.airplane_2_ascii()
        print("Velkomin/n Vaktstjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Uppfæra starfsmenn\n2: Uppfæra vinnuferðir\n3: Skoða vaktir \nQ: Hætta\nB: Til baka"
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
                print("\nÞú hefur valið að sjá allar vinnuferðir á dagsetningu.\n")
                date_input = input("Sláðu inn dagsetningu (DD-MM-ÁÁ): ")
                dates_shifts = self.logic_wrapper.get_staff_by_date(date_input)
                
                date_dest = PrettyTable()
                date_dest.field_names = ["ID", "Nafn starfsmanns", "Kennitala", "Dagsetning", "Tími", "Vinnuferð til"]
               
                if dates_shifts != None:    
                    print(f"Allar starfsmenn á vakt þann {date_input}")
                    
                    for elem in dates_shifts:
                        date_dest.add_row([elem[0],elem[1],elem[2],elem[4],elem[5], elem[6]])
                    
                    date_dest.align = "l"
                    print(date_dest)
                else:
                    print(f"\nEngar vinnuferðir eru skráðar þann {date_input}")
                                      
            elif command == "q":
                return "q"
            
            elif command == "b":
                return "b"
            
            else:
                print("Virkaði ekki, reyndu aftur.")

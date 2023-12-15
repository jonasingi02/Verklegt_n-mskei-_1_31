from .EmployeeUI import EmployeeUI
from .VoyageUI import VoyageUI
from logic.logic_wrapper import Logic_wrapper
from .ascii_art import AsciiArt
from prettytable import PrettyTable

class ShiftManagerUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        """
        Displays a menu with various options for shift management activities.

        This method prints an ASCII art representation of an airplane, followed by a greeting message. It then presents a menu offering choices related to managing employees, voyages, viewing shifts on a specific date, and navigation options like 'Quit' and 'Back'. It's designed to guide the shift manager through different management tasks.
        """
        AsciiArt.airplane_2_ascii()
        print("Velkomin/n vaktstjóri")
        print(
            "Hvað má bjóða þér að vinna í?\n\n1: Starfsmenn\n2: Vinnuferðir\n3: Skoða vaktir á ákveðinni dagsetningu\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        """
        Handles user input in response to the shift management menu options.

        This method displays the menu and processes user input for various operations such as managing employees, voyages, viewing shifts on specific dates, and handling navigation commands like 'Quit' and 'Back'. It includes directing the user to different UI classes based on their selection and performing specific actions as required.
        """
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
                print("\nÞú hefur valið að sjá alla starfsmenn sem eru að vinna á ákveðinni dagsetningu.\n")
                date_input = input("Sláðu inn dagsetningu (DD-MM-ÁÁ): ")
                dates_shifts = self.logic_wrapper.get_staff_by_date(date_input)
                attendants_shift = self.logic_wrapper.get_all_attendants_on_date(date_input)

                date_dest = PrettyTable()
                date_dest.field_names = ["ID", "Nafn starfsmanns", "Kennitala", "Starfsheiti", "Dagsetning", "Tími", "Vinnuferð til"]
               
                if dates_shifts != None:    
                    print(f"Allir starfsmenn á vakt þann {date_input}")
                    
                    for elem in dates_shifts:
                        date_dest.add_row([elem[0],elem[1],elem[2],elem[3], elem[4],elem[5], elem[6]])
                    
                    if attendants_shift != None:
                        for attendant in attendants_shift:
                            date_dest.add_row([elem[0],elem[1],elem[2],elem[3], elem[4],elem[5], elem[6]])

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

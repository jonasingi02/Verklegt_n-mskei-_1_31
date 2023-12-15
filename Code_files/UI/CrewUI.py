from logic.logic_wrapper import Logic_wrapper
from logic.EmployeeLogic import EmployeeLogic
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt
from prettytable import PrettyTable

class CrewUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        """Displays the flight crew menu and all the commands follow"""
        print("Velkomin/n flugáhafnarmeðlimur")
        print("Hvað má bjóða þér að gera?\n\n1: Sjá samstarfsfólk \n2: Sjá mínar vinnuferðir \nQ: Hætta\nB: Til baka\n")

    def input_prompt(self):
        """Input prompt for flight crew"""
        while True:
            AsciiArt.airplane_1_ascii()
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            
            if command == "1":
                # Prints all employees by calling on the read_all_employees function
                result = self.logic_wrapper.read_all_employees()
                all_staff = PrettyTable()
                all_staff.field_names = ["Nafn", "Símanúmer", "Starfsheiti"]
                for elem in result:
                   all_staff.add_row([elem.name, elem.phone_number, elem.occupation])

                all_staff.align = "l"
                print(all_staff)

            if command == "2":
                #Input prompt for user ID(SSN) and date.
                print("\nHvort vilt þú sjá?\n1. Þínar vinnuferðir í dag\n2. Þínar vinnuferðir á næstkomandi viku\n")
                user_input = input("Innsláttarreitur: ")
                user_kt = input("\nSláðu inn kennitöluna þína: ")
                date_today = input("Sláðu inn dagsetninguna í dag (DD-MM-ÁÁ): ")

                if user_input == "1":
                    #Prints the user´s voyages (shifts) according to date input.
                    today = self.logic_wrapper.get_staff_voyages_today(user_kt, date_today)
                    shift_today = PrettyTable()
                    shift_today.field_names = ["ID", "Dagsetning", "Brottfarartími", "Vinnuferð til"]
                    
                    if today != None:
                        for elem in today:
                            shift_today.add_row([elem.id, elem.date, elem.time, elem.dest])
                        shift_today.align = "l"
                        print(shift_today)
                    else:
                        print("Engar vaktir í dag.")

                elif user_input == "2":
                    #Prints the user´s voyages (shifts) for the next 7 days.
                    week = self.logic_wrapper.get_staff_voyages_week(user_kt, date_today)
                    shift_week = PrettyTable()
                    shift_week.field_names = ["ID", "Dagsetning", "Brottfarartími", "Vinnuferð til"]
                    
                    if week != None:
                        for elem in week:
                            shift_week.add_row([elem.id, elem.date, elem.time, elem.dest])
                        shift_week.align = "l"
                        print(shift_week)
                    else:
                        print("Engar vaktir á næstu 7 dögum.")
            
            if command == "b":
                #Back
                return "b"
            
            if command == "q":
                #Quit
                break 

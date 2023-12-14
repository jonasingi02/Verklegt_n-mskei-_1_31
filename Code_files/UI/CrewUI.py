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
        print("Velkomin/n flugáhafnarmeðlimur")
        print("Hvað má bjóða þér að gera?\n\n1: Sjá samstarfsfólk \n2: Sjá mínar vinnuferðir \nQ: Hætta\nB: Til baka\n")

    def input_prompt(self):
        while True:
            AsciiArt.airplane_1_ascii()
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            
            if command == "1":
                result = self.logic_wrapper.read_all_employees()
                all_staff = PrettyTable()
                all_staff.field_names = ["Nafn", "Símanúmer", "Starfsheiti"]
                for elem in result:
                   all_staff.add_row([elem.name, elem.phone_number, elem.occupation])

                all_staff.align = "l"
                print(all_staff)

            if command == "2":
                print("Hvort vilt þú sjá?\n1. Þínar vinnuferðir í dag\n2. Þínar vinnuferðir á næstkomandi viku?\n")
                user_input = input("Innsláttarreitur: ")
                user_kt = input("\nSláðu inn kennitöluna þína: ")
                date_today = input("Sláðu inn dagsetninguna í dag (01-01-01): ")

                if user_input == "1":
                    today = self.logic_wrapper.get_staff_voyages_today(user_kt, date_today)
                    print(today)
                elif user_input == "2":
                    week = self.logic_wrapper.get_staff_voyages_week(user_kt, date_today)
                    print(week)

            
            if command == "b":
                #Back
                return "b"
            
            if command == "q":
                #Quit
                break 

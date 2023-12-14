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
        print("Hvað má bjóða þér að gera?\n\n1: Sjá samstarfsfólk \n2: Sjá vinnuferðir \nQ: Hætta\nB: Til baka\n")

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
                result = self.logic_wrapper.read_all_fmvoyages()
                all_voyages = PrettyTable()
                all_voyages.field_names = ["Flugnúmer", "Dagsetning", "Brottfarartími", "Flugvél", "Flugvöllur"]
                
                for elem in result:
                    all_voyages.add_row([elem.id, elem.date, elem.time, elem.plane, elem.airport])
                
                all_voyages.align = "l"
                print(all_voyages)

            if command == "b":
                return "b"
            
            if command == "q":
                break 

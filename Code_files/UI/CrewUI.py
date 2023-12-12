from logic.logic_wrapper import Logic_wrapper
from logic.EmployeeLogic import EmployeeLogic
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt

class CrewUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        # AsciiArt.airplane_1_ascii()
        print("Velkomin/n flugáhafnarmeðlimur")
        print("Hvað má bjóða þér að gera:\n\n1: Sjá samstarfsfólk \n2: Sjá vinnuferðir \nQ: Hætta\nB: Til baka\n")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            
            if command == "1":
                result = self.logic_wrapper.read_all_employees()
                for elem in result:
                   print(f"Nafn {elem.name}, Starfsheiti: {elem.occupation}")

            if command == "2":
                result = self.logic_wrapper.get_all_fmvoyages()
                for elem in result:
                    print(f"Flugnúmer: {elem.id}, Dagsetning: {elem.date}, Flugvél: {elem.plane}, Flugvöllur: {elem.airport}")  

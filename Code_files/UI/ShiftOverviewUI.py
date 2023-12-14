from logic.logic_wrapper import Logic_wrapper
from logic.EmployeeLogic import EmployeeLogic
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt
from prettytable import PrettyTable

class ShiftOverviewUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):

        print("Hvað má bjóða þér að gera?\n\n1: Sjá lausa starfsmenn á ákveðinni dagsetningu\n2: Sjá starfsmenn sem eiga bókaða vakt á ákveðinni dagsetningu\n3: Prenta út viku vinnuyfirlit ákveðins starfsmanns\nQ: Hætta\nB: Til baka\n")


    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            
            if command == "1":
                pass
            if command == "2":
                pass
            if command == "3":
                pass
              
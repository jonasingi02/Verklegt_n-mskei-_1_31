from logic.logic_wrapper import Logic_wrapper
from logic.EmployeeLogic import EmployeeLogic
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt
from prettytable import PrettyTable
from logic.fmvoyage_logic import FmvoyageLogic

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
                date = input("Veldu dagsetningu (01-01-01) : ")
                print("Þú hefur valið dagsetninguna: " + date)

                

                # dates = PrettyTable()
                # dates.field_names = ["Date", "id"]
                result = self.logic_wrapper.find_voyage_by_date(date)
                # for elem in result:
                #     dates.add_row([elem.date,elem.id])
                # dates.align = "l"

                #Her að neðan Virkar ekki, pælingin er:

                # Result sýnir öll voyage á þessum degi
                # vxp skilar lista af voyage ID og kt flugmanna
                # pilots = ná í alla flugmenn
                # Temp listi sem geymir allar kt ef ID í vxp finnst í result (öllum voyages þann dags)
                # Ef ID finnst í result þá geymist kt
                # Ef pilot kt finnst ekki þá þýðir það að pilot sé laus.
 
                vxp = self.logic_wrapper.get_all_voyagexpilots()
                pilots = self.logic_wrapper.get_all_pilots()
                Temp = []
                for elem in vxp:
                    if elem.id in result:
                        Temp.append(elem.kt)
                for pilot in pilots:
                    for kt in Temp:
                        if pilot.kt != kt:
                            print(pilot)




            
                    
                
              


                

            if command == "2":
                pass
            if command == "3":
                pass
              
from .input_validators import *
from logic.logic_wrapper import Logic_wrapper
from model.destination import destination
from prettytable import PrettyTable


class destinationUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta alla áfangastaði\n2: Bæta við áfangastað\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            
            if command == "1":
                # Print all destinations in system
                destination_table = PrettyTable()
                destination_table.field_names = ["Land", "Flugvöllur"]
                result = self.logic_wrapper.get_all_destinations()
                for elem in result:
                    destination_table.add_row([elem.country, elem.airport])
                destination_table.align = "l"
                print(destination_table)

            elif command == "2":
                #Add destination to system
                print("\nÞú hefur valið að bæta við nýjum áfangstað.\n")
                d = destination()

                s = ValidateDestinationInputs()
                while d.country == "":
                    d.country = s.validate_destination_string(input("Nafn lands: "))
                while d.airport == "":
                    d.airport = s.validate_dest_airport(input("Nafn flugvallar: "))
                d.flighttime = input("Flugtími í klukkutímum (dæmi: 3.5): ")
                d.distance = input("Vegalengd í km (dæmi: 1234.5): ")
                d.name = input("Nafn tengiliðs: ")
                while d.country == "":
                    d.phone = s.validate_contact_phone_number(input("Símanúmer tengiliðs (dæmi: 5812345): "))
                self.logic_wrapper.create_destination(d)

                print("\nÞú hefur bætt við áfangastaðnum:")
                
                dest_table = PrettyTable()
                dest_table.field_names = ["Land", "Flugvöllur", "Tengiliður"]
                dest_table.add_row([d.country, d.airport, d.name])
                dest_table.align = "l"
                print(dest_table)

            elif command == "q":
                #Quit
                return "q"
            elif command == "b":
                #Back
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")

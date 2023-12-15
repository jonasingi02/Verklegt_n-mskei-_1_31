from .input_validators import *
from logic.logic_wrapper import Logic_wrapper
from model.destination import destination
from prettytable import PrettyTable


class destinationUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """
        Displays the travel manager menu with various options.

        This method prints a greeting message and a list of commands for the travel manager, including options to display all destinations, add a new destination, and navigation commands like 'Quit' and 'Back'.
        """
        print("Velkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta alla áfangastaði\n2: Bæta við áfangastað\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        """
        Handles user input in response to the travel manager menu options.

        This method continuously displays the menu and processes user input. It supports various operations such as printing all destinations, adding a new destination, and navigation options like 'Quit' and 'Back'. User responses are handled with appropriate actions, including input validation and system updates.
        """
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            
            if command == "1":
                # Print all destinations in system
                # Fetch and prints out all the destinations from the system.
                destination_table = PrettyTable()
                destination_table.field_names = ["Land", "Flugvöllur"]
                result = self.logic_wrapper.get_all_destinations()
                
                # Iterating over the list of destinations fetch from the system.
                for elem in result:
                    # Adding each destination´s country and airport to the table.
                    destination_table.add_row([elem.country, elem.airport])
                    # Alining the table content to the left for better layout.
                destination_table.align = "l"
                print(destination_table)

            elif command == "2":
                # Add destination to system
                print("\nÞú hefur valið að bæta við nýjum áfangstað.\n")
                d = destination()

                s = ValidateDestinationInputs()
                # Validate each input.
                while d.country == "":
                    d.country = s.validate_destination_string(input("Nafn lands: "))
                while d.airport == "":
                    d.airport = s.validate_dest_airport(input("Nafn flugvallar: "))
                d.flighttime = input("Flugtími í klukkutímum (dæmi: 3.5): ")
                d.distance = input("Vegalengd í km (dæmi: 1234.5): ")
                d.name = input("Nafn tengiliðs: ")
                while d.phone == "":
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

from model.planes import Planes
from .input_validators import ValidatePlaneInfo
from logic.logic_wrapper import Logic_wrapper
from prettytable import PrettyTable
from .ascii_art import AsciiArt

class planesUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """
        Displays a menu with various options for managing aircraft in the system.

        This method prints a menu offering choices such as viewing all aircraft, adding a new aircraft to the system, and navigation options like 'Quit' and 'Back'. It's designed to guide the user through the process of managing the aircraft fleet.
        """
        print("\nVelkomin/n ferðastjóri")
        print(
            "Hvað má bjóða þér að gera?\n\n1: Birta allar flugvélar\n2: Bæta við flugvél\nQ: Hætta\nB: Til baka"
        )

    def input_prompt(self):
        """
        Handles user input in response to the aircraft management menu options.

        This method continuously displays the menu and processes user input for operations such as displaying all aircraft in the system, adding new aircraft, and handling navigation commands like 'Quit' and 'Back'. It includes steps for input validation and appropriate actions based on the user's choice.
        """
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()

            if command == "1":
                #Retrieve all planes in system and print information.
                result = self.logic_wrapper.get_all_planes()
                plane_table = PrettyTable()
                plane_table.field_names = ["Nafn", "Tegund", "Framleiðandi", "Fjöldi sæta"]
            
                for elem in result:
                    plane_table.add_row([elem.name, elem.type, elem.manufacturer, elem.numseats])
                
                plane_table.align = "l"
                print(plane_table)
            
            elif command == "2":
                #Add new plane to system
                p = Planes()
                print("Þú hefur valið að bæta við flugvél. \n")
                
                validate_planes = ValidatePlaneInfo()
                p.name = validate_planes.get_validated_plane_name("Nafn vélar: ")
                p.type = validate_planes.get_validated_string("Tegund vélar: ")
                p.numseats = validate_planes.validate_num_seats()
                p.manufacturer = validate_planes.get_validated_string("Framleiðandi vélar: ")
                self.logic_wrapper.create_plane(p)

                print(f"\nÞú hefur bætt við flugvélinni: {p.name}, {p.type}, fjöldi sæta {p.numseats}\n\n")

            elif command == "q":
                #Quit
                AsciiArt.airplane_3_ascii()
                return "q"

            elif command == "b":
                #Go back
                return "b"

            else:
                #Invalid input
                print("Virkaði ekki, reyndu aftur.")

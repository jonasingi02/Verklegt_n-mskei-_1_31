from .PlanesUI import planesUI
from .DestinationUI import destinationUI
from .FMVoyageUI import FMVoyageUI
from logic.logic_wrapper import Logic_wrapper
from .ascii_art import AsciiArt

class FlightManagerUI:
    def __init__(self):
        self.logic_wrapper = Logic_wrapper()

    def menu_output(self):
        """
        Displays the main menu for the flight manager with various options.

        This method prints an ASCII art representation of an airport followed by a welcome message. It then presents a menu offering choices related to managing voyages, destinations, and aircraft fleets, along with navigation options like 'Quit' and 'Back'.
        """
        AsciiArt.airport_1_ascii()
        print("Velkomin/n ferðastjóri")
        print("Hvað má bjóða þér að vinna í?\n\n1: Vinnuferðum\n2: Áfangastaðalista\n3: Flugvélaflota\nQ: Hætta\nB: Til baka")

    def input_prompt(self):
        """
        Handles user input in response to the main menu options of the flight manager.

        This method displays the main menu and processes user input, facilitating navigation to specific sub-menus for managing voyages, destinations, and aircraft fleets. It also handles exit ('q') and back ('b') commands. User responses are directed to the appropriate UI classes for further actions.
        """
        while True:
            self.menu_output()
            # Getting users input and converting it to lowercase for consistency.
            command = input("\nInnsláttarreitur: ")
            command = command.lower()

            if command == "1":
            # Creating an instance of FMvoyage and displaying its menu.
                uiv = FMVoyageUI(self.logic_wrapper)
                menu = uiv.input_prompt()
                if menu == "q":
                # Exit if "q" is selected
                    return "q" 
                
            elif command == "2":
                # Hndle the destinations management operations.
                uid = destinationUI(self.logic_wrapper)
                menu = uid.input_prompt()
                if menu == "q":
                # Exit if "q" is selected.
                    return "q" 
                
            elif command == "3":
                # Handle the airplane management operations.
                uip = planesUI(self.logic_wrapper)
                menu = uip.input_prompt()
                if menu == "q":
                # Exit if "q" is selected.
                    return "q" 
                
            elif command == "q":
                # Quit the application.
                return "q" 
            
            elif command == "b":
                # Return to the previous menu.
                return "b"
            
            else:
                print("Virkaði ekki, reyndu aftur.")

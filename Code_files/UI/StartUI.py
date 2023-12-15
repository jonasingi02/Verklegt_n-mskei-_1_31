from .EmployeeUI import EmployeeUI
from .ShiftManagerUI import ShiftManagerUI
from .FlightManagerUI import FlightManagerUI
from .ascii_art import AsciiArt
from .CrewUI import CrewUI

class StartUI:
    def __init__(self):
        pass

    def menu_output(self):
        """
        Displays the main menu of the application with various options.

        This method prints the NAN logo and a welcome message, followed by a menu offering choices for navigating to different sections of the application, such as the Airport (Flugáhöfn), Shift Manager (Vaktstjóri), Flight Manager (Ferðastjóri), and viewing major sponsors. It also provides an option to exit the application ('Quit').
        """
        AsciiArt.nan_logo()
        print(f"{'Where dividing by zero makes sense!':^55}\n")

        print(
            "\nHvað má bjóða þér að sjá?\n\n1: Flugáhöfn\n2: Vaktstjóri\n3: Ferðastjóri\n4: Styrktaraðili\nQ: Hætta"
        )

    def input_prompt(self):
        """
        Handles user input in response to the main menu options of the application.

        This method displays the main menu and processes user input for navigating to different sections of the application, including the Crew UI, Shift Manager UI, and Flight Manager UI, as well as displaying sponsors' information. It also handles the 'Quit' command to exit the application. The method includes logic for user redirection and appropriate action based on the selected option.
        """
        while True:
            self.menu_output()
            command = input("\nInnsláttarreitur: ")
            command = command.lower()
            if command == "1":
                uie = CrewUI()
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "2":
                uie = ShiftManagerUI()
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "3":
                uie = FlightManagerUI()
                menu = uie.input_prompt()
                if menu == "q":
                    return "q"
            elif command == "4":
                print()
                AsciiArt.pepsi_max()
            elif command == "q":
                AsciiArt.airplane_3_ascii()
                print(f"Njóttu dagsins!\n")
                break
            else:
                print("Virkaði ekki, reyndu aftur.")

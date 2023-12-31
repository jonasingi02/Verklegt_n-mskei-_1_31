from logic.logic_wrapper import Logic_wrapper
from logic.EmployeeLogic import EmployeeLogic
from model.employee import Employee
from .input_validators import ValidatingStaffInput
from .ascii_art import AsciiArt
from prettytable import PrettyTable


class EmployeeUI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """
        Displays a menu with various employee management options.

        This method prints a menu offering several choices, such as viewing all employees, adding a new employee, updating employee information, retrieving specific employee details, and navigation options like 'Quit' and 'Back'.
        """
        print("Hvað má bjóða þér að gera?\n\n1: Sjá alla starfsmenn\n2: Bæta við starfsmanni\n3: Uppfæra upplýsingar starfsmanns\n4. Sækja upplýsingar um einstakan starfsmann\nQ: Hætta\nB: Til baka\n")

    def input_prompt(self):
        """
        Handles user input in response to the employee management menu options.

        This method continuously displays the menu and processes user input. It supports various operations such as displaying all employees, adding new employees, updating employee information, retrieving specific employee details, and handling navigation commands like 'Quit' and 'Back'. Input validation and corresponding actions are performed based on the user's choice.
        """
        while True:
            self.menu_output()
            command = input("Innsláttarreitur: ").lower()
            
            if command == "1":
                # Print all employess of NaN Air.
                table = PrettyTable()
                table.field_names = ["Nafn", "Kennitala", "Símanúmer", "Heimilisfang", "Póstnúmer", "Starfsheiti"]
                result = self.logic_wrapper.read_all_employees()
                print(f'\n{"Allir starfsmenn NaN Air":^99}')
                
                for elem in result:
                   table.add_row([elem.name, elem.kt, elem.phone_number, elem.address, elem.postal_code, elem.occupation])
                
                table.align = "l"
                print(table)

            elif command == "2":
                # Adding a new employee to the system.
                print("\nÞú hefur valið að bæta við starfsmanni í kerfið.\n")
                e = Employee()
                
                validating_input = ValidatingStaffInput()
                e.name = validating_input.get_validated_name()
                e.kt = validating_input.get_validated_kennitala()
                e.phone_number = validating_input.get_validated_phone_number()
                e.address = validating_input.get_validated_address()
                e.postal_code = validating_input.get_validated_pc()
                e.occupation = validating_input.get_validated_occupation()

                self.logic_wrapper.create_employee(e)
                print(f"\nÞú hefur bætt við starfsmanninum: {e.name}, {e.occupation}.")

            elif command == "3":
                # Update info for an employee in the system.
                validating_input = ValidatingStaffInput()
                
                print("\nÞú hefur valið að uppfæra upplýsingar um starfsmann.\n\nSláðu inn kennitölu starfsmanns til að finna þann sem þú ætlar að breyta upplýsingum um.")
                kt = (input("Sláðu inn kennitölu: "))
                print("Hvað má bjóða þér að uppfæra hjá starfsmanni?\n")
                print("1. Símanúmer \n2. Heimilisfang \n3. Póstnúmer \n4. Starfsheiti")
                user_input = int(input("\nInnsláttarreitur: "))

                if user_input == 1:
                    info = "símanúmer"    
                    column_to_update = 2
                    new_info = validating_input.get_validated_phone_number()
                elif user_input == 2:
                    info = "heimilisfang"
                    column_to_update = 3
                    new_info = validating_input.get_validated_address()
                elif user_input == 3:
                    info = "póstnúmer"
                    column_to_update = 4
                    new_info = validating_input.get_validated_pc()
                elif user_input == 4:
                    info = "starfsheiti"
                    column_to_update = 5
                    new_info = validating_input.get_validated_occupation()

                print(f"\nÞú hefur uppfært {info} starfsmanns með kennitöluna {kt}\n.")
                self.logic_wrapper.update_employee(kt, column_to_update, new_info)
            
            elif command == "4":
                #Get information for a specific employee.
                print("\nÞú hefur valið að sækja upplýsingar um einstakan starfsmann. \nSláðu inn nafn starfsmanns (nóg er að skrifa inn fyrsta nafn).\n")
                validating_input = ValidatingStaffInput()
                user_input = validating_input.get_validated_name()

                valid = True
                while valid:
                    staff_str, count = self.logic_wrapper.return_certain_employee(user_input)
                    if staff_str != None:
                        if count >= 2:
                            print(f"\nÞað eru {count} starfsmenn í kerfinu með nafnið {user_input}.\n")
                        else:
                            print(f"\nÞað er {count} starfsmaður í kerfinu með nafnið {user_input}.\n")
                        
                        print(staff_str)
                        valid = False
                    else:
                        print("Þetta nafn er ekki til í kerfinu. Reyndu aftur.\n")
                        break

            elif command == "q":
                #Quit
                return "q"
            elif command == "b":
                #Back
                return "b"
            else:
                #Invalid Input
                print("Ógilt. Reyndu aftur.")

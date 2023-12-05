class FlightManagerUI:
    def __init__(self):
        print("inside UI")

    def menu_output(self):
        print("Velkomin/n ferðastjóri")
        print("Hvað má bjóða þér að gera:\n\n1: uppfæra vinnuferðir\n2: uppfæra áfangastaðalista\n3: uppfæra flugvélaflota\nQ: Hætta\nB: til baka")

    
    def input_prompt(self):
        self.menu_output()
        while True:
            command = input("\nInnsláttarreitur:")
            command = command.lower()
            if command == "1":
                pass
            elif command == "2":
                pass
            elif command == "3":
                pass
            elif command == "q":
                break
            elif command == "b":
                return "b"
            else:
                print("Virkaði ekki, reyndu aftur.")
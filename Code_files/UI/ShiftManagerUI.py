class ShiftManagerUI:
    def __init__(self):
        print("inside UI")

    def menu_output(self):
        print("Velkomin/n vaktstjóri")
        print("Hvað má bjóða þér að gera:\n\n1: Sjá alla starfsmenn\n2: Bæta við starfsmanni\n3: Uppfæra upplýsingar starfsmanns\nQ: Hætta\nB: Til baka")

    def input_prompt(self):
        self.menu_output()
        while True:
            command = input("Innsláttarreitur: ").lower()
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
                print("Invalid input, try again.")
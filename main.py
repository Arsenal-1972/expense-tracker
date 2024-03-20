#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass
import json
while True:
    command = input("\nChoose command:")
    if command == "1":
        name  =input("Enter a transaction name: ")
        sum = input("Enter a transaction sum: ")
        category = input ("Enter transactions category: ")
        izdevums = {"Transaction name": name, "Transaction sum": sum, "Transaction category": category}
        expenses.append(izdevums) 
    elif command == "2":
        print(expenses)
        pass
    elif command == "3":
        def biggest_izdevums(expenses):
            return int(expenses["Transaction sum"])
        expenses.sort(key = biggest_izdevums)
        print(expenses[:10])
        pass
    elif command == "4":
        def smalest_izdevums(expenses):
            return int(expenses["Transaction sum"])    
        expenses.sort(key = smalest_izdevums)
        print(expenses[:10])
        pass
    elif command == "5":
        

        pass
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass


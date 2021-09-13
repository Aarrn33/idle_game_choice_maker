CHOOSING = True
best_choice = False

choices = ["Cursor", "Grandma", "Farm", "Mine", "Factory", "Bank", "Temple", "Wizard Tower", "Shipment",
           "Alchemy Lab", "Portal", "Time Machine", "Antimatter Condenser", "Prism", "Chancemaker",
           "Fractal Engine", "Javascript Console", "Idleverse"]
speeds = [0.1, 1.0, 8.0, 47.0, 260.0, 1400, 7800, 44000, 260000, 1600000, 10000000, 65000000, 430000000, 2900000000,
          21000000000, 150000000000, 1100000000000, 8300000000000]
base_prices = [15.0, 100.0, 1100.0, 12000.0, 130000.0, 1400000.0, 20000000, 330000000, 5100000000, 75000000000,
               1000000000000, 14000000000000, 170000000000000, 2100000000000000, 26000000000000000,
               310000000000000000, 71000000000000000000, 12000000000000000000000]

upgrades_choices = ["Reinforced index finger", "Carpal tunnel prevention cream"]
upgrades_conditions = ["1 cu", "1 cu"]
upgrades_prices = [100.0, 500.0]
upgrades_id = [0, 1]

data = open("data.txt", "r")
pieces = data.readline()
cps = float(data.readline())
upgrades_ids = data.readline()
data.close()

pieces = list(pieces.split(" "))
pieces = list(map(float, pieces))

upgrades_ids = list(upgrades_ids.split(" "))
try:
    upgrades_ids = list(map(int, upgrades_ids))
except ValueError:
    pass

print("Upgrades are not yet implemented")
while CHOOSING:
    time_to_upgrade = []
    for building in range(len(choices)):
        time_to_upgrade.append((base_prices[building] * (1.15 ** pieces[building])) / speeds[building])
    minimum = min(time_to_upgrade)
    for building in range(len(choices)):
        if time_to_upgrade[building] == minimum:
            best_choice = choices[building]
            pieces[building] += 1
            cps += speeds[building]
    print("The best choice is to buy a", best_choice, ".")
    continuing = str(input("Do you want to continue ?"))
    if continuing not in ["y", "Y", "yes", "Yes"]:
        CHOOSING = False


pieces = list(map(str, pieces))
pieces = " ".join(pieces)

upgrades_ids = list(map(str, upgrades_ids))
upgrades_ids = " ".join(upgrades_ids)

data = open("data.txt", "w")
data.writelines(pieces)
cps = "\n" + str(cps)
data.writelines(cps)
upgrades_ids = "\n" + str(upgrades_ids)
data.close()

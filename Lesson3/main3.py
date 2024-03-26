from auto import *

humans = list()

dmytro = Human("Dmytro", HumanRole.GUNNER)
kyrylo = Human("Kyrylo", HumanRole.DRIVER)
for human in  dmytro, kyrylo:
    humans.append(human)

Krupp = Auto("Panzer I", AutoType.TANK)
for human in humans:
    Krupp.AddDriver(human)
    Krupp.AddGunner(human)

print(Krupp)
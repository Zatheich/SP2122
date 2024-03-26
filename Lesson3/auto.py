from ls3 import HumanRole
from human import Human
from autotype import AutoType

class Auto:
    def __init__(self, model:str, type:AutoType):
        self.Model:str = model
        self.Type:AutoType = type
        self.Gunners:list = list()
        self.Drivers:list = list()
    def AddGunner(self, human:Human):
        if(isinstance(self.Drivers, list) and human.Role == HumanRole.GUNNER):
            self.Gunners.append(human)
    def AddDriver(self, human:Human):
        if(isinstance(self.Drivers, list) and human.Role == HumanRole.DRIVER):
            self.Drivers.append(human)
    def __str__(self):
        drivers:str = ''
        gunners:str = ''
        for driver in self.Drivers:
            drivers += str(driver)
        for gunner in self.Gunners:
            gunners += str(gunner)
        return (f"Drivers:\n{drivers}\n"
                f"Gunners:\n{gunners}")
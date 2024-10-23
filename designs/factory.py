from interfaces import IMageFactory
from models.mages import FireMage, IceMage, HealerMage

class MageFactory(IMageFactory):
    @staticmethod
    def create_mage(mage_type, name):
        if mage_type == "Fogo":
            return FireMage(name)
        elif mage_type == "Gelo":
            return IceMage(name)
        elif mage_type == "Cura":
            return HealerMage(name)
        else:
            raise ValueError("Tipo de mago desconhecido")

from .appliances import Appliance

def Dryer(Appliance):

    def __init__(self, color, heat_method):
        super.__init__(color, heat_method)

    def dry_clothes(setting="low"):
        if setting != "low":
          print("Please allow 40 minutes for you clothes to come out crispy.")
        else:
          print("Please allow 40 minutes for your clothes to come out soggy.")

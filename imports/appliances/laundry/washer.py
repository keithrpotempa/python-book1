from appliances import Appliance

class Washer(Appliance):

    def __init__(color, heat_method):
        super().__init__(color, heat_method)

    def wash_clothes(setting="normal"):
        if setting == "delicates":
            print("Time to wash the undies")
        elif setting == "super_scrub":
            print("Washing your diapers and bibs")
        else:
            print("Hope you didn't mix your colors and whites")

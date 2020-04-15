from appliances import Appliance

class CanOpener(Appliance):

    def __init__(self, color):
        super().__init__(color)

    def open_can(self):
        print("Tuna smells bad")

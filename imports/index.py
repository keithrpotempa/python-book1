from appliances.kitchen import Dishwasher
from appliances.laundry import Dryer
from appliances.laundry import Washer
from appliances.kitchen.utility import Refrigerator

whirlpool_dishwasher = Dishwasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

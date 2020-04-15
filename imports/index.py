from appliances import Appliance, DishWasher, Washer, Dryer, Refrigerator, CoffeeMaker, CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red")
samsung_washer.wash_clothes()

samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes("high")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

brand_can_opener = CanOpener("black")
brand_can_opener.open_can()
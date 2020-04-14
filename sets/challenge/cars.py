makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)

reporting_object = {}

def make_reporting_object():
  for make in makes:
      make_id = make[0]
      make_name = make[1]
      reporting_object[make_name] = {}
      for model in models:
          model_id = model[0]
          model_name = model[1]
          model_fk = model[2]
          if model_fk == make_id:
              reporting_object[make_name][model_name] = []
              for color in available_car_colors:
                    color_model = color[0]
                    color_id = color[1]
                    if color_model == model_id:
                        #print(colors[color_id][1])
                        for color in colors:
                            id = color[0]
                            color_name = color[1]
                            if color_id == id:
                                reporting_object[make_name][model_name].append(color_name)
  
# print(reporting_object)

def summary_report():
    for make in reporting_object.items():
        make_name = make[0]
        models = make[1]
        print(make_name)
        print("--------------------")
        for model in models.items():
            model_name = model[0]
            color_list = ", ".join(model[1])
            print(f"{model_name} is available in {color_list}")
        # Blank line between entries
        print()

make_reporting_object()        
summary_report()
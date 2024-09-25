class Meal:
    meal_count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Meal.meal_count+=1

    def add_on(self,add_on):
        add_on_dict = {"rice":2.5,"coke":3.5,"egg":2}
        for k,v in add_on_dict.items():
            if add_on == k:
                self.price = self.price+add_on_dict[k]
            else:
                raise ValueError("no such add_on")

    def __str__(self):
        return f'{self.name} pay for {self.price} dollar '
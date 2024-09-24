# %%
import random
import datetime

# creating location class
class Location:

    def __init__(self):
        self.restaurants = {}

    def add_res(self, name):
        if name not in self.restaurants:
            self.restaurants[name] = []

    def add_meal(self, res, meal):
        if res in self.restaurants:
            self.restaurants[res].append(meal)
        else:
            print(f'Please check')

    def get_res(self):
        for k, v in self.restaurants.items():
            print(k)

    def get_meals(self, res):
        return self.restaurants.get(res, [])

    def count_res(self):
        return len(self.restaurants)

    def random_res(self):
        return random.choice(list(self.restaurants.keys()))

# class for meal
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


# example of creating instance of meal
classic_beef_noodle = Meal("招牌牛肉麵", 18.8)
beef_brisket_noodle = Meal("牛暔麵", 17.8)
classic_rice_noodle = Meal("正宗過橋米線", 24.8)
spicy_seafood_rice_noodle = Meal("麻辣海鮮米線", 19.8)
stir_fry = Meal("麻辣香鍋", 24)
stir_fry.add_on("coke")

#  example of creating restaurants and meals for each restaurant
adelaide = Location()
adelaide.add_res("golden bowl")
adelaide.add_res("happy bowl")
adelaide.add_res("18 street")
adelaide.add_meal("golden bowl", classic_beef_noodle)
adelaide.add_meal("golden bowl", beef_brisket_noodle)
adelaide.add_meal("happy bowl", classic_rice_noodle)
adelaide.add_meal("happy bowl", spicy_seafood_rice_noodle)
adelaide.add_meal("18 street", stir_fry)


# time for eating outside(optional)
def is_before_six():
    now = datetime.datetime.now()
    return now.hour < 18


def main():



    action = input(f'Starting to roll the dice! Now have {adelaide.count_res()} restaurants and {Meal.meal_count} meals in total, y/n')
    if action.lower() == "y":
        selected_res = adelaide.random_res()
        selected_meal = random.choice(adelaide.get_meals(selected_res))
        print(f'Just go to {selected_res} and eat {selected_meal}')
    else:
        print("Fasting is good to you!")


if __name__ == "__main__":
    main()






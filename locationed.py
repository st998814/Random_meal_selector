import random

class Location:

    def __init__(self):
        self.restaurants = {}

    def add_res(self, name):
        if name not in self.restaurants:
            self.restaurants[name] = []
        else:
            print("Already exist")

    def add_meal(self, res, meal):
        if res in self.restaurants:
            self.restaurants[res].append(meal)
        else:
            print(f'Please check')

    def get_res(self):
        return list(self.restaurants.keys())


    def get_meals(self, res):
        return self.restaurants.get(res, [])

    def count_res(self):
        return len(self.restaurants)

    def random_res(self):
        return random.choice(list(self.restaurants.keys()))

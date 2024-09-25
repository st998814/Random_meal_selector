from locationed import Location
from meal import Meal
import json


def load_data():
    try:
        with open('restaurant_data.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}



def save_data(location):

    data = load_data()

    # Update the data with new entries from 'location'
    for res, meals in location.restaurants.items():
        if res not in data:
            data[res] = []
        data[res].extend([{'name': meal.name, 'price': meal.price} for meal in meals])

    # Now, write the updated data back to the JSON file
    with open('restaurant_data.json', 'w') as file:
        json.dump(data, file, indent=4)


def input_res(location):
    data = load_data()
    res_list = [res for res in data]

    while True:
        print(f'Now have {len(data)} restaurant: {res_list}')
        res_name = input("Please type the name of restaurant to add(or type 'e' to add meal)")
        if res_name.lower() =="e":
            break
        location.add_res(res_name)
        print(f"The restaurant added: {res_name}")







def input_meal(location):
    while True:
        check_res = input("Please type in the restaurant's name(or type 'e' to save file )")
        if check_res.lower() =="e":
            break
        meal_name = input("Please in name of meal")
        price = input("Please type in the price of this meal")
        meal = Meal(meal_name,price)
        location.add_meal(check_res,meal)













def main():
    location = Location()
    input_res(location)
    input_meal(location)
    save_data(location)

if __name__ == "__main__":
    main()








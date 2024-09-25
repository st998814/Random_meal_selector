# %%
import random
import user_input
import json





def main():
    while True:
        user_select = input(''' Welcome to random meal select system, please choice [1] rolling dice or [2] Adding meals or [3] exit
       ''')
        if user_select == "3":
            break
        if user_select == "1":
            try:
                with open('restaurant_data.json', 'r') as file:
                    data = json.load(file)
                    selected_res = random.choice(list(data.keys()))
                    meals = data[selected_res]
                if meals:
                    meal = random.choice(meals)
                    print(f'{selected_res}-{meal}')
            except(FileNotFoundError, json.JSONDecodeError):
                return "file not found"
        if user_select == "2":
            user_input.main()


if __name__ == "__main__":
    main()

import csv
import random
coffees=["americano", "latte","ice-latte", "flat-white", "ice-flat-white", "cappucino","frappe", "mocha","ice-mocha"]
moods =["tired", "normal", "energetic", "relaxed"]
weather_status=["cold" "hot", "sunny"]
previous_choice=["filter-coffee","latte", "ice-latte", "flat-white", "ice-flat-white"]
sugar_request=["sugar", "non-sugar"]
milk_choice=["milk","non-milk","oat-milk", "lactose-free-milk", "almond-milk"]

with open("augmented_dataset.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["time","mood", "weather_status", "previous_choice", "sugar_request", "milk_choice", "coffee_recommendation"])


    for _ in range(200):
        row=[

            random.randint(8,22),
            random.choice(moods),
            random.choice(weather_status),
            random.choice(previous_choice),
            random.choice(sugar_request),
            random.choice(milk_choice),
            random.choice(coffees)
        ]

        writer.writerow(row)
        
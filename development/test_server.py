import requests
import random
import json
import numpy as np


url = "http://127.0.0.1:5000/predict"


def get_message_for_index(index):
    if index == 0:
        return "Normal heartbeat"
    if index == 1:
        return "Supraventricular premature beat"
    if index == 2:
        return "Premature ventricular contraction"
    if index == 3:
        return "Fusion of ventricular and normal beat"
    if index == 4:
        return "Unclassifiable beat"


def get_index_for_message(message):
    if message == "Normal heartbeat":
        return 0
    if message == "Supraventricular premature beat":
        return 1
    if message == "Premature ventricular contraction":
        return 2
    if message == "Fusion of ventricular and normal beat":
        return 3
    if message == "Unclassifiable beat":
        return 4
    else:
        return 5


with open(r".\input\mitbih_test.csv") as file:
    all = file.readlines()

# print(all[0].split(","))


def get_rand_line():
    rand = int(random.random() * len(all))
    line = all[rand].replace("\n", "").split(",")
    numbers = [float(number) for number in line]
    return numbers[: -1], int(numbers[-1])


def make_request():
    line, expected = get_rand_line()
    data = {"ecg_data": line}
    r = requests.post(url,
                      json=data)
    # print(r.status_code)
    print("Prediction:", r.json()["prediction"],
          "\tExpected:", get_message_for_index(expected))
    return get_index_for_message(r.json()["prediction"]), expected


if __name__ == "__main__":
    matrix = np.zeros((6, 6))
    epochs = 20
    for i in range(0, epochs):
        result, expected = make_request()
        matrix[result, expected] += 1
    print(matrix)
    print("Accuracy:", np.diag(matrix).sum()/epochs)

import requests
import random
import json
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


with open(r".\input\mitbih_test.csv") as file:
    all = file.readlines()

# print(all[0].split(","))


def get_rand_line():
    rand = int(random.random() * len(all))
    line = all[rand].replace("\n", "").split(",")
    numbers = [float(number) for number in line]
    return numbers[: -1], numbers[-1]


def make_request():
    line, expected = get_rand_line()
    data = {"ecg_data": line}
    r = requests.post(url,
                      json=data)
    print(r.status_code)
    print(r.json(), "\tExpected is", get_message_for_index(expected))


def print_rand_line():
    l = get_rand_line()
    for i in l:
        print(i)
    print("lenght is", len(l))


if __name__ == "__main__":
    make_request()


def print_rand_line():
    l = get_rand_line()
    for i in l:
        print(i)
    print("lenght is", len(l))


if __name__ == "__main__":
    make_request()

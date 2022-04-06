import requests
import random
import json

r = requests.post('https://httpbin.org/post', data={'key': 'value'})
with open(r".\input\mitbih_test.csv") as file:
    all = file.readlines()

# print(all[0].split(","))


def get_rand_line():
    rand = int(random.random() * len(all))
    line = all[rand].replace("\n", "").split(",")
    numbers = [float(number) for number in line]
    return numbers[: -1]


def make_request():
    data = {"ecg_data": get_rand_line()}
    r = requests.post('http://127.0.0.1:5000/predict',
                      json=data)
    print(r.status_code)
    print(r.json())


def print_rand_line():
    l = get_rand_line()
    for i in l:
        print(i)
    print("lenght is", len(l))


if __name__ == "__main__":
    make_request()

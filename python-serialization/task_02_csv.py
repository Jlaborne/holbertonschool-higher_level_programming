#!/usr/bin/python3
""""""
import json
import csv


def convert_csv_to_json(filename):
    """"""
    try:
        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            data_list = list(reader)

        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file)

        return True

    except FileNotFoundError:
        return False

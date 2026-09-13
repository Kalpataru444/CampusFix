import csv
import os

FILE_NAME = "complaints.csv"


def get_complaints():

    if not os.path.exists(FILE_NAME):
        return []

    complaints = []

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            complaints.append(row)

    # Sort by score: highest first
    complaints.sort(
        key=lambda complaint: int(complaint["Score"]),
        reverse=True
    )

    return complaints
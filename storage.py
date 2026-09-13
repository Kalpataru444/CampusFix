import csv
import os

FILE_NAME = "complaints.csv"


def save_complaint(
    location,
    category,
    severity,
    safety_risk,
    students_affected,
    description,
    score,
    priority
):
    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)

        # Add headers only for a new file
        if not file_exists:
            writer.writerow([
                "Location",
                "Category",
                "Severity",
                "Safety Risk",
                "Students Affected",
                "Description",
                "Score",
                "Priority"
            ])

        # Add the complaint
        writer.writerow([
            location,
            category,
            severity,
            safety_risk,
            students_affected,
            description,
            score,
            priority
        ])


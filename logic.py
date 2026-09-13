def calculate_priority(severity, safety_risk, students_affected):

    # Severity score
    if severity == "Low":
        severity_score = 1

    elif severity == "Medium":
        severity_score = 2

    elif severity == "High":
        severity_score = 3

    # Safety risk score
    if safety_risk == "Yes":
        safety_score = 3

    elif safety_risk == "No":
        safety_score = 0

    # Students affected score
    if students_affected <= 10:
        impact_score = 1

    elif students_affected <= 50:
        impact_score = 2

    else:
        impact_score = 3

    # Combine all scores
    total_score = severity_score + safety_score + impact_score

    # Decide priority level

    if safety_risk == "Yes":
     priority = "High"

    elif total_score <= 3:
     priority = "Low"

    elif total_score <= 6:
     priority = "Medium"

    else:
     priority = "High"

    return total_score, priority



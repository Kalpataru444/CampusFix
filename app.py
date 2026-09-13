import streamlit as st

from logic import calculate_priority
from storage import save_complaint
from dashboard import get_complaints


st.title("🏫 CampusFix")
st.subheader("Smart Campus Issue Reporting System")


location = st.selectbox(
    "Location",
    [
        "Academic Building",
        "Classroom",
        "Library",
        "Hostel",
        "Canteen",
        "Washroom",
        "Other"
    ]
)


category = st.selectbox(
    "Issue Category",
    [
        "Electrical",
        "Water/Plumbing",
        "Infrastructure",
        "Furniture",
        "Cleanliness",
        "Wi-Fi/Internet",
        "Other"
    ]
)


severity = st.radio(
    "Severity",
    ["Low", "Medium", "High"]
)


safety_risk = st.radio(
    "Safety Risk",
    ["Yes", "No"]
)


students_affected = st.number_input(
    "Number of Students Affected",
    min_value=1,
    step=1
)


description = st.text_area(
    "Description",
    placeholder="Describe the issue..."
)


if st.button("Submit Issue"):

    # Calculate priority using logic.py
    score, priority = calculate_priority(
        severity,
        safety_risk,
        students_affected
    )

    # Save complaint using storage.py
    save_complaint(
        location,
        category,
        severity,
        safety_risk,
        students_affected,
        description,
        score,
        priority
    )

    # Show success message
    st.success("Issue submitted successfully! 🎉")

    # Show submitted information
    st.write("### Submitted Information")

    st.write("Location:", location)
    st.write("Issue Category:", category)
    st.write("Severity:", severity)
    st.write("Safety Risk:", safety_risk)
    st.write("Students Affected:", students_affected)
    st.write("Description:", description)

    # Show calculated result
    st.write("### Priority Analysis 🧠")
    st.write("Priority Score:", score)
    st.write("Priority Level:", priority)



    st.divider()

st.header("📋 Admin Dashboard")

complaints = get_complaints()

if complaints:

    st.write("### All Reported Issues")

    for complaint in complaints:

        priority = complaint["Priority"]

        if priority == "High":
            st.error(
                f"🔴 HIGH PRIORITY — {complaint['Category']}"
            )

        elif priority == "Medium":
            st.warning(
                f"🟡 MEDIUM PRIORITY — {complaint['Category']}"
            )

        else:
            st.success(
                f"🟢 LOW PRIORITY — {complaint['Category']}"
            )

        st.write("📍 Location:", complaint["Location"])
        st.write(
            "👥 Students Affected:",
            complaint["Students Affected"]
        )
        st.write("📝 Description:", complaint["Description"])
        st.write("📊 Priority Score:", complaint["Score"])

        st.divider()

else:
    st.info("No complaints submitted yet.")
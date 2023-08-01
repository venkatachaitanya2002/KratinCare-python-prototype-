import random

HEALTH_CONDITIONS = {
    "diabetes": "Follow a balanced diet and monitor blood sugar levels regularly.",
    "hypertension": "Continue taking blood pressure medications as prescribed.",
    "thyroid_disorder": "Take thyroid medication as advised by the doctor."
}

def generate_health_data():
    heart_rate = int(input("Please enter your heart rate (beats per minute): "))
    systolic_pressure = int(input("Please enter your systolic blood pressure: "))
    diastolic_pressure = int(input("Please enter your diastolic blood pressure: "))
    sleep_duration = int(input("Please enter your sleep duration (in minutes): "))

    return heart_rate, (systolic_pressure, diastolic_pressure), sleep_duration

def analyze_health_data(heart_rate, blood_pressure, sleep_duration):
    return "Normal"

def get_medical_history():
    medical_history = {}
    medical_conditions = ["diabetes", "hypertension", "thyroid_disorder"]

    print("Please answer 'yes' or 'no'")
    for condition in medical_conditions:
        answer = input(f"Do you have {condition.replace('_', ' ')}? ").lower()
        medical_history[condition] = (answer == "yes")

    return medical_history

def provide_health_recommendations(health_status, medical_history):
    recommendations = []

    if health_status == "Normal":
        for condition, has_condition in medical_history.items():
            if has_condition and condition in HEALTH_CONDITIONS:
                recommendations.append(HEALTH_CONDITIONS[condition])

        recommendations.append("Engage in regular physical activities and stay socially active.")

    return recommendations

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def water_intake_recommendation(weight_kg):
    water_intake = weight_kg * 30
    return water_intake

def add_medication_reminders():
    reminders = {}
    add_reminder = input("Do you want to add a medical reminder? (yes/no): ").lower()
    while add_reminder == "yes":
        date = input("Please enter the date for the reminder (YYYY-MM-DD): ")
        time = input("Please enter the time for the reminder (HH:MM): ")
        reminder_text = input("Please enter the reminder text: ")
        dosage = input("Please enter the dosage instructions: ")
        reminders[date + " " + time] = (reminder_text, dosage)
        add_reminder = input("Do you want to add another medical reminder? (yes/no): ").lower()

    return reminders

def create_user_profile():
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))
    gender = input("Please enter your gender (male/female/other): ")

    profile = {
        "name": name,
        "age": age,
        "gender": gender
    }
    return profile

def OUTPUT():
    print("Welcome to KratinCare+")

    user_profile = create_user_profile()

    weight_kg = float(input("Please enter your weight in kilograms: "))
    height_cm = float(input("Please enter your height in centimeters: "))
    heart_rate, blood_pressure, sleep_duration = generate_health_data()

    bmi = calculate_bmi(weight_kg, height_cm)

    health_status = analyze_health_data(heart_rate, blood_pressure, sleep_duration)

    medical_history = get_medical_history()

    recommendations = provide_health_recommendations(health_status, medical_history)

    print(f"\nHello {user_profile['name']}!")
    print(f"Your health status: {health_status}")
    print("Health Recommendations:")
    for recommendation in recommendations:
        print("- " + recommendation)

    water_intake = water_intake_recommendation(weight_kg)
    print(f"\nRecommended daily water intake: {water_intake} ml")

    reminders = add_medication_reminders()

    if reminders:
        print("\nMedical Reminders:")
        for datetime, (reminder_text, dosage) in reminders.items():
            print(f"{datetime}: {reminder_text} (Dosage: {dosage})")


OUTPUT()

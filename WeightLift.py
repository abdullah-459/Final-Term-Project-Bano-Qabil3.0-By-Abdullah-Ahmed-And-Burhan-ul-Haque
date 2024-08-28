def suggest_reps(weight):
    # Validate weight input
    if weight < 30 or weight > 130:
        return "Weight should be between 30 and 130 kg."
    
    # Suggest sets and reps based on weight
    if weight <= 50:
        sets = 5
        reps = 12
    elif weight <= 80:
        sets = 8
        reps = 10
    elif weight <= 110:
        sets = 10
        reps = 8
    else:
        sets = 12
        reps = 6
    
    return sets, reps

def workout_precautions():
    precautions = [
        "Always warm up before starting your workout to avoid injuries.",
        "Start with lighter weights to get comfortable with the exercises.",
        "Maintain proper form and posture while lifting weights.",
        "Do not overexert yourself; listen to your body and take breaks when needed.",
        "Gradually increase the weight as your strength improves.",
        "Make sure the area around you is clear of any obstacles before starting.",
        "Keep a firm grip on the dumbbells and avoid sudden jerky movements.",
    ]
    return precautions

# User input
try:
    user_weight = float(input("Enter your weight (in kg): "))

    # Get suggested sets and reps
    result = suggest_reps(user_weight)
    
    if isinstance(result, str):
        print(result)
    else:
        sets, reps = result
        print(f"Suggested workout plan:\nSets: {sets}\nReps: {reps} per set")

    # Display workout precautions
    print("\nPrecautions:")
    for precaution in workout_precautions():
        print(f"- {precaution}")

except ValueError:
    print("Please enter a valid number for weight.")


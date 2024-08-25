# Class for Exercise Goals and Diet Checker
class HealthApp:
    def __init__(self):
        # Initialize empty dictionaries to store exercise goals and diet plans
        self.exercise_goals = {}
        self.diet_plan = {}

    # Function to set exercise goals
    def set_exercise_goals(self):
        num_goals = int(input("How many exercise goals would you like to set? "))
        for i in range(num_goals):
            exercise = input(f"Enter the name of exercise {i + 1}: ")
            reps = int(input(f"Enter the number of repetitions for {exercise}: "))
            self.exercise_goals[exercise] = reps
        print("Your exercise goals have been set!")

    # Function to display exercise goals
    def display_exercise_goals(self):
        if not self.exercise_goals:
            print("No exercise goals set.")
        else:
            print("Your exercise goals:")
            for exercise, reps in self.exercise_goals.items():
                print(f"- {exercise}: {reps} reps")

    # Function to set diet plan
    def set_diet_plan(self):
        num_items = int(input("How many items do you want to include in your diet plan? "))
        for i in range(num_items):
            item = input(f"Enter the name of food item {i + 1}: ")
            calories = int(input(f"Enter the number of calories for {item}: "))
            self.diet_plan[item] = calories
        print("Your diet plan has been set!")

    # Function to check diet
    def check_diet(self):
        daily_calorie_limit = int(input("Enter your daily calorie limit: "))
        total_calories = sum(self.diet_plan.values())

        print("Your diet plan includes the following items:")
        for item, calories in self.diet_plan.items():
            print(f"- {item}: {calories} calories")

        if total_calories <= daily_calorie_limit:
            print(f"Good job! Your diet is within the limit of {daily_calorie_limit} calories.")
        else:
            print(f"Warning! Your diet exceeds the limit by {total_calories - daily_calorie_limit} calories.")

    # Function to display the diet plan
    def display_diet_plan(self):
        if not self.diet_plan:
            print("No diet plan set.")
        else:
            print("Your diet plan:")
            for item, calories in self.diet_plan.items():
                print(f"- {item}: {calories} calories")


# Main program
def main():
    # Create an instance of HealthApp
    app = HealthApp()

    while True:
        print("\nHealth App Menu:")
        print("1. Set Exercise Goals")
        print("2. Display Exercise Goals")
        print("3. Set Diet Plan")
        print("4. Check Diet")
        print("5. Display Diet Plan")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            app.set_exercise_goals()
        elif choice == "2":
            app.display_exercise_goals()
        elif choice == "3":
            app.set_diet_plan()
        elif choice == "4":
            app.check_diet()
        elif choice == "5":
            app.display_diet_plan()
        elif choice == "6":
            print("Exiting the Health App. Stay healthy!")
            break
        else:
            print("Invalid choice, please choose again.")

# Run the main program
if __name__ == "__main__":
    main()

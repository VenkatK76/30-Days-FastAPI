### Variables and Data Types ###
# Habit attributes
habit_name = "Drink Water"      # string
habit_frequency = 3             # integer (times per week)
habit_completed = False         # boolean
habit_notes = ["Morning", "Evening"]  # list
habits = {"name": "Drink Water", "completed": True} # Dictionary

### Operators and Expressions ###
habit_frequency = 3
habit_frequency += 1       # increment frequency
habit_completed = not habit_completed  # toggle True/False

# Check conditions
if habit_frequency > 5:
    print("High-frequency habit")

### Functions – Encapsulating Behavior ###

def mark_habit_completed(habit: dict):
    habit["completed"] = True
    return habit

def add_notes(habit, note):
    habit["notes"].append(note)
    return habit

# Usage
habit = {"name": "Drink Water", "completed": False, "notes": []}
habit = mark_habit_completed(habit)
habit = add_notes(habit, "Morning Session")
habit = add_notes(habit, "After noon Session")

# print(habit)

### Classes & Objects – Modeling Real Things ###

class Habit:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.completed = False
        self.notes = []
    
    def mark_habit_completed(self):
        self.completed = True

    def add_notes(self, note):
        self.notes.append(note)

habit_1 = Habit("Read Book", 1)
habit_1.mark_habit_completed()
habit_1.add_notes("Discipline")

habit_2 = Habit("Running", 1)
habit_2.mark_habit_completed()
habit_2.add_notes("Exercise")

print(habit_1.__dict__)       
print(habit_2.__dict__)

### Lists & Storing Multiple Objects ###

habits = [habit_1, habit_2]
for h in habits:
    print(h.name, '', h.completed)







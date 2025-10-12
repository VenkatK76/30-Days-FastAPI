# Day - 2

from fastapi import FastAPI, HTTPException
from typing import Optional

# Create the FastAPI instance
app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {"app": "Habit Tracker", "developer": "Venkat", "version": "1.0"}

# Day - 3

habits = [
    {"id": 1, "name": "Drink Water", "frequency": 3, "completed": True, "notes": []},
    {"id": 2, "name": "Read Book", "frequency": 1, "completed": False, "notes": []},
    {"id": 3, "name": "Exercise", "frequency": 5, "completed": False, "notes": []},

]

@app.get("/habits/{habit_id}")
def get_habit(habit_id: int):
    for habit in habits:
        if habit["id"] == habit_id:
            return {"data": habit}
    raise HTTPException(status_code=404, detail="Habit not found")

@app.post("/habits/{habit_id}/complete")
def mark_completed(habit_id: int):
    for habit in habits:
        if habit["id"] == habit_id:
            habit["completed"] = True
            return {"message": f"{habit_id} is completed.", "habit": habit}
    raise HTTPException(status_code=404, detail="Habit not found.")

@app.post("/habits/{habit_id}/notes")
def add_notes(habit_id: int, note: str):
    for habit in habits:
        if habit["id"] == habit_id:
            habit["notes"].append(note)
            return {"message": f"{note} is added to {habit_id}.", "habit": habit}
    raise HTTPException(status_code=404, detail="Habit not found.")



# Day - 4

@app.get("/habits")
def get_all_habits(
    completed: Optional[bool] = None,
    min_frequency: Optional[int] = None,
    max_frequency: Optional[int] = None
):
    filtered = habits
    
    if completed is not None:
        filtered = [h for h in filtered if h["completed"] == completed]  

    if min_frequency is not None :
        filtered = [h for h in filtered if h["frequency"] >= min_frequency]

    if max_frequency is not None:
        filtered = [h for h in filtered if h["frequency"] <= max_frequency]

    return { "count": len(filtered), "habits": filtered}
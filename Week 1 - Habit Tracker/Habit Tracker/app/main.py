# Day - 2

from fastapi import FastAPI, HTTPException, status
from typing import Optional, List
from pydantic import BaseModel

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

# Day - 5

class Habit(BaseModel):
    name: str
    frequency: int
    completed: bool = False
    notes: list[str] = []

class HabitResponse(BaseModel):
    message: str
    habit: Habit

@app.post("/habits", response_model=HabitResponse)
def create_habit(habit: Habit):
    new_habit = habit.dict()
    new_habit["id"] = len(habits) + 1
    habits.append(new_habit)
    return {"message": "Habit added successfully!", "habit": new_habit}


# Day - 6

class HabitUpdate(BaseModel):
    name: Optional[str] = None
    frequency: Optional[int] = None
    completed: Optional[bool] = None
    notes: Optional[list[str]] = None


@app.patch("/habits/{habit_id}", response_model=HabitResponse)
def update_habit(habit_id: int, habit_update: HabitUpdate):
    for habit in habits:
        if habit["id"] == habit_id:
            update_data = habit_update.dict(exclude_unset=True)
            habit.update(update_data)
            return {"message": "Habit Updated Successfully", "habit": habit}
    raise HTTPException(status_code=404, detail="Habit not found")

@app.put("/habits/{habit_id}", response_model= HabitResponse)
def replace_habit(habit_id: int, updated_habit: Habit):
    for index, habit in enumerate(habits):
        if habit["id"] == habit_id:
            updated_habit_dict = updated_habit.dict().copy()
            updated_habit_dict["id"] = habit_id
            habits[index] = updated_habit_dict
            return {"message": "Habit replaced Successfully", "habit": updated_habit_dict} 
    raise HTTPException(status_code=404, detail="Habit not found")
       

# Day - 7

@app.delete("/habits/{habit_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_habit(habit_id: int):
    for index, habit in enumerate(habits):
        if habit["id"] == habit_id:
            habits.pop(index)
            return
    return HTTPException(status_code=404, detail="Habit not found")
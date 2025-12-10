# backend/app/routers/ai_controller.py

from typing import List, Literal, Optional
from fastapi import APIRouter
from pydantic import BaseModel

from app.services.gemini_ai import (
    generate_weekly_plan,
    generate_meal_plan,
    generate_workout_plan,
)

router = APIRouter(tags=["fitness-ai"])

# ========== MODELS ==========

FitnessGoal = Literal["Lose Fat", "Gain Muscle", "Maintenance"]
FoodPreference = Literal["South Indian", "North Indian", "Mixed", "Other"]


class UserProfile(BaseModel):
    name: str
    age: Optional[int] = None
    gender: Optional[str] = None
    fitness_goal: FitnessGoal
    height_cm: float
    weight_kg: float
    equipment: List[str]
    food_preference: FoodPreference
    # OPTIONAL preferences from frontend (added for safety)
    weekly_preferences: Optional[dict] = None
    meal_preferences: Optional[dict] = None
    workout_preferences: Optional[dict] = None


# Save profile (optional)
@router.post("/profile")
def save_profile(profile: UserProfile):
    return {
        "message": "Profile received",
        "profile": profile.dict(),  # convert to dict for consistency
    }


# ========== WEEKLY PLAN ==========
@router.post("/weekly-plan")
def weekly_plan(profile: UserProfile):
    # Convert Pydantic → dict (IMPORTANT!)
    return generate_weekly_plan(profile.dict())


# ========== MEAL PLAN ==========
@router.post("/meal-plan")
def meal_plan(profile: UserProfile):
    # Convert Pydantic → dict
    return generate_meal_plan(profile.dict())


# ========== WORKOUT PLAN ==========
@router.post("/workout-plan")
def workout_plan(profile: UserProfile):
    # Convert Pydantic → dict
    return generate_workout_plan(profile.dict())

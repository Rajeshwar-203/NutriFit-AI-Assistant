import json
import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

# ============================================================
# WEEKLY PLAN
# ============================================================
def generate_weekly_plan(profile: dict):
    weekly_prefs = profile.get("weekly_preferences", {})
    base_profile = {
        "name": profile.get("name"),
        "fitness_goal": profile.get("fitness_goal"),
        "height_cm": profile.get("height_cm"),
        "weight_kg": profile.get("weight_kg"),
        "equipment": profile.get("equipment"),
        "food_preference": profile.get("food_preference"),
    }

    prompt = f"""
You are a professional fitness coach & dietitian.

USER BASE PROFILE:
{json.dumps(base_profile, indent=2)}

WEEKLY PLAN EXTRA PREFERENCES:
{json.dumps(weekly_prefs, indent=2)}

Generate a 7-day fitness plan (Monday–Sunday).

STRICT RULES:
- Respond ONLY in VALID JSON
- Structure:
{{
  "user_name": "{base_profile.get('name')}",
  "goal": "{weekly_prefs.get('weekly_goal') or base_profile.get('fitness_goal')}",
  "days": [
    {{
      "day": "Monday",
      "title": "string",
      "workout": "string",
      "protein_g": 0,
      "carbs_g": 0,
      "fats_g": 0,
      "breakfast": "string",
      "lunch": "string",
      "dinner": "string"
    }}
  ]
}}
- Use activity_level & health_issues to adjust the difficulty.
- If feedback is present, adjust compared to the previous week's plan.
    """

    r = model.generate_content(prompt)
    text = r.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)


# ============================================================
# MEAL PLAN
# ============================================================
def generate_meal_plan(profile: dict):
    meal_prefs = profile.get("meal_preferences", {})
    base_profile = {
        "name": profile.get("name"),
        "fitness_goal": profile.get("fitness_goal"),
        "food_preference": profile.get("food_preference"),
    }

    prompt = f"""
You are a certified nutritionist.

USER BASE PROFILE:
{json.dumps(base_profile, indent=2)}

MEAL PLAN EXTRA PREFERENCES:
{json.dumps(meal_prefs, indent=2)}

Create a daily AI meal plan.

STRICT JSON RESPONSE:
{{
  "calories": 2000,
  "protein_g": 120,
  "carbs_g": 200,
  "fats_g": 60,
  "breakfast": "string",
  "lunch": "string",
  "dinner": "string",
  "snacks": "string"
}}

RULES:
- Use diet_type (Veg, Non-veg, Vegan).
- Avoid all allergies/dislikes.
- Match target_calories & target_protein_g.
- If feedback is added, improve upon the previous plan.
"""

    r = model.generate_content(prompt)
    text = r.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)


# ============================================================
# WORKOUT PLAN
# ============================================================
def generate_workout_plan(profile: dict):
    workout_prefs = profile.get("workout_preferences", {})
    base_profile = {
        "name": profile.get("name"),
        "fitness_goal": profile.get("fitness_goal"),
        "equipment": profile.get("equipment"),
    }

    prompt = f"""
You are a certified strength coach & physiotherapist.

USER BASE PROFILE:
{json.dumps(base_profile, indent=2)}

WORKOUT EXTRA PREFERENCES:
{json.dumps(workout_prefs, indent=2)}

Create a structured workout plan with:
- warmup (list)
- main_workout (list)
- cooldown (list)

STRICT JSON FORMAT:
{{
  "warmup": [
    {{
      "name": "string",
      "duration": "30 sec",
      "equipment": "None",
      "notes": "string"
    }}
  ],
  "main_workout": [
    {{
      "name": "string",
      "duration": "45 sec",
      "equipment": "Dumbbells",
      "notes": "string"
    }}
  ],
  "cooldown": [
    {{
      "name": "string",
      "duration": "30 sec",
      "notes": "string"
    }}
  ]
}}

RULES:
- Use intensity + level (Beginner/Intermediate/Advanced).
- Body focus required.
- Avoid movements that worsen health pains.
- Fit within time_minutes duration.
- If feedback exists, improve the workout plan carefully.
"""

    r = model.generate_content(prompt)
    text = r.text.strip().replace("```json", "").replace("```", "")
    return json.loads(text)

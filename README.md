Overview

The AI-Based Personalized Fitness & Nutrition Planner is a full-stack web application that generates:

🗓️ Weekly Fitness Plans (Mon–Sun)

🍽️ Daily Meal Plans

💪 Workout Plans

All outputs are AI-driven, personalized, and regenerable with feedback.

This system uses:

React.js → UI & User Input

FastAPI → Backend API

Gemini 2.5 Flash Model → AI reasoning & JSON generation

Neon Glass UI → Modern, aesthetic UI design

It enables users to input their personal preferences such as goals, diet preferences, workouts, calories, allergies, health conditions, etc.
The system then generates structured JSON output for each plan and displays them with clean UI layouts.

🚀 Features
✅ 1. Weekly Plan Generator

Creates a 7-day fitness plan (Mon–Sun)

Includes:

Workout title

Macros (Protein/Carbs/Fats)

Meals (Breakfast/Lunch/Dinner)

Supports Regenerate using Feedback

Plans adapt to:

Activity level

Health issues

User goals

✅ 2. Meal Plan Generator

Generates:

Breakfast

Lunch

Dinner

Snacks

Personalized by:

Target calories

Protein target

Diet type (Veg/Non-Veg/Vegan)

Allergies & disliked items

Regenerate based on feedback (e.g., low carbs, avoid rice, etc.)

✅ 3. Workout Plan Generator

Generates:

Warm-up

Main workout

Cooldown

Exercises shown in rectangular card boxes

Includes:

Equipment

Duration

Notes

Body focus

Regenerate with feedback (e.g., avoid knee pain, more core workout)

✅ 4. Dashboard

Glass UI 3-card Navigation:

Weekly Plan → open

Meal Plan → open

Workout Plan → open

PC-friendly layout

Clean boxed UI

✅ 5. Tech Stack
Layer	Technology
Frontend	React.js, Axios, Neon Glass UI, Custom CSS
Backend	FastAPI (Python)
AI	Gemini 2.5 Flash Model
Data Format	JSON (AI enforced)

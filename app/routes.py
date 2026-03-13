from fastapi import APIRouter # type: ignore
from app.adaptive_engine import get_next_question, update_ability
from app.ai_service import generate_study_plan

router = APIRouter()

ability = 0.5


@router.get("/next-question")
def next_question():
    global ability

    question = get_next_question(ability)

    return {
        "current_ability": ability,
        "question": question
    }


@router.post("/submit-answer")
def submit_answer(is_correct: bool):
    global ability

    ability = update_ability(ability, is_correct)

    return {
        "new_ability": ability
    }


# AI Study Plan Endpoint
@router.get("/study-plan")
def study_plan():

    weak_topics = ["Algebra", "Vocabulary"]
    max_difficulty = ability

    plan = generate_study_plan(weak_topics, max_difficulty)

    return {
        "study_plan": plan
    }
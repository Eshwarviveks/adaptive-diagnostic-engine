from app.database import questions_collection


def get_next_question(ability):

    question = questions_collection.find_one(
        {"difficulty": {"$gte": ability}},
        {"_id": 0}
    )

    # remove correct answer before sending to user
    if question and "correct_answer" in question:
        question.pop("correct_answer")

    return question


def update_ability(current_ability, is_correct):

    step = 0.1

    if is_correct:
        new_ability = current_ability + step
    else:
        new_ability = current_ability - step

    # keep ability within range
    new_ability = max(0.1, min(1.0, new_ability))

    return round(new_ability, 2)
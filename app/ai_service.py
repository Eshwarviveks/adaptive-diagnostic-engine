import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_study_plan(weak_topics, max_difficulty):

    prompt = f"""
    A student completed an adaptive test.

    Weak topics: {weak_topics}
    Highest difficulty reached: {max_difficulty}

    Create a simple 3 step study plan to improve their performance.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an educational tutor."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
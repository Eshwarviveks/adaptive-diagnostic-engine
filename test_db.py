from app.database import questions_collection

questions_collection.insert_one({
    "question": "Test question",
    "difficulty": 0.5
})

print("Data inserted successfully!")
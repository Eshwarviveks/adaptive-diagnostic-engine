from app.database import questions_collection

questions = [

# Easy (0.1–0.3)
{
"question": "What is 5 + 7?",
"options": ["10","11","12","13"],
"correct_answer": "12",
"difficulty": 0.1,
"topic": "Algebra",
"tags": ["addition"]
},
{
"question": "What is 9 × 6?",
"options": ["54","45","63","48"],
"correct_answer": "54",
"difficulty": 0.2,
"topic": "Algebra",
"tags": ["multiplication"]
},
{
"question": "Square root of 144?",
"options": ["10","11","12","13"],
"correct_answer": "12",
"difficulty": 0.3,
"topic": "Algebra",
"tags": ["square-root"]
},

# Medium (0.4–0.6)
{
"question": "Solve: 2x + 6 = 14",
"options": ["3","4","5","6"],
"correct_answer": "4",
"difficulty": 0.4,
"topic": "Algebra",
"tags": ["equation"]
},
{
"question": "Synonym of 'Abundant'",
"options": ["Rare","Plentiful","Weak","Tiny"],
"correct_answer": "Plentiful",
"difficulty": 0.5,
"topic": "Vocabulary",
"tags": ["synonym"]
},
{
"question": "What is 15% of 200?",
"options": ["20","25","30","35"],
"correct_answer": "30",
"difficulty": 0.6,
"topic": "Arithmetic",
"tags": ["percentage"]
},

# Hard (0.7–1.0)
{
"question": "If x² = 49, x = ?",
"options": ["7","-7","±7","0"],
"correct_answer": "±7",
"difficulty": 0.7,
"topic": "Algebra",
"tags": ["quadratic"]
},
{
"question": "Antonym of 'Benevolent'",
"options": ["Kind","Cruel","Helpful","Friendly"],
"correct_answer": "Cruel",
"difficulty": 0.8,
"topic": "Vocabulary",
"tags": ["antonym"]
},
{
"question": "What is derivative of x²?",
"options": ["x","2x","x²","2"],
"correct_answer": "2x",
"difficulty": 0.9,
"topic": "Calculus",
"tags": ["derivative"]
},
{
"question": "Limit of sin(x)/x as x→0?",
"options": ["0","1","∞","-1"],
"correct_answer": "1",
"difficulty": 1.0,
"topic": "Calculus",
"tags": ["limits"]
}

]

questions_collection.insert_many(questions)

print("Questions inserted successfully!")
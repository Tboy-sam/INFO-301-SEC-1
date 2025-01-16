import random

def quiz_game():
    # List of questions, each represented as a dictionary
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
            "answer": "C",
        },
        {
            "question": "What is the capital city of Liberia?",
            "choices": {"A": "Guinea", "B": "Monrovia", "C": "Buchanan", "D": "Barclayville"},
            "answer": "B",
        },
        {
            "question": "Who Kill Golliah?",
            "choices": {"A": "David", "B": "Samuel", "C": "Uriah", "D": "Sampson"},
            "answer": "A",
        },
        {
            "question": "How Many Men Wrote the Bible?",
            "choices": {"A": "10", "B": "100", "C": "50", "D": "40"},
            "answer": "D",
        },
        {
            "question": "Who is the current president of Liberia?",
            "choices": {"A": "Joseph Boakai", "B": "George Weah", "C": "Barrack Obama", "D": "Joe Baiden"},
            "answer": "A",
        },
        {
            "question": "What is the capital city of Bong?",
            "choices": {"A": "Ganta", "B": "Buchanan", "C": "Gbarnga", "D": "Greenville"},
            "answer": "C",
        },
        {
            "question": "Which country is known as the world super power?",
            "choices": {"A": "China", "B": "South Korea", "C": "Thailand", "D": "America"},
            "answer": "D",
        },
        {
            "question": "Who painted the Mona Lisa?",
            "choices": {"A": "Leonardo da Vinci", "B": "Vincent van Gogh", "C": "Pablo Picasso", "D": "Claude Monet"},
            "answer": "A",
        },
        {
            "question": "What is the smallest prime number?",
            "choices": {"A": "0", "B": "1", "C": "2", "D": "3"},
            "answer": "C",
        },
        {
            "question": "Which gas do plants primarily use for photosynthesis?",
            "choices": {"A": "Oxygen", "B": "Carbon Dioxide", "C": "Nitrogen", "D": "Hydrogen"},
            "answer": "B",
        },
    ]

    score = 0
    random.shuffle(questions)  # Shuffle questions for randomness

    print("Welcome to the Quiz Game!\n")
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for key, value in q["choices"].items():
            print(f"  {key}. {value}")
        user_answer = input("Enter the letter of your answer (A, B, C, D): ").upper()

        if user_answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong answer. The correct answer was {q['answer']}.\n")

    print(f"Quiz over! Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    quiz_game()

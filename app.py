import requests
import random

def fetch_questions(amount=5, category=None, difficulty=None):
    """Fetch trivia questions from the Open Trivia API."""
    url = "https://opentdb.com/api.php"
    params = {
        "amount": amount,
        "type": "multiple"
    }
    if category:
        params["category"] = category
    if difficulty:
        params["difficulty"] = difficulty

    response = requests.get(url, params=params)
    data = response.json()
    return data.get("results", [])

def play_game():
    print("Welcome to the Trivia Quiz Game!")
    print("Answer the questions to earn points.\n")

    questions = fetch_questions()
    score = 0

    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question['question']}")
        options = question["incorrect_answers"] + [question["correct_answer"]]
        random.shuffle(options)

        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")

        try:
            answer = int(input("Your answer (Enter the number): "))
            if options[answer - 1] == question["correct_answer"]:
                print("Correct! 🎉\n")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_answer']}\n")
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.\n")

    print(f"Game Over! Your final score is {score}/{len(questions)}")
    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()

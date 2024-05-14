import sys

def kbc_game():
    questions = [
        {
            "question": "Who is the father of Indian Constitution?",
            "options": ["A. Mahatma Gandhi", "B. Jawaharlal Nehru", "C. B.R. Ambedkar", "D. Sarder Patel"],
            "answer": "C"
        },
        {
            "question": "Which is the largest planet in our solar system?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "C"
        },
        {
            "question": "Who wrote the Indian National Anthem?",
            "options": ["A. Rabindranath Tagore", "B. Bankim Chandra Chatterjee", "C. Sarojini Naidu", "D. Aurobindo Ghosh"],
            "answer": "A"
        },
        {
            "question": "Which is the longest river in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Ganges", "D. Yangtze"],
            "answer": "B"
        },
        {
            "question": "Who was the first woman Prime Minister of India?",
            "options": ["A. Indira Gandhi", "B. Pratibha Patil", "C. Sonia Gandhi", "D. Sushma Swaraj"],
            "answer": "A"
        }

    ]

    print("Welcome to Kaund Banega Crorepati\n")
    money = 0
    for i, q in enumerate(questions):
        print(f"Question {i+1}: {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Please enter your answer (A/B/C/D): ").strip().upper()

        if answer == q['answer']:
            money += 1000
            print('Correct. Your current amount is: ', money)
        else:
            print(f"Wrong answer. The correct answer wa {q['answer']}")
            break
        print()
    

    print(f"Game Over. Your final amount is: {money}")


if __name__ == "__main__":
    kbc_game()



       



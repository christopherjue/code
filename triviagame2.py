import random

def play_game():
    print("Welcome to the Elon Musk Trivia Game!")
    print("Answer the questions correctly to test your knowledge about Elon Musk.")

    questions = [
        {
            "question": "In which country was Elon Musk born?",
            "options": ["United States", "Canada", "South Africa"],
            "answer": "South Africa"
        },
        {
            "question": "Which company did Elon Musk found in 2002?",
            "options": ["Tesla Motors", "SpaceX", "SolarCity"],
            "answer": "SpaceX"
        },
        {
            "question": "Which electric vehicle model is produced by Tesla?",
            "options": ["Model S", "Model X", "Model 3", "All of the above"],
            "answer": "All of the above"
        },
        {
            "question": "What is the name of Elon Musk's company that aims to develop high-speed transportation through vacuum tubes?",
            "options": ["Hyperloop Technologies", "Virgin Hyperloop", "The Boring Company"],
            "answer": "The Boring Company"
        },
        {
            "question": "In 2021, Elon Musk became the CEO of which space exploration company?",
            "options": ["NASA", "Virgin Galactic", "Blue Origin"],
            "answer": "Blue Origin"
        },
        {
            "question": "Which entrepreneur served as Elon Musk's inspiration?",
            "options": ["Thomas Edison", "Nikola Tesla", "Henry Ford"],
            "answer": "Nikola Tesla"
        },
        {
            "question": "What is the name of Elon Musk's project to create a global satellite internet constellation?",
            "options": ["Starlink", "Moonshot", "SkyNet"],
            "answer": "Starlink"
        },
        {
            "question": "Which comedian hosted Elon Musk as a guest on Saturday Night Live in 2021?",
            "options": ["Jimmy Fallon", "Trevor Noah", "Dave Chappelle"],
            "answer": "Dave Chappelle"
        },
        {
            "question": "Elon Musk briefly surpassed which tech mogul to become the richest person in the world in 2021?",
            "options": ["Jeff Bezos", "Bill Gates", "Mark Zuckerberg"],
            "answer": "Jeff Bezos"
        },
        {
            "question": "What is the name of Elon Musk's tunnel construction project in Las Vegas?",
            "options": ["Loop", "MuskTunnel", "SubwayX"],
            "answer": "Loop"
        }
    ]

    random.shuffle(questions)
    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        print(q["question"])
        print("Options:")
        for j, option in enumerate(q["options"], start=1):
            print(f"{j}. {option}")

        user_choice = input("Enter your answer (1, 2, 3, 4): ")
        if user_choice == str(q["options"].index(q["answer"]) + 1):
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print("\nGame Over!")
    print(f"You answered {score} out of {len(questions)} questions correctly.")

    if score == len(questions):
        print("Congratulations! You got a perfect score.")

play_game()

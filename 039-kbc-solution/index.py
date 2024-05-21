questions = [
    [
        "How many grams of salt are there in a litre of typical seawater?",
        "1gm", "1000gm", "9999gm", "None", 4
    ],
    [
        "What is the capital of France?", "London", "Paris", "Berlin", "Tokyo",
        2
    ],
    [
        "Which country has the highest population density?", "China", "India",
        "United States", "Brazil", 1
    ],
    [
        "What is the tallest mountain in the world?", "Mount Everest", "K2",
        "Kangchenjunga", "Lhotse", 1
    ],
    [
        "What is the name of the largest ocean on Earth?", "Pacific Ocean",
        "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", 1
    ],
]

levels = [1000, 10000, 100000, 1000000, 10000000]

for index in range(0, len(questions)):
    question = questions[index]
    print(f"Question for Rs. {levels[index]}:")
    print(question[0])
    print(f"1. {question[1]}          2. {question[2]}")
    print(f"3. {question[3]}          4. {question[4]}")
    print("\n")
    answer = int(input("Enter your answer (1-4): "))
    if answer == question[-1]:
        print(f"\nCorrect answer you have won Rs. {levels[index]}\n")
    else:
        print("Wrong answer")
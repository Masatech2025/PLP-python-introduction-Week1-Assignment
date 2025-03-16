import time


def quiz_game ( ):
    questions = [
        { "question": "What is the keyword to define a function in Python?",
          "options": [ "A) func", "B) def", "C) define", "D) function" ], "answer": "B" },
        { "question": "Which movie features a character named 'Jack Sparrow'?",
          "options": [ "A) Titanic", "B) Pirates of the Caribbean", "C) The Jungle Book", "D) Indiana Jones" ],
          "answer": "B" },
        { "question": "What is the capital of France?", "options": [ "A) Madrid", "B) Berlin", "C) Paris", "D) Rome" ],
          "answer": "C" },
        { "question": "Which programming language is known as the 'mother of all languages'?",
          "options": [ "A) Python", "B) C", "C) Assembly", "D) Java" ], "answer": "B" },
        { "question": "Who played Iron Man in the Marvel Cinematic Universe?",
          "options": [ "A) Chris Evans", "B) Robert Downey Jr.", "C) Mark Ruffalo", "D) Chris Hemsworth" ],
          "answer": "B" },
    ]

    score = 0

    print ( "Welcome to the Fun Quiz! 🎉" )
    time.sleep ( 1 )

    for index, q in enumerate ( questions, start = 1 ):
        print ( f"\nQuestion {index}: {q [ 'question' ]}" )
        for option in q [ 'options' ]:
            print ( option )

        answer = input ( "Your answer (A, B, C, or D): " ).strip ( ).upper ( )
        if answer == q [ 'answer' ]:
            print ( "Correct! ✅" )
            score += 1
        else:
            print ( f"Wrong! ❌ The correct answer was {q [ 'answer' ]}" )

        time.sleep ( 1 )

    print ( f"\nYour final score is {score}/{len ( questions )} 🎯" )

    play_again = input ( "Do you want to play again? (yes/no): " ).strip ( ).lower ( )
    if play_again == "yes":
        quiz_game ( )
    else:
        print ( "Thanks for playing! 👋" )


quiz_game ( )
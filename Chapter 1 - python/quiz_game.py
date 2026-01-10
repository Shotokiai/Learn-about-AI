def create_question(question_text, options, correct_answer):
    """Create a question dictionary"""
    return {
        'question': question_text,
        'options': options,
        'correct_answer': correct_answer
    }

def display_question(question, question_number):
    """Display a question with its options"""
    print(f"\nQuestion {question_number}: {question['question']}")
    print()
    
    for i, option in enumerate(question['options'], 1):
        print(f"  {i}. {option}")
    print()

def check_answer(question, user_answer):
    """Check if user's answer is correct"""
    try:
        answer_index = int(user_answer) - 1
        
        if 0 <= answer_index < len(question['options']):
            if answer_index == question['correct_answer']:
                return True, question['options'][answer_index]
            else:
                return False, question['options'][answer_index]
        else:
            return None, "Invalid option"
    except ValueError:
        return None, "Invalid input"

def calculate_score(correct_answers, total_questions):
    """Calculate percentage score"""
    if total_questions == 0:
        return 0
    return (correct_answers / total_questions) * 100

def display_results(correct_answers, total_questions, results):
    """Display quiz results"""
    score = calculate_score(correct_answers, total_questions)
    
    print("\n" + "="*70)
    print(f"{'QUIZ RESULTS':^70}")
    print("="*70)
    print(f"\nCorrect Answers: {correct_answers}/{total_questions}")
    print(f"Score: {score:.1f}%")
    
    if score >= 80:
        print("Grade: A - Excellent! 🌟")
    elif score >= 60:
        print("Grade: B - Good job! 👍")
    elif score >= 40:
        print("Grade: C - You can do better! 📚")
    else:
        print("Grade: D - Keep practicing! 💪")
    
    print("\n" + "-"*70)
    print("Question-by-Question Breakdown:")
    print("-"*70)
    
    for i, result in enumerate(results, 1):
        status = "✓" if result['correct'] else "✗"
        print(f"\nQ{i}: {result['question']}")
        print(f"  {status} Your answer: {result['user_answer']}")
        
        if not result['correct']:
            print(f"  Correct answer: {result['correct_option']}")
    
    print("="*70 + "\n")

# Main program
print("=== QUIZ SYSTEM ===\n")

# Create quiz questions
questions = []

# You can add questions here or let user create them
print("Create your quiz questions")
print("(or type 'start' to use default questions)\n")

user_choice = input("Choice: ").lower().strip()

if user_choice == 'start':
    # Default questions about Python
    questions.append(create_question(
        "What is Python?",
        ["A snake", "A programming language", "A type of coffee", "A mathematical formula"],
        1  # Index of correct answer (0-based)
    ))
    
    questions.append(create_question(
        "Which keyword is used to define a function in Python?",
        ["function", "def", "func", "define"],
        1
    ))
    
    questions.append(create_question(
        "What is the output of: print(2 + 3 * 2)?",
        ["10", "8", "12", "Error"],
        1
    ))
    
    questions.append(create_question(
        "Which data type is mutable in Python?",
        ["tuple", "string", "list", "integer"],
        2
    ))
    
    questions.append(create_question(
        "What does 'len()' function do?",
        ["Deletes items", "Returns length", "Sorts items", "Creates a list"],
        1
    ))

else:
    # Let user create questions
    print("\nEnter questions (type 'done' when finished):\n")
    
    while True:
        question_text = input("Question: ").strip()
        
        if question_text.lower() == 'done':
            break
        
        if not question_text:
            print("  ✗ Question cannot be empty\n")
            continue
        
        print("Enter 4 options:")
        options = []
        
        for i in range(4):
            option = input(f"  Option {i+1}: ").strip()
            if not option:
                print("  ✗ Option cannot be empty")
                break
            options.append(option)
        
        if len(options) != 4:
            print("  ✗ All 4 options are required\n")
            continue
        
        try:
            correct = int(input("Correct option number (1-4): "))
            
            if 1 <= correct <= 4:
                questions.append(create_question(question_text, options, correct - 1))
                print("  ✓ Question added\n")
            else:
                print("  ✗ Invalid option number\n")
        except ValueError:
            print("  ✗ Please enter a valid number\n")

# Start the quiz
if not questions:
    print("No questions available. Goodbye!")
else:
    print("\n" + "="*70)
    print(f"{'QUIZ START':^70}")
    print("="*70)
    print(f"\nTotal Questions: {len(questions)}")
    print("Enter the option number (1-4) for each question")
    
    input("\nPress Enter to begin...")
    
    correct_answers = 0
    results = []
    
    for i, question in enumerate(questions, 1):
        display_question(question, i)
        
        user_answer = input("Your answer: ").strip()
        
        is_correct, answer_text = check_answer(question, user_answer)
        
        if is_correct is None:
            print(f"  ✗ {answer_text}. Marking as incorrect.")
            is_correct = False
            answer_text = "Invalid"
        elif is_correct:
            print("  ✓ Correct!")
            correct_answers += 1
        else:
            print(f"  ✗ Incorrect.")
            correct_option = question['options'][question['correct_answer']]
        
        # Store result
        result = {
            'question': question['question'],
            'user_answer': answer_text,
            'correct': is_correct,
            'correct_option': question['options'][question['correct_answer']]
        }
        results.append(result)
    
    # Display final results
    display_results(correct_answers, len(questions), results)
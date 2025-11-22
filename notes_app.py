import json

# Path to your JSON file
JSON_FILE = "categorized_notes.json"

# Function to load notes from JSON
def load_notes():
    try:
        with open(JSON_FILE, "r") as file:
            notes = json.load(file)
        return notes
    except FileNotFoundError:
        return {}  # Return empty dict if file not found
    except json.JSONDecodeError:
        return {}  # Return empty dict if file is empty or invalid

# Function to save notes to JSON
def save_notes(notes):
    with open(JSON_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_initial_generator_notes():
    notes = load_notes()  # Load existing notes
    
    # Make sure 'Generator' topic exists
    if "Generator" not in notes:
        notes["Generator"] = {}

    # Add Generator questions and answers
    notes["Generator"]["What is a generator?"] = "A generator produces electricity by converting mechanical energy into electrical energy."
    notes["Generator"]["Formula for generator power?"] = "Power (kW) = (Voltage × Current × Power Factor) / 1000"
    notes["Generator"]["Difference between kW and kVA?"] = "kW is real power, kVA is apparent power."
    notes["Generator"]["How to calculate generator current if kW is given?"] = "Current (A) = (kW × 1000) / (Voltage × Power Factor)"
    notes["Generator"]["How to calculate kW if current is available?"] = "kW = (Voltage × Current × Power Factor) / 1000"
    
    save_notes(notes)  # Save notes back to JSON
    print("Initial Generator notes added successfully!")


# Call this only once to add initial notes
# add_initial_generator_notes()

def view_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return

    for category, questions in notes.items():
        print(f"\n--- {category} ---")
        for question, answer in questions.items():
            print(f"Q: {question}")
            print(f"A: {answer}")

def add_note():
    category = input("Enter category: ").strip()
    question = input("Enter question: ").strip()
    answer = input("Enter answer: ").strip()

    if not category or not question or not answer:
        print("All fields are required!")
        return

    notes = load_notes()
    if category not in notes:
        notes[category] = {}
    
    notes[category][question] = answer
    save_notes(notes)
    print("Note added successfully!")

def search_notes():
    keyword = input("Enter keyword to search: ").strip().lower()
    notes = load_notes()
    found = False

    for category, questions in notes.items():
        for question, answer in questions.items():
            if keyword in question.lower() or keyword in answer.lower():
                print(f"\n[{category}]")
                print(f"Q: {question}")
                print(f"A: {answer}")
                found = True
    
    if not found:
        print("No matching notes found.")

def edit_note():
    notes = load_notes()
    category = input("Enter category of the note to edit: ").strip()
    
    if category not in notes:
        print("Category not found.")
        return

    question = input("Enter the exact question to edit: ").strip()
    if question not in notes[category]:
        print("Question not found.")
        return

    new_answer = input(f"Enter new answer (current: {notes[category][question]}): ").strip()
    if new_answer:
        notes[category][question] = new_answer
        save_notes(notes)
        print("Note updated successfully!")

def delete_note():
    notes = load_notes()
    category = input("Enter category of the note to delete: ").strip()
    
    if category not in notes:
        print("Category not found.")
        return

    question = input("Enter the exact question to delete: ").strip()
    if question not in notes[category]:
        print("Question not found.")
        return

    del notes[category][question]
    if not notes[category]:  # Remove empty category
        del notes[category]
        
    save_notes(notes)
    print("Note deleted successfully!")

def main_menu():
    while True:
        print("\n--- Python Notes App ---")
        print("1. View all notes")
        print("2. Add a new note")
        print("3. Search notes")
        print("4. Edit a note")
        print("5. Delete a note")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            edit_note()
        elif choice == "5":
            delete_note()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-6.")



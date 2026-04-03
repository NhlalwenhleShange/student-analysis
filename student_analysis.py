import csv 

students = [] 

# -------- LOAD DATA -------- # 
def load_data():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    "name": row["Name"],
                    "math": int(row["Math"]),
                    "science": int(row["Science"]),
                    "english": int(row["English"]) 
                })
    except FileNotFoundError:
        print("Error: students.csv not found.")

# -------- CALCULATE AVERAGE -------- # 
def calculate_averages():
    for student in students:
        avg = (student["math"] + student["science"] + student["english"]) / 3 
        student["average"] = avg 

# -------- TOP STUDENT -------- # 
def top_student():
    top = max(students, key=lambda x: x["average"])
    print("\n🏆 Top Student:")
    print(f"\n  Top Student: {top['name']} ({top['average']:.2f})") 

# -------- FAILING STUDENTS -------- # 
def failing_students():
    print("\n⚠️ Failing Students (Average < 50):")
    for student in students:
        if student["average"] < 50:
            print(f"{student['name']}: {student['average']:.2f}") 

# -------- DISPLAY ALL -------- #
def display_all():
    print("\n📊 All Students:")
    for student in students:
        print(f"{student['name']}: {student['average']:.2f}") 

# -------- MAIN -------- # 
def main():
    load_data() 
    calculate_averages()
    while True:
        print("\n=== Student Analysis System ===")
        print("1. View All Students")
        print("2. Top Student")
        print("3. Failing Students")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            display_all()
        elif choice == "2":
            top_student()
        elif choice == "3":
            failing_students()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice") 
main()
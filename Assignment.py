import os
import shutil

# פונקציה לרשימת פריטים בתיקייה הנוכחית
def list_items():
    for entry in os.listdir():
        print(entry)

# פונקציה לשינוי תיקייה
def change_dir(directory_name):
    try:
        os.chdir(directory_name)
    except FileNotFoundError:
        print("Directory not found")  # תיקייה לא נמצאה
    except NotADirectoryError:
        print(f"{directory_name} is not a directory")  # זה לא תיקייה

# פונקציה לעליה לתיקיית האב
def go_up_dir():
    os.chdir("..")

# פונקציה ליצירת תיקייה
def create_dir(directory_name):
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        print("Directory already exists")  # התיקייה כבר קיימת

# פונקציה למחיקת תיקייה וכל התוכן שלה
def delete_dir(directory_name):
    try:
        shutil.rmtree(directory_name)
    except FileNotFoundError:
        print("Directory not found")  # תיקייה לא נמצאה

# פונקציה למחיקת קובץ
def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("File not found")  # הקובץ לא נמצא

# פונקציה להצגת עץ התיקיות והקבצים בצורה היררכית
def print_directory_tree(path=".", level=0):
    for entry in os.listdir(path):
        entry_path = os.path.join(path, entry)
        print(" " * level * 4 + "|── " + entry)
        if os.path.isdir(entry_path):
            print_directory_tree(entry_path, level + 1)

# פונקציה ראשית שמנהלת את הקלט והפעולות
def main():
    commands = {
        "ls": list_items,
        "cd..": go_up_dir,
        "tree": print_directory_tree
    }

    while True:
        print(f"\nCurrent Directory: {os.getcwd()}")  # מציג את התיקייה הנוכחית
        command = input("Enter command: ").strip()

        if command in commands:
            commands[command]()
        elif command.startswith("cd "):
            directory_name = command[3:].strip()
            change_dir(directory_name)
        elif command.startswith("mkdir "):
            directory_name = command[6:].strip()
            create_dir(directory_name)
        elif command.startswith("rmdir "):
            directory_name = command[6:].strip()
            delete_dir(directory_name)
        elif command.startswith("del "):
            file_name = command[4:].strip()
            delete_file(file_name)
        else:
            print("Unknown command")  # פקודה לא מוכרת

if __name__ == "__main__":
    main()

class Student:
    pass


def main():
    student = get_student()
    # print(student)
    print(f"{student.name} is {student.age}")

def get_student():
    student = Student()
    student.name = input("Name:")
    student.age = input("Age:")
    
    return student


if __name__ == "__main__":
    main()
    
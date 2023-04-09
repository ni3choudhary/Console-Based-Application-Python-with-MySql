from db_operations import DBOperations
import sys
from utils.logger import logging
from utils.exception import CustomException

def main():
    db = DBOperations()
    print("***********WELCOME********")
    while True:
        print()
        print("PRESS 1 to Display All Student Details")
        print("PRESS 2 to Insert New Student")
        print("PRESS 3 to Delete Student Details")
        print("PRESS 4 to Update Student Details")
        print("PRESS 0 to exit program")
        print()
        try:
            choice = int(input())
            if (choice == 1):
                #display student details
                db.fetch_all()
            elif choice == 2:
                #insert student details
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                major = input("Enter Major Subject: ")
                birthdate = input("Enter BirthDate: ")
                db.insert_student(student_id, first_name, last_name, major, birthdate)
            elif choice == 3:
                #delete student details
                student_id = int(
                    input("Enter Student ID to Which You Want to Delete: "))
                db.delete_student(student_id)
            elif choice == 4:
                #update student details
                student_id = int(input("Enter Student ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                major = input("Enter Major Subject: ")
                birthdate = input("Enter BirthDate: ")
                db.update_student(student_id, first_name, last_name, major, birthdate)
            elif choice == 0:
                break
            else:
                print("Invalid Input!! Try Again...")
        except Exception as e:
            logging.exception(CustomException(e, sys))
            raise CustomException(e, sys)


if __name__ == "__main__":
    main()

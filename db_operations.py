import mysql.connector as connector
import os
import sys
from dotenv import load_dotenv
load_dotenv()

from utils.logger import logging
from utils.exception import CustomException

# Load Connection Variables
HOST = os.environ['HOST']
PORT = os.environ['PORT']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']

TABLE_NAME = 'student'

class DBOperations:
    def __init__(self):
        try:
            self.con = connector.connect(host=HOST,
                                        port=PORT,
                                        user=USER,
                                        password=PASSWORD,
                                        database=DATABASE)
            query = f"create table if not exists {TABLE_NAME}(studentId int primary key, firstName varchar(20), lastName varchar(20), major varchar(20), birthdate date)"
            cursor = self.con.cursor()
            cursor.execute(query)
            logging.info("Created Table Successfully...")
        except Exception as e:
            logging.exception(CustomException(e, sys))
            raise CustomException(e, sys)


    # Insert Student Data
    def insert_student(self, student_id, firstname, lastname, major_sub, birthdate):
        try:
            query = f"insert into {TABLE_NAME}(studentId, firstName, lastName, major, birthdate) values({student_id},'{firstname}','{lastname}','{major_sub}', '{birthdate}')"
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            logging.info("Student Data Saved to Database...")
            
        except Exception as e:
            logging.exception(CustomException(e, sys))
            raise CustomException(e, sys)
        

    # Fetch All Details
    def fetch_all(self):
        try:
            query = f"select * from {TABLE_NAME}"
            cursor = self.con.cursor()
            cursor.execute(query)
            for row in cursor:
                print("User Id : ", row[0])
                print("User Name :", row[1])
                print("Major : ", row[3])
                print()
            logging.info("Data Fetched Successfully...")
        except Exception as e:
            logging.exception(CustomException(e, sys))
            raise CustomException(e, sys)

    # delete student
    def delete_student(self, student_id):
        try:
            query = f"delete from {TABLE_NAME} where studentId= {student_id}"
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            logging.info(f"Deleted Details of Student with ID[{student_id}] Successfully...")
        except Exception as e:
            logging.exception(CustomException(e, sys))
            raise CustomException(e, sys)
    
    #Update Student Details
    def update_student(self, student_id, first_name, last_name, major, birthdate):
        try:
            query = f"update {TABLE_NAME} set firstName='{first_name}',lastName='{last_name}', major='{major}',birthdate='{birthdate}' where studentId={student_id}"
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            logging.info(f"Updated Details of Student with ID[{student_id}] Successfully...")
        except Exception as e:
            logging.exception(CustomException(e, sys))
            raise CustomException(e, sys)


# helper = DBOperations()
# helper.insert_student(2, 'Gaurav', 'Choudhary', 'Dancer', '1998-05-09')
# helper.insert_student(3, 'Piyush', 'Mahajan', 'Actor', '1999-10-08')
# helper.insert_student(4, 'Sanket', 'Patil', 'Comedian', '2001-02-22')
# helper.fetch_all()
# helper.delete_student(2)
# helper.fetch_all()
# helper.update_student(3, 'Piyush', 'Mahajan', 'Actor', '1999-10-07')
# helper.fetch_all()
import csv
from course import Course
import sqlite3
    
def add_to_db(data):
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    for row in data[1:]:
        print(row)
        course = Course(row[0],row[0] + row[1], row[2], row[3], row[4], row[5])

        required = 0
        req_time_slots = row[6].strip().split("\n")
        for time in req_time_slots:
            day, hour = time.split(" | ")
            hour_split = hour.split(" - ")
            start_hour = int(hour_split[0][0:2])
            end_hour = int(hour_split[1][0:2])
            required += end_hour - start_hour
        cursor.execute('''
            INSERT INTO courses (course_name, section_name, faculty, description, credits, lecturer, required)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (course.course_name, course.section_name, course.faculty, course.description, course.credits, course.lecturer,required))
        conn.commit()

        course_id = cursor.lastrowid

        time_slots = row[6].strip().split("\n")
        for time_slot in time_slots:
            day, hour = time_slot.split(" | ")

            day_id = 0
            if day == "Pazartesi":
                day_id = 1
            elif day == "Salı":
                day_id = 14
            elif day == "Çarşamba":
                day_id = 27
            elif day == "Perşembe":
                day_id = 40
            elif day == "Cuma":
                day_id = 53

            sep_hours = hour.split(" - ")
            start_hour = int(sep_hours[0][0:2])
            end_hour = int(sep_hours[1][0:2]) - 1

            start_hour_id = start_hour - 8
            end_hour_id = end_hour - 8

            cursor.execute('''
                           INSERT INTO course_time_slots (course_id, start_time_id, end_time_id)
                            VALUES (?, ?, ?)
                        ''', (course_id, start_hour_id+day_id, end_hour_id+day_id))
            conn.commit()
    conn.close()
   
def handle_time_table():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    for day in ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]:
        for hour in range(8, 21):
            hour = f"{hour}:40"
            cursor.execute('''
                INSERT INTO time_slots (day_of_week, hour_of_day)
                VALUES (?, ?)
            ''', (day, hour))
            conn.commit()

def main():
    with open("faculty_of_engineering.csv", 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)
        add_to_db(data=data)
        handle_time_table()
    
if __name__ == "__main__":
    main()
    
    
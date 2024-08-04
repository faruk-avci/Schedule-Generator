import sqlite3

def create_database(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create table for courses
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            course_name TEXT NOT NULL,
            section_name TEXT NOT NULL,
            faculty TEXT NOT NULL,
            description TEXT,
            credits REAL NOT NULL,
            lecturer TEXT NOT NULL,
            required INTEGER NOT NULL
        )
    ''')
    conn.commit()

    # Create table for time slots
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS time_slots (
            time_id INTEGER PRIMARY KEY,
            day_of_week TEXT NOT NULL,
            hour_of_day INTEGER NOT NULL
        )
    ''')
    conn.commit()

    # Create table for course time slots
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS course_time_slots (
            course_id INTEGER NOT NULL,
            start_time_id INTEGER NOT NULL,
            end_time_id INTEGER NOT NULL,
            FOREIGN KEY(course_id) REFERENCES courses(id),
            FOREIGN KEY(start_time_id) REFERENCES time_slots(time_id),
            FOREIGN KEY(end_time_id) REFERENCES time_slots(time_id)
        )
    ''')
    conn.commit()

    conn.close()

if __name__ == "__main__":
    create_database('courses.db')

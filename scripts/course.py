
class Course:
    def __init__(self, course_name, section_name, description, faculty, credits, lecturer):
        self.course_name = course_name
        self.section_name = section_name
        self.faculty = faculty
        self.description = description
        self.credits = credits
        self.lecturer = lecturer
    
    def __str__(self):
        return f"Course: {self.course_name}\nSection: {self.section_name}\nFaculty: {self.faculty}\nDescription: {self.description}\nCredits: {self.credits}\nLecturer: {self.lecturer}\nTime Slots: {self.time_slots}"
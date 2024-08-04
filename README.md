# Schedule Generator

## Overview

The Schedule Generator is a Node.js application that allows users to manage and generate course schedules. It provides functionalities for searching courses, adding or removing courses from a session, and generating schedules based on the selected courses. The backend uses SQLite for database operations and Python for generating schedules.

## Features

- **Course Search**: Search for courses by name and retrieve details including sections.
- **Add Course**: Add courses to the session with their respective credits.
- **Remove Course**: Remove courses from the session.
- **View Added Courses**: Retrieve the list of courses added to the session.
- **Total Credits and Lessons**: Get the total credits and number of lessons in the session.
- **Generate Schedules**: Generate schedules using a Python script based on the courses in the session.

## Technologies Used

- **Node.js**: For the main server-side application.
- **Express.js**: For building the web server.
- **SQLite**: For database management.
- **Python**: For generating schedules.
- **Body-parser**: For parsing incoming request bodies.
- **Express-session**: For managing user sessions.

## Setup

### Prerequisites

- Node.js (version 16 or higher)
- Python 3.x
- SQLite

### Running the Application

Clone the repository and run:
```bash
npm install
```
and then run this:
```bash
node index.js
```


## API Endpoints

- **GET /**: Serve the main HTML page.
- **POST /search**: Search for courses by name.
- **POST /add-course**: Add a course to the session.
- **POST /remove-course**: Remove a course from the session.
- **GET /get-added-courses**: Retrieve the list of added courses.
- **GET /get-total-credit-lesson**: Get the total credits and number of lessons.
- **POST /generate-schedules**: Generate schedules based on the added courses.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your changes include tests and adhere to the project's coding standards.


## Contact

For any questions or support, please reach out to [faruk.avci@ozu.edu.tr](mailto:faruk.avci@ozu.edu.tr).

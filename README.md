# Online Quiz Management System

A simple Python-based quiz management system that lets an admin create quizzes and questions, and lets students take quizzes and view their scores. Built as a college project for Introduction to Python (24CSA209).

## Features

**Admin**
- Add new quizzes
- Add questions (with 4 options and a correct answer) to a quiz
- View all quizzes and how many questions each has

**Student**
- View available quizzes
- Take a quiz and get instant right/wrong feedback per question
- See a final score at the end

## How it works

- All quiz data (quizzes, questions, options, correct answers) is stored in `quizzes.txt` using Python's `json` module, so data is saved permanently and reloaded every time the program runs.
- Basic validation prevents duplicate quiz names and handles missing quizzes/questions gracefully.

## How to run

```bash
python quiz_management_system.py
```

Default admin login:
- Username: `admin`
- Password: `admin`

## Tech used

Python, JSON (built-in `json` and `os` modules — no external libraries required)

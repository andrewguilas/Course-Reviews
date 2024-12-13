# Plan

## Goals
- [ ] Demonstrate knowledge of Python
- [ ] Demonstrate knowledge of Python's OOP principles
- [ ] Demonstrate knowledge of unit testing
- [ ] Demonstrate knowledge of Tkinter for GUI
- [ ] Demonstrate use of SQLite for database
- [ ] Finish by Dec 15, 11:59pm

## Database
- [ ] Store user username, password, and course reviews
- [ ] Encrypt passwords
- [ ] Store course information and reviews
- [ ] Minimum error handling at the database level

## GUI
- [ ] Error handling at the GUI level as a popup
- [ ] Implement a consistent theme
- [ ] Add tooltips for better user experience

## Login Scene
- [x] Input username & password
- [x] Login/register user
- [x] Check for valid username & password format

## Course List Scene
- [x] List of all courses
- [x] Search by mnemonic, number, and title
- [ ] Sort alphabetically, average rating, review counter, and more recent review
- [ ] Average course rating
- [x] New course button
- [ ] My reviews button
- [ ] Log off button 

## New Course Scene
- [x] Input course mnemonic, number, and title
- [x] Check for valid formats
- [x] Back button
- [ ] Log off button 

## Course Reviews Scene
- [ ] List of all reviews for a specific course
- [ ] Sort by rating and date
- [ ] Edit/delete button for current user's reviews and confirmation dialogue
- [ ] New review button
- [ ] Back button
- [ ] Log off button 

## New Review Scene
- [ ] Input rating and comment
- [ ] Check for valid formats
- [ ] Back button
- [ ] Log off button 

## My Reviews Scene
- [ ] List of all reviews for the current user
- [ ] Sort by course, date, and rating
- [ ] Edit/delete button for current user's reviews and confirmation dialogue
- [ ] Back button
- [ ] Log off button 

## Admin Panel (if time permits)
- View, edit, and delete users
- View, edit, and delete courses
- View, edit, and delete reviews

## Proposed File Structure
```
course_review_app/
│
├── app.py                  # Main application file (Flask app setup and routing)
├── requirements.txt        # Python dependencies (Flask, SQLite, etc.)
├── config.py               # Configuration settings (e.g., database URL)
│
├── static/                  # Static files (e.g., CSS, JavaScript, images)
│   ├── css/                 # CSS files
│   │   └── style.css        # Styling for the app
│   └── images/              # Image files for the app (e.g., logos)
│
├── templates/               # HTML templates (for rendering pages)
│   ├── layout.html          # Base template (header, footer, navigation)
│   ├── index.html           # Home page template
│   ├── course_list.html     # Template to display all courses
│   ├── course_detail.html   # Template to display course details and reviews
│   └── login.html           # Login page template
│
├── database/                # SQL and database-related files
│   ├── schema.sql           # SQL file to create the database schema (tables, etc.)
│   └── db.py                # Python file to handle database operations (e.g., connect to DB)
│
├── models/                  # Python files for app logic
│   ├── user.py              # User model (sign-up, login, etc.)
│   ├── course.py            # Course model (course-related operations)
│   └── review.py            # Review model (review-related operations)
│
├── migrations/              # Optional if using Alembic for DB migrations (for more advanced setups)
│   └── versions/            # Directory for migration scripts
│
└── tests/                   # Unit tests for your app
    ├── test_app.py          # Tests for app routes and logic
    ├── test_models.py       # Tests for database models and logic
    └── test_forms.py        # Tests for form validation and user input

```
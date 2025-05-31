# Django Course Management System

This project is a Django-based Course Management System where:
- Admin can manage Courses and Students.
- Each Student is linked to a Django User and can enroll in one Course.
- User creation and linking is handled automatically when adding a Student.
- Admin can combine courses, and student status is managed automatically.

## Features

- **User Management:**  
  Each student is linked to a Django User. When a student is deleted, their user is deactivated.
- **Course Management:**  
  Add, edit, delete, and combine courses from the admin panel.
- **Student Management:**  
  Add students with first name, last name, email, username, and course.  
  Student creation also creates/links a Django User.
- **Admin Customization:**  
  User admin shows only the "Active" status (not staff status).  
  Student admin shows user details and course.
- **Beautiful Forms:**  
  Bootstrap-styled forms for a modern look.

## Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd <your-project-folder>
   ```

2. **Install dependencies:**
   ```sh
   pip install django
   ```

3. **Apply migrations:**
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a superuser:**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the admin panel:**  
   Go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with your superuser credentials.

## Usage

- **Add Courses** from the admin panel.
- **Add Students** from the admin panel or custom form.  
  Enter first name, last name, email, username, and select a course.
- **Combine Courses:**  
  Select two or more courses in the admin and use the "Combine selected courses" action.
- **Delete Students:**  
  When a student is deleted, their linked user is deactivated (not deleted).

## File Structure

- `courses/models.py` — Models for Course and Student.
- `courses/forms.py` — Custom forms for Student and Course.
- `courses/admin.py` — Admin customizations.
- `courses/templates/courses/` — Bootstrap-styled HTML templates.

## Notes

- Each student can enroll in only one course (as per current form).
- Username must be unique for each student/user.
- When combining courses, students enrolled in both will appear only once in the new course.

---

**Enjoy managing your courses and students with Django!**
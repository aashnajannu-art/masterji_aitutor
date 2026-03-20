# Import Django's model tools so we can define database tables as Python classes.
from django.db import models


# Store student account information in the database.
class StudentLogin(models.Model):
    # Save the student's first name.
    first_name = models.CharField(max_length=100)
    # Save the student's last name.
    last_name = models.CharField(max_length=100)
    # Save a unique email for each student account.
    email = models.EmailField(unique=True)
    # Save the hashed password instead of plain text.
    password_hash = models.CharField(max_length=256)
    # Record when the account was first created.
    created_at = models.DateTimeField(auto_now_add=True)
    # Record the most recent time this row was updated.
    last_login_at = models.DateTimeField(auto_now=True)

    # Return a readable label for this student in the Django admin or shell.
    def __str__(self):
        return f"{self.first_name} {self.last_name} <{self.email}>"

from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    experience_points = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title

class PythonWorkspace(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    code = models.TextField()

    def __str__(self):
        return f"Workspace for {self.user.username}"
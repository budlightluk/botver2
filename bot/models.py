from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.first_name} ({self.telegram_id})"


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    creator = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, related_name='created_projects')
    members = models.ManyToManyField(TelegramUser, related_name='projects')

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    description = models.TextField()
    assigned_to = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20,
                              choices=[('TODO', 'To Do'), ('IN_PROGRESS', 'In Progress'), ('DONE', 'Done')])

    def __str__(self):
        return f"{self.description[:20]}... ({self.project.name})"

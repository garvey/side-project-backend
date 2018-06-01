from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        """A string representation of the model."""
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    crest = models.CharField(max_length=100)

    def __str__(self):
        """A string representation of the model."""
        return self.name



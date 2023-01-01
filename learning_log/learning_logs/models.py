"""The beginning of the models.py file."""
from django.db import models

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return str(self.text)

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Holds extra information for managing a model."""
        verbose_name_plural = 'entries'

    def set_text(self, text: str) -> None:
        """Ensuring the text field is assigned a value before __str__ method is called"""
        self.text = text

    def __str__(self) -> str:
        """Return a string representation of the model."""
        return str(f"{self.text[:50]}...")

# Create your models here.

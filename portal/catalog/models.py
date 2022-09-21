from django.db import models
from django.urls import reverse
import datetime


# Create your models here.

class Category(models.Model):
    """
    Model representing a category of record (e.g. ).
    """
    name = models.CharField(max_length=200, help_text="Enter a category of record")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Record(models.Model):
    """
    Model representing a record.
    """
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000, help_text="Enter a description of the record")

    category = models.ManyToManyField(Category, help_text="Select a genre for this book")

    # timestamp = datetime.date.today()
    LOAN_STATUS = (
        ('p', 'Performed'),
        ('a', 'Accepted for work'),
    )

    status = models.CharField(
        max_length=100,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Record availability')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular record.
        """
        return reverse('record-detail', args=[str(self.id)])



from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.db import models


class Category(models.Model):
    """Model representing a recipe's category"""
    name = models.CharField(
        max_length=50, help_text='Enter a recipe category (breakfast, lunch, dinner, etc.)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Recipe(models.Model):
    """Model representing a recipe"""
    title = models.CharField(max_length=200)

    # Foreign Key used because recipe can only have one author, but authors can have multiple recipes
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    summary = models.TextField(
        max_length=300, help_text='Enter a brief description of the recipe')

    ingredients = models.TextField(
        max_length=1000, help_text='Enter the ingredients and the amounts of each item for this recipe')

    servings = models.CharField(
        max_length=100, help_text='Enter the amount of servings this recipe yields')

    prep_time = models.CharField(
        max_length=100, help_text='Enter the amount of time this recipe takes to prepare')
    
    cook_time = models.CharField(
        max_length=100, help_text='Enter the amount of time this recipe takes to cook')

    created = models.DateField()

    steps = models.TextField(
        max_length=3000, help_text='Enter the step-by-step instructions to make this recipe')

    notes = models.TextField(
        null=True, blank=True, max_length=300, help_text='Enter any helpful tips about this recipe')

    # ManyToManyField used because category can contain many recipes. Recipes can fall into various categories.
    # Category class has already been defined so we can specify the object.
    category = models.ManyToManyField(
        Category, help_text='Select a category for this recipe')

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this recipe."""
        return reverse('recipe-detail', args=[str(self.id)])


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

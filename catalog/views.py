from django.shortcuts import render
from catalog.models import Category, Recipe, Author

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_recipes = Recipe.objects.all().count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_categories = Category.objects.count()

    context = {
        'num_recipes': num_recipes,
        'num_authors': num_authors,
        'num_categories': num_categories,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

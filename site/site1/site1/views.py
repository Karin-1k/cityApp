from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # List of French cities
    cities = [
        {"name": "Paris", "population": 2140526, "famous_for": "Eiffel Tower, Louvre Museum"},
        {"name": "Marseille", "population": 863310, "famous_for": "Old Port, Notre-Dame de la Garde"},
        {"name": "Lyon", "population": 513275, "famous_for": "Basilique Notre-Dame de Fourvière, Traboules"},
        {"name": "Nice", "population": 342295, "famous_for": "Promenade des Anglais, Cours Saleya"},
        {"name": "Bordeaux", "population": 257068, "famous_for": "Wine, Place de la Bourse"}
    ]

    # Creating a formatted HTML response with city information
    html_response = "<h1>Popular Cities in France</h1>"
    html_response += "<ul>"
    for city in cities:
        html_response += f"<li><strong>{city['name']}</strong>: Population {city['population']}, Famous for {city['famous_for']}</li>"
    html_response += "</ul>"

    return HttpResponse(html_response)

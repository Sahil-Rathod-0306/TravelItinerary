from django.shortcuts import render, HttpResponse

from django.shortcuts import render
import requests  
# Create your views heredef 
def index(request):
    return render (request, "index.html")

def home(request):
    return render (request, "home.html")

def Destinations(request):
    return render (request, "Destinations.html")

def about(request):
    return render (request, "about.html")

def contacts(request):
    return render (request, "contacts.html")

def login(request):
    return render (request, "login.html")

def register(request):
    return render (request, "register.html")

def detail(request):
    return render (request, "detail.html")

def planTrip(request):
    return render (request, "planTrip.html")
from django.shortcuts import render

def destinations_view(request):
    destinations = [
        {"title": "GOA TRIP", "image": "Photos/Goa.jpg", "description": "Goa, India's beach paradise, is known for its stunning shores, water sports, nightlife, historic forts, and vibrant culture."},
        {"title": "Ayodhya", "image": "Photos/ayodhya.jpg", "description": "Ayodhya, a historic city in Uttar Pradesh, India, is the revered birthplace of Lord Rama and a major pilgrimage site, home to the Ram Mandir and ancient temples."},
        {"title": "Manali", "image": "Photos/manali.jpg", "description": "Manali is a scenic hill station in Himachal Pradesh, India, known for its snow-capped mountains, adventure sports, and vibrant culture. It's a popular destination for trekking, skiing, and honeymoon trips."},
        {"title": "Rajasthan", "image": "Photos/Rajasthan.jpg", "description": "Rajasthan, the Land of Kings, is known for its majestic palaces, vibrant festivals, and vast golden deserts. It offers a rich cultural heritage, featuring historic forts, colorful bazaars, and traditional folk music."},
        {"title": "Kerala", "image": "Photos/Kerala.jpg", "description": "Kerala, known as 'God’s Own Country,' is famous for its serene backwaters, lush greenery, and Ayurvedic wellness retreats. It offers a unique blend of beaches, hill stations, and rich cultural traditions."},
        {"title": "Sikkim", "image": "Photos/Sikkism.jpg", "description": "Sikkim, a serene Himalayan state, is known for its breathtaking landscapes, Buddhist monasteries, and rich biodiversity. It offers snow-capped peaks, vibrant culture, and peaceful trekking trails."}
    ]
    return render(request, 'destinations.html', {'destinations': destinations})


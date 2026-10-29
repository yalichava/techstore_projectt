from django.shortcuts import render

PRODUCTS = [
    {"name": "Laptop", "price": 2500, "image": "images/laptop.png", "category": "კომპიუტერები", "description": "ძლიერი და თანამედროვე ლეპტოპი"},
    {"name": "Mouse", "price": 80, "image": "images/mouse.png", "category": "აქსესუარები", "description": "კომფორტული უსადენო მაუსი"},
    {"name": "Keyboard", "price": 150, "image": "images/keyboard.png", "category": "აქსესუარები", "description": "მოხერხებული კლავიატურა ყოველდღიური მუშაობისთვის"},
    {"name": "Monitor", "price": 700, "image": "images/monitor.png", "category": "მონიტორები", "description": "მკვეთრი გამოსახულება და ფართო ეკრანი"},
    {"name": "Headphones", "price": 350, "image": "images/headphones.svg", "category": "აუდიო", "description": "სუფთა ხმა და კომფორტული დიზაინი"},
    {"name": "Smartphone", "price": 1800, "image": "images/smartphone.svg", "category": "ტელეფონები", "description": "თანამედროვე სმარტფონი ყოველდღიური გამოყენებისთვის"},
]

def home(request):
    return render(request, "home.html", {"products": PRODUCTS[:3]})

def products(request):
    return render(request, "products.html", {"products": PRODUCTS})

import requests
from django.shortcuts import render

def home (request):

  # USING APIS
  response = requests.get('https://api.github.com/events')
  data = response.json()
  results = data[0]["repo"]

  # Example 2
  response2 = requests.get('https://randomfox.ca/floof/')
  data2 = response2.json()
  results2 = data2["image"]

  
  return render(request, 'templates/index.html', {'results': results, 'results2': results2})
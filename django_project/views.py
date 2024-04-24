from django.shortcuts import render
import requests


def index(request):
  r = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')
  res1 = r.json()
  fact = res1['text']

  r2 = requests.get('https://www.boredapi.com/api/activity')
  res2 = r2.json()
  activity = res2['activity']

  r3 = requests.get('https://dog.ceo/api/breeds/image/random')
  res3 = r3.json()
  dog = res3['message']

  return render(request, "templates/index.html", {
      'fact': fact,
      'activity': activity,
      'dog': dog
  })

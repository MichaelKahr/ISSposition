import json
import urllib.request
import turtle
import time


url = "http://api.open-notify.org/iss-now.json"
response = urllib.request.urlopen(url)
results = json.loads(response.read())
location = results['iss_position']
lat = location['latitude']
lon = location['longitude']
print("Latutude: ",lat)
print("Longitude: ",lon)
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('Map.gif')
screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(90)
iss.penup()
while True:
    url2 = "http://api.open-notify.org/iss-now.json"
    response2 = urllib.request.urlopen(url2)
    results2 = json.loads(response2.read())
    location = results2['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    iss.goto(float(lon),float(lat))
    time.sleep(1)


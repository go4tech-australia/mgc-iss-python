import urllib.request, json

# Checkout what the api returns
issUrl = 'http://api.open-notify.org/iss-now.json'

response = urllib.request.urlopen(issUrl)
result = json.loads(response.read())

print(result)


# set up some variables for the application to understand the result
issPosition = {'latitude': float(result['iss_position']['latitude']), 'longitude': float(result['iss_position']['longitude'])}
latitude = float(result['iss_position']['latitude'])
longitude = float(result['iss_position']['longitude'])

import turtle

# setting up the stage
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90, 180, 90)

screen.bgpic('map.gif')

# setting up iss
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')

# moving iis to where it is right now
iss.penup()
iss.goto(longitude, latitude)
screen.exitonclick()

astrosUrl = 'http://api.open-notify.org/astros.json'
astrosResponse = urllib.request.urlopen(astrosUrl)
astrosResult = json.loads(astrosResponse.read())

people = astrosResult['people']
for person in people:
    print(person['name'])
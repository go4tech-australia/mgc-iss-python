# Space Station finder

This project will show you how to create a program that will track location of the International Space Station
and show who is currently out there in space! All with just a little bit of python code and some awesome pictures.

## Getting Started

Please make sure that python is install on your PC and there is an internet access as our application will need to communicate
to orher programs to get updates of the Space Station Location.

## Things to be aware of

 - API (Application Programming Interface) is an abstraction that allows different machines talk to each other over a network.
 Typically, APIs would used a specific format of communication, for example JSON.
 - JSON (JavaScript Object Notation) - is a standartized format that is readable for both machines and humans. It allows different systems
 to understand messages sent and reseaved between each other.  

## The main task

Our main goal for today will be to find where the International Space Station is right now and show it on a map.
To do that we will need to use an API (Application Programming Interface) to get its location saved on the internet.
The position is updated every second that is quite accurate for something that is flying so far from us with almost nothing around!

### Step 0

Open the Visual Studio Code text editor and click File -> open folder -> [navigate to the folder where the workshop materials are]

### Step 1

Firstly, lets see what API response we would get and get to know the data.
For that, go to http://api.open-notify.org/iss-now.json, you shold see something like

```
{
  "timestamp": 1534660081,
  "iss_position": {
    "latitude": "-49.8355",
    "longitude": "-110.4369"
  },
  "message": "success"
}
```
#### Making sense of the data

As you can see there is 
 - a timestamp (which is the current date formatted in seconds passed since 01.01.1970)
 - the iss position consisting on latitude and longitude
 - message (should be saying success unless something is wrong with the API)

 ### Step 2
 Now let's do the same thing but from our python script!

 First, make sure that your Visual Studio Code is in front of you and you have a new empty file opened there.

Then, let's type in the following:

```
#getting libraries for working with the API
import urllib.request, json 

# getting data from the api
issUrl = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(issUrl)
result = json.loads(response.read())

# setting variables from the data
latitude = float(result['iss_position']['latitude'])
longitude = float(result['iss_position']['longitude'])
```

### Step 3 Creating a canvas space

Before we start, make sure that all the  files from the repository are in the same folder with your code.

Now let's continue:

```
import turtle
# setting up the stage
screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90, 180, 90)
screen.bgpic('map.gif')
```

### Step 4 Drawing the ISS on the map

Time to draw the ISS icon on top of the map:
```
# setting up iss
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
# moving the iss figure to where it is right now
iss.penup()
iss.goto(longitude, latitude)
screen.exitonclick()
```

Done! Now you should be able to see the resulting image!

## Bonus task

If you would like to play more, see if you could print out the names of each person currently on board of the ISS.

You will need to use this url: http://api.open-notify.org/astros.json
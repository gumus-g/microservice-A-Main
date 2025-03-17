import zmq
import json

# Load recipes from JSON file
with open('recipes.json', 'r') as f:
    recipes_data = json.load(f)

def browse_recipes():
    return json.dumps(recipes_data["recipes"])

# ZeroMQ context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("Browse Recipes Server is running...")

while True:
    message = socket.recv()
    if message.decode() == "browse":
        recipes = browse_recipes()
        socket.send_string(recipes)
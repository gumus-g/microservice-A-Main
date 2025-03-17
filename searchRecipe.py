import zmq
import json

# Load recipes from JSON file
with open('recipes.json', 'r') as f:
    recipes_data = json.load(f)
    recipes = recipes_data["recipes"]

def search_recipes(keyword):
    return json.dumps([recipe for recipe in recipes if keyword.lower() in recipe["name"].lower()])

# ZeroMQ context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5556")

print("Search Recipes Server is running...")

while True:
    message = socket.recv_string()
    search_result = search_recipes(message)
    socket.send_string(search_result)
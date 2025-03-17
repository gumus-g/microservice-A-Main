import zmq
import json

# Load recipes from JSON file
with open('recipes.json', 'r') as f:
    recipes_data = json.load(f)
    recipe_details = {recipe["id"]: recipe for recipe in recipes_data["recipes"]}

def view_recipe_details(recipe_id):
    return json.dumps(recipe_details.get(recipe_id, {}))

# ZeroMQ context and socket setup
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

print("View Recipe Server is running...")

while True:
    message = socket.recv_string()
    recipe_id = int(message)
    details = view_recipe_details(recipe_id)
    socket.send_string(details)
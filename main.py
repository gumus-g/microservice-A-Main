import zmq
import json

context = zmq.Context()

# Function to browse recipes
def browse_recipes():
    print("Fetching recipes, please wait...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")
    socket.send_string("browse")
    recipes = socket.recv_string()
    print("Recipes fetched successfully.")
    return json.loads(recipes)

# Function to search recipes
def search_recipes(keyword):
    print(f"Searching for recipes with keyword '{keyword}', please wait...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5556")
    socket.send_string(keyword)
    search_results = socket.recv_string()
    print("Search completed.")
    return json.loads(search_results)

# Function to view recipe details
def view_recipe_details(recipe_id):
    print(f"Fetching details for recipe ID '{recipe_id}', please wait...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5557")
    socket.send_string(str(recipe_id))
    details = socket.recv_string()
    print("Recipe details fetched successfully.")
    return json.loads(details)

# Function to display help
def display_help():
    help_text = """
    Recipe Catalog App - Help Information

    1. Browse Recipes:
       - Select option 1 from the main menu to view a list of available recipes.
    2. Search Recipes:
       - Select option 2 from the main menu to search for recipes by keyword.
       - Enter the keyword and press enter to see the search results.
    3. View Recipe Details:
       - Select option 3 from the main menu to view detailed information about a specific recipe.
       - Enter the recipe ID to view its ingredients and steps.
    4. Help:
       - Select option 4 from the main menu to view this help guide.
    5. Exit:
       - Select option 5 from the main menu to exit the application.
    """
    print("Displaying help information...")
    print(help_text)

# Function to check if the user wants to save their work before exiting 
def check_unsaved_changes():
    unsaved_changes = input("\nDo you have any unsaved changes? If you exit without saving, you may lose your work. Type 'yes' or 'no': ")
    if unsaved_changes.lower() == "yes":
        save = input("Would you like to save your changes before exiting? Type 'yes' or 'no': ")
        if save.lower() == "yes":
            print("Your changes have been saved.")
        else:
            print("You chose not to save your changes.")
    else:
        print("No unsaved changes to worry about.")

# Main program
if __name__ == "__main__":
    while True:
        print("\nWelcome to Recipe Catalog App")
        print("\nAbout the Recipe App :")
        print("Our Recipe Catalog App lets you explore a variety of delicious recipes at your fingertips.")
        print("Whether you want to browse, search, or view detailed recipes, we've got you covered.")
        print("Use our intuitive interface to find your next favorite dish!\n")
        print("Please note: This app requires an internet connection to browse, search, and view recipes. Ensure you have a stable connection to avoid interruptions. Additionally, remember to save your work to prevent data loss.\n")
        print("Please use the main menu options to navigate through the app:")
        print("1. Browse Recipes")
        print("2. Search Recipes")
        print("3. View Recipe Details")
        print("4. Help")
        print("5. Exit")

        choice = input("Enter one of the numbers to discover: ")

        if choice == "1":
            recipes = browse_recipes()
            print("\nAvailable Recipes:")
            for recipe in recipes:
                print(f"- {recipe['name']} (Cuisine: {recipe['cuisine']})")

        elif choice == "2":
            while True:
                keyword = input("\nEnter a keyword to search for recipes: ")
                search_results = search_recipes(keyword)
                if search_results:
                    print("\nSearch Results:")
                    for recipe in search_results:
                        print(f"- {recipe['name']} (Cuisine: {recipe['cuisine']})")
                    break
                else:
                    retry = input("\nNo recipes found matching the keyword. Do you want to try again? Type 'yes' or 'no': ")
                    if retry.lower() != "yes":
                        break

        elif choice == "3":
            recipe_id = int(input("\nEnter the recipe ID to view details: "))
            details = view_recipe_details(recipe_id)
            if details:
                print(f"\nRecipe Details for {details['name']}:")
                print("Ingredients:")
                for ingredient in details["ingredients"]:
                    print(f"- {ingredient}")
                print("Steps:")
                for step in details["steps"]:
                    print(f"- {step}")
            else:
                print("\nRecipe not found.")

        elif choice == "4":
            display_help()

        elif choice == "5":
            check_unsaved_changes()
            confirm_exit = input("Are you sure you want to exit? Type 'yes' or 'no': ")
            if confirm_exit.lower() == "yes":
                print("Exiting the application. Bye!")
                break
            else:
                print("\nExit cancelled.")

        else:
            print("\nInvalid choice. Please try again.")
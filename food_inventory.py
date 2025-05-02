import json
import os

FOOD_INVENTORY_FILE = "food_inventory.json"

def load_data(file_path):
    """Load data from a file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_data(file_path, data):
    """Save data to a file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def add_food_item():
    """Add a new food item to the inventory."""
    name = input("🍔 Enter the food name: ")
    calories = input("🔥 Enter calories: ")
    protein = input("💪 Enter protein content (g): ")
    carbs = input("🍞 Enter carbs content (g): ")
    fat = input("🥑 Enter fat content (g): ")
    servings = input("🍽️ Enter servings: ")

    food_item = {
        "name": name,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat,
        "servings": servings
    }

    food_inventory = load_data(FOOD_INVENTORY_FILE)
    food_inventory.append(food_item)
    save_data(FOOD_INVENTORY_FILE, food_inventory)

    print("✅ Food item added!\n")

def view_food_inventory():
    """View all food items in the inventory."""
    food_inventory = load_data(FOOD_INVENTORY_FILE)
    if not food_inventory:
        print("❌ No food items recorded yet.\n")
        return

    print("\n🍽️ Your Food Inventory:\n")
    for i, food in enumerate(food_inventory, 1):
        print(f"{i}. {food['name']} - {food['calories']} kcal, {food['protein']}g protein, {food['carbs']}g carbs, {food['fat']}g fat, {food['servings']} servings")
        print("\n")

def main():
    while True:
        print("=== Food Inventory Menu ===")
        print("1. Add new food item")
        print("2. View food inventory")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_food_item()
        elif choice == "2":
            view_food_inventory()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()

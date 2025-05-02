import json
from datetime import datetime
import os

DATA_FILE = "stat_data.json"

def load_data(file_path):
    """Load stats from JSON file."""
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []

def save_data(file_path, data):
    """Save stats to JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def add_stats():
    """Add a new stat entry."""
    stats_data = load_data(DATA_FILE)

    print("\nEnter your new stats:")
    weight = input("🏋️ Enter your weight (lbs): ")
    bmi = input("📊 Enter your BMI: ")
    body_fat = input("💧 Enter your body fat %: ")
    body_water = input("💦 Enter your body water %: ")
    muscle_mass = input("💪 Enter your muscle mass %: ")
    kcal = input("🔥 Enter your kcal intake: ")

    new_stat = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "weight": weight,
        "bmi": bmi,
        "body_fat": body_fat,
        "body_water": body_water,
        "muscle_mass": muscle_mass,
        "kcal": kcal
    }

    stats_data.append(new_stat)
    save_data(DATA_FILE, stats_data)
    print("\n✅ Stat entry added!\n")

def modify_stat(stats_data):
    """Allow user to modify an existing stat entry."""
    if not stats_data:
        print("❌ No stats recorded yet.\n")
        return

    print("\n📈 Your Stat History:\n")
    for i, entry in enumerate(stats_data, 1):
        print(f"{i}. Date: {entry['date']} - Weight: {entry['weight']} lbs")

    stat_index = input("\nSelect the stat entry you want to modify (or press Enter to cancel): ")
    if stat_index.strip():
        try:
            stat_index = int(stat_index) - 1
            if 0 <= stat_index < len(stats_data):
                entry = stats_data[stat_index]

                print("\n✏️ Edit this entry (press Enter to keep current value):")
                entry['weight'] = input(f"🏋️ Current weight ({entry['weight']} lbs): ") or entry['weight']
                entry['bmi'] = input(f"📊 Current BMI ({entry['bmi']}): ") or entry['bmi']
                entry['body_fat'] = input(f"💧 Current body fat % ({entry['body_fat']}%): ") or entry['body_fat']
                entry['body_water'] = input(f"💦 Current body water % ({entry['body_water']}%): ") or entry['body_water']
                entry['muscle_mass'] = input(f"💪 Current muscle mass ({entry['muscle_mass']}%): ") or entry['muscle_mass']
                entry['kcal'] = input(f"🔥 Current kcal intake ({entry['kcal']} kcal): ") or entry['kcal']

                save_data(DATA_FILE, stats_data)
                print("\n✅ Stat entry updated!\n")
            else:
                print("❌ Invalid selection. Returning to menu.\n")
        except ValueError:
            print("❌ Invalid input. Returning to menu.\n")
    else:
        print("❌ No stat selected. Returning to menu.\n")

def add_or_edit_stats():
    """Add new stat entry or modify an existing one."""
    stats_data = load_data(DATA_FILE)
    print("\nWould you like to:")
    print("1. Add new stat entry")
    print("2. Edit an existing stat entry")
    choice = input("Choose an option: ")

    if choice == "1":
        add_stats()
    elif choice == "2":
        modify_stat(stats_data)
    else:
        print("❌ Invalid option.\n")

def view_stats():
    """Display all recorded stats."""
    stats_data = load_data(DATA_FILE)

    if not stats_data:
        print("❌ No stats recorded yet.\n")
        return

    print("\n📈 Your Stat History:\n")
    for entry in stats_data:
        print(f"Date: {entry['date']}")
        print(f"  Weight: {entry['weight']} lbs")
        print(f"  BMI: {entry['bmi']}")
        print(f"  Body Fat: {entry['body_fat']}%")
        print(f"  Body Water: {entry['body_water']}%")
        print(f"  Muscle Mass: {entry['muscle_mass']}%")
        print(f"  Kcal Intake: {entry['kcal']} kcal\n")

def main():
    while True:
        print("=== Stat Tracker Menu ===")
        print("1. Add or Edit stat entry")
        print("2. View all stats")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_or_edit_stats()
        elif choice == "2":
            view_stats()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()

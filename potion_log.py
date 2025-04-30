# Save as potion_log.py

import streamlit as st

# Potion database
potions = {
    "1": {
        "category": "Healing",
        "potions": [
            {
                "name": "Lesser Healing Potion",
                "danger_level": "Low",
                "ingredients": ["Pixie Dust", "Red Herb", "Crystal Water"],
                "cost": "25 gold"
            },
            {
                "name": "Greater Healing Potion",
                "danger_level": "Medium",
                "ingredients": ["Unicorn Hair", "Red Herb", "Holy Water"],
                "cost": "75 gold"
            }
        ]
    },
    "2": {
        "category": "Damage",
        "potions": [
            {
                "name": "Fire Bomb Potion",
                "danger_level": "High",
                "ingredients": ["Sulfur Ash", "Dragon Scale", "Oil"],
                "cost": "100 gold"
            },
            {
                "name": "Poison Draught",
                "danger_level": "Medium",
                "ingredients": ["Nightshade", "Snake Venom", "Rotten Root"],
                "cost": "50 gold"
            }
        ]
    },
    "3": {
        "category": "Buffs",
        "potions": [
            {
                "name": "Potion of Giant Strength",
                "danger_level": "High",
                "ingredients": ["Ogre Blood", "Troll Bone", "Mountain Salt"],
                "cost": "120 gold"
            }
        ]
    }
}

st.set_page_config(page_title="🧪 D&D Potion Log", page_icon="💀")

st.title("🧙 Terminal-style Potion Log")

st.markdown("```\nWelcome adventurer!\nWhat kind of potion do you seek?\n1. Healing\n2. Damage\n3. Buffs\n```")

# Input from user
choice = st.text_input("Enter the number of your choice:")

# Show results based on input
if choice in potions:
    category_data = potions[choice]
    st.markdown(f"```\nYou selected: {category_data['category']} Potions\n```")
    for potion in category_data["potions"]:
        st.markdown(f"```\nName: {potion['name']}\nDanger Level: {potion['danger_level']}\nIngredients: {', '.join(potion['ingredients'])}\nCost: {potion['cost']}\n```")
elif choice:
    st.markdown("```\nUnknown command. Please enter 1, 2, or 3.\n```")

import streamlit as st

# You can paste your full alchemy_data dict here instead of importing it
from updated_code_list import alchemy_data  

def convert_to_bronze(amount, currency):
    return amount * alchemy_data["currency_rates"][currency]

def format_currency(amount):
    gold = amount // 10000
    remainder = amount % 10000
    silver = remainder // 100
    bronze = remainder % 100
    parts = []
    if gold > 0: parts.append(f"{gold} Gold")
    if silver > 0: parts.append(f"{silver} Silver")
    if bronze > 0 or not parts: parts.append(f"{bronze} Bronze")
    return " ".join(parts)

# Track state
if "page" not in st.session_state:
    st.session_state.page = "main"
if "sub_choice" not in st.session_state:
    st.session_state.sub_choice = ""

st.title("Let this fucking dnd thing work please")

# === Main Menu ===
if st.session_state.menu == "main":
    st.subheader("What would you like to do?")
    option = st.radio("Choose an option:", [
        "Browse Ingredients",
        "Browse Mixtures",
        "Search by Category",
        "Search by Safety Level"
    ])
    if option == "Browse Ingredients":
        st.session_state.menu = "ingredients"
    elif option == "Browse Mixtures":
        st.session_state.menu = "mixtures"
    elif option == "Search by Category":
        st.session_state.menu = "category"
    elif option == "Search by Safety Level":
        st.session_state.menu = "safety"
    
# === Ingredients ===
elif st.session_state.page == "ingredients":
    st.markdown("```\n-- INGREDIENT LIST --\nChoose a number to view details or 'back' to return.\n```")
    ingredients = sorted(alchemy_data["ingredients"].keys())
    for i, name in enumerate(ingredients, 1):
        st.markdown(f"{i}. {name}")
    choice = st.text_input("Ingredient number or 'back':", key="ing_choice")

    if choice.lower() == "back":
        st.session_state.page = "main"
    elif choice.isdigit() and 1 <= int(choice) <= len(ingredients):
        ing = ingredients[int(choice) - 1]
        data = alchemy_data["ingredients"][ing]
        st.markdown(f"```\n{ing}\nType: {data['type']} | Safety: {data['safety']}\nPrice: {data['price']} {data['currency']} ({convert_to_bronze(data['price'], data['currency'])} Bronze)\n\n[States]\nNatural: {data['states']['natural']}\nHeated: {data['states']['heated']}\nFrozen: {data['states']['frozen']}\n```")
    elif choice:
        st.warning("Invalid selection.")

# === Mixtures ===
elif st.session_state.page == "mixtures":
    st.markdown("```\n-- MIXTURE LIST --\nChoose a number to view details or 'back' to return.\n```")
    mixtures = sorted(alchemy_data["mixtures"].keys())
    for i, name in enumerate(mixtures, 1):
        stars = "★" * alchemy_data["mixtures"][name]["danger"]
        st.markdown(f"{i}. {name} {stars}")
    choice = st.text_input("Mixture number or 'back':", key="mix_choice")

    if choice.lower() == "back":
        st.session_state.page = "main"
    elif choice.isdigit() and 1 <= int(choice) <= len(mixtures):
        mix = mixtures[int(choice) - 1]
        data = alchemy_data["mixtures"][mix]
        total_cost = sum(
            convert_to_bronze(alchemy_data["ingredients"][ing]["price"],
                              alchemy_data["ingredients"][ing]["currency"])
            for ing in data["ingredients"]
        )
        st.markdown(f"```\n{mix}\nEffect: {data['effect']}\nCategory: {data['category']}\nDanger: {'★' * data['danger']} | Safety: {data['safety']}\nTotal Cost: {format_currency(total_cost)} ({total_cost} Bronze)\n\nIngredients:\n" +
                    "\n".join([f"- {ing}" for ing in data["ingredients"]]) + "\n```")
    elif choice:
        st.warning("Invalid selection.")

# === Category Search ===
elif st.session_state.page == "category":
    st.markdown("```\n-- CATEGORY LIST --\nChoose a number to view mixtures in that category or 'back'.\n```")
    categories = alchemy_data["categories"]
    for i, name in enumerate(categories, 1):
        st.markdown(f"{i}. {name}")
    choice = st.text_input("Category number or 'back':", key="cat_choice")

    if choice.lower() == "back":
        st.session_state.page = "main"
    elif choice.isdigit() and 1 <= int(choice) <= len(categories):
        selected = categories[int(choice) - 1]
        keyword = selected.lower().split()[0]
        matches = {k: v for k, v in alchemy_data["mixtures"].items() if keyword in v["category"].lower()}
        if not matches:
            st.warning("No mixtures found.")
        else:
            st.markdown("```\nMatching Mixtures:\n" + "\n".join([f"- {k}" for k in matches]) + "\n```")
    elif choice:
        st.warning("Invalid selection.")

# === Safety Search ===
elif st.session_state.page == "safety":
    st.markdown("```\n-- SAFETY LEVELS --\n1. Safe\n2. Mid\n3. Dangerous\nEnter a number or 'back'\n```")
    levels = ["Safe", "Mid", "Dangerous"]
    choice = st.text_input("Safety level number or 'back':", key="safe_choice")

    if choice.lower() == "back":
        st.session_state.page = "main"
    elif choice.isdigit() and 1 <= int(choice) <= 3:
        selected = levels[int(choice) - 1]
        matches = {k: v for k, v in alchemy_data["mixtures"].items() if v["safety"].lower() == selected.lower()}
        if not matches:
            st.warning("No mixtures found.")
        else:
            st.markdown("```\nMatching Mixtures:\n" + "\n".join([f"- {k}" for k in matches]) + "\n```")
    elif choice:
        st.warning("Invalid selection.")

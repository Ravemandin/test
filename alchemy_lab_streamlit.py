import streamlit as st

# Paste your full alchemy_data dictionary here
from updated_code_list import alchemy_data  # or paste the dict directly

# Set page config
st.set_page_config(page_title="Alchemy Lab", page_icon="🧪")

# Session state for navigation
if "menu" not in st.session_state:
    st.session_state.menu = "main"

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

st.title("if this fucking thing doesn't work im going to kms")

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
elif st.session_state.menu == "ingredients":
    ingredient = st.selectbox("Select an ingredient:", sorted(alchemy_data["ingredients"].keys()))
    data = alchemy_data["ingredients"][ingredient]
    st.markdown(f"### {ingredient}")
    st.markdown(f"**Price:** {data['price']} {data['currency']} ({convert_to_bronze(data['price'], data['currency'])} Bronze)")
    st.markdown(f"**Safety:** {data['safety']} | **Type:** {data['type']}")
    st.markdown("**States:**")
    st.markdown(f"- Natural: {data['states']['natural']}")
    st.markdown(f"- Heated: {data['states']['heated']}")
    st.markdown(f"- Frozen: {data['states']['frozen']}")
    st.button("Back", on_click=lambda: st.session_state.update({"menu": "main"}))

# === Mixtures ===
elif st.session_state.menu == "mixtures":
    mixture = st.selectbox("Select a mixture:", sorted(alchemy_data["mixtures"].keys()))
    data = alchemy_data["mixtures"][mixture]
    st.markdown(f"### {mixture}")
    st.markdown("**Ingredients:**")
    total_bronze = 0
    for ing in data["ingredients"]:
        ing_data = alchemy_data["ingredients"][ing]
        bronze = convert_to_bronze(ing_data["price"], ing_data["currency"])
        total_bronze += bronze
        st.markdown(f"- {ing}: {ing_data['price']} {ing_data['currency']} ({bronze} Bronze)")
    st.markdown(f"**Effect:** {data['effect']}")
    st.markdown(f"**Danger:** {'★' * data['danger']} | **Safety:** {data['safety']}")
    st.markdown(f"**Category:** {data['category']}")
    st.markdown(f"**Total Cost:** {format_currency(total_bronze)} ({total_bronze} Bronze)")
    st.button("Back", on_click=lambda: st.session_state.update({"menu": "main"}))

# === Search by Category ===
elif st.session_state.menu == "category":
    cat = st.selectbox("Choose a category:", alchemy_data["categories"])
    keyword = cat.lower().split()[0]
    matches = {k: v for k, v in alchemy_data["mixtures"].items() if keyword in v["category"].lower()}
    if matches:
        mix = st.selectbox("Select a mixture:", list(matches.keys()))
        data = matches[mix]
        st.markdown(f"### {mix}")
        total_bronze = sum(convert_to_bronze(alchemy_data["ingredients"][ing]["price"],
                                             alchemy_data["ingredients"][ing]["currency"])
                           for ing in data["ingredients"])
        st.markdown(f"**Effect:** {data['effect']}")
        st.markdown(f"**Danger:** {'★' * data['danger']} | **Safety:** {data['safety']}")
        st.markdown(f"**Total Cost:** {format_currency(total_bronze)} ({total_bronze} Bronze)")
    else:
        st.warning("No mixtures found in this category.")
    st.button("Back", on_click=lambda: st.session_state.update({"menu": "main"}))

# === Search by Safety Level ===
elif st.session_state.menu == "safety":
    level = st.selectbox("Choose a safety level:", ["Safe", "Mid", "Dangerous"])
    matches = {k: v for k, v in alchemy_data["mixtures"].items() if v["safety"].lower() == level.lower()}
    if matches:
        mix = st.selectbox("Select a mixture:", list(matches.keys()))
        data = matches[mix]
        st.markdown(f"### {mix}")
        total_bronze = sum(convert_to_bronze(alchemy_data["ingredients"][ing]["price"],
                                             alchemy_data["ingredients"][ing]["currency"])
                           for ing in data["ingredients"])
        st.markdown(f"**Effect:** {data['effect']}")
        st.markdown(f"**Category:** {data['category']}")
        st.markdown(f"**Danger:** {'★' * data['danger']} | **Safety:** {data['safety']}")
        st.markdown(f"**Total Cost:** {format_currency(total_bronze)} ({total_bronze} Bronze)")
    else:
        st.warning("No mixtures found at this safety level.")
    st.button("Back", on_click=lambda: st.session_state.update({"menu": "main"}))

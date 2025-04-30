import sys
# ALCHEMY DATABASE
alchemy_data = {
    "ingredients": {
        "Alchemical coral powder": {
            "price": 19, "currency": "Silver", "safety": "Safe", "type": "Mineral",
            "states": {
                "natural": "Seals wounds with crystalline film, leaves brittle scars",
                "heated": "Forms unbreakable glass when cooled",
                "frozen": "Explodes on contact with moisture"
            }
        },
        "Ancient Dragon's Heart Shard": {
            "price": 25, "currency": "Gold", "safety": "Dangerous", "type": "Mineral",
            "states": {
                "natural": "Pulses with latent energy, grants temporary fire resistance",
                "heated": "Melts into liquid dragonfire (burns eternally)",
                "frozen": "Shatters into cursed ice causing frostburn"
            }
        },
        "Ashen Bark Chips": {
            "price": 3, "currency": "Bronze", "safety": "Safe", "type": "Organic",
            "states": {
                "natural": "Repels insects when rubbed (produces harmless smoke)",
                "heated": "Burns indefinitely as an eternal ember",
                "frozen": "Induces prophetic visions when ingested (causes temporary blindness)"
            }
        },
        "Banshee Core": {
            "price": 22, "currency": "Gold", "safety": "Dangerous", "type": "Organic",
            "states": {
                "natural": "Cracks glass/mirrors with silent screams",
                "heated": "Releases deafening sonic shockwave",
                "frozen": "Forms paralyzing 'Wail Gem' when shattered"
            }
        },
        "Black Widow Queen Venom": {
            "price": 27, "currency": "Gold", "safety": "Dangerous", "type": "Organic",
            "states": {
                "natural": "One drop kills giants, diluted causes hallucinations",
                "heated": "Turns into heart-stopping adhesive",
                "frozen": "Becomes nerve-freezing Frost Venom"
            }
        },
        "Bloodgrass Stalks": {
            "price": 69, "currency": "Bronze", "safety": "Safe", "type": "Organic",
            "states": {
                "natural": "Boosts stamina but induces bloodthirst when chewed",
                "heated": "Ferments into vampiric healing tonic",
                "frozen": "Stops bleeding instantly (risk of thrombosis)"
            }
        },
        "Dragonflame Core": {
            "price": 11, "currency": "Gold", "safety": "Mid", "type": "Mineral",
            "states": {
                "natural": "Glows like hot coal, reignites extinguished fires",
                "heated": "Explodes like miniature sun",
                "frozen": "Becomes Frostflame Core (burns cold)"
            }
        },
        "Emberroot Chunks": {
            "price": 66, "currency": "Silver", "safety": "Mid", "type": "Organic",
            "states": {
                "natural": "Warms nearby area when placed",
                "heated": "Ignites into firestorm if uncontained",
                "frozen": "Grants cold resistance when chewed (chills heart)"
            }
        },
        "Firethorn Berry": {
            "price": 1, "currency": "Gold", "safety": "Mid", "type": "Organic",
            "states": {
                "natural": "Induces feverish energy when eaten",
                "heated": "Ferments into volatile explosive",
                "frozen": "Explodes on impact dealing fire+cold damage"
            }
        },
        "Flask of Vital Essence": {
            "price": 4, "currency": "Gold", "safety": "Dangerous", "type": "Organic",
            "states": {
                "natural": "Restores stamina but causes addiction",
                "heated": "Potent healing (regrows limbs over time)",
                "frozen": "Crystallizes into Life Shards (drains lifespan)"
            }
        },
        "Phoenix Feather": {
            "price": 2, "currency": "Gold", "safety": "Mid", "type": "Organic",
            "states": {
                "natural": "Can reignite extinguished flames",
                "heated": "Burns eternally (cannot be extinguished)",
                "frozen": "Deals both fire and ice damage"
            }
        },
        "Phoenix Tear": {
            "price": 5, "currency": "Gold", "safety": "Dangerous", "type": "Organic",
            "states": {
                "natural": "Resurrects if applied within 1 minute of death (burns user)",
                "heated": "Evaporates into healing cloud",
                "frozen": "Forms Rebirth Gem for delayed resurrection"
            }
        },
        "Trollblood Extracts": {
            "price": 53, "currency": "Silver", "safety": "Mid", "type": "Organic",
            "states": {
                "natural": "Accelerates healing (may grow extra limbs)",
                "heated": "Causes uncontrolled regeneration (tumor risk)",
                "frozen": "Grants regeneration but fire vulnerability"
            }
        }
    },
    "mixtures": {
        "Elixir of Supreme Restoration": {
            "ingredients": ["Phoenix Tear", "Trollblood Extracts", "Flask of Vital Essence"],
            "effect": "Full resurrection with flesh hunger (1d4 days)",
            "category": "healing",
            "danger": 4,
            "safety": "Dangerous"
        },
        "Dragon's Breath Elixir": {
            "ingredients": ["Dragonflame Core", "Firethorn Berry", "Emberroot Chunks"],
            "effect": "Grants fire breath (3d6 damage in 15-ft cone) for 1 minute",
            "category": "combat",
            "danger": 3,
            "safety": "Mid"
        }
    },
    "currency_rates": {
        "Gold": 10000,
        "Silver": 100,
        "Bronze": 1
    },
    "categories": [
        "Healing & Restoration",
        "Combat Enhancements",
        "Stealth & Illusion",
        "Curses & Hexes",
        "Elemental & Magical",
        "Summoning & Constructs",
        "Utility & Trickery",
        "Dangerous / Experimental",
        "Random & Bizarre"
    ]
}
# CORE FUNCTIONS
def clear_screen():
    """Clears the console screen"""
    print("\n" * 50)


def convert_to_bronze(amount, currency):
    """Convert any currency to bronze base value"""
    return amount * alchemy_data["currency_rates"][currency]

def format_currency(amount):
    """Convert bronze amount to optimal currency display"""
    gold = amount // 10000
    remainder = amount % 10000
    silver = remainder // 100
    bronze = remainder % 100

    parts = []
    if gold > 0:
        parts.append(f"{gold} Gold")
    if silver > 0:
        parts.append(f"{silver} Silver")
    if bronze > 0 or not parts:
        parts.append(f"{bronze} Bronze")
    return " ".join(parts)

def calculate_mixture_cost(mixture_name):
    """Calculate total cost of a mixture in bronze"""
    mixture = alchemy_data["mixtures"][mixture_name]
    total_bronze = 0
    for ingredient in mixture["ingredients"]:
        ing_data = alchemy_data["ingredients"][ingredient]
        total_bronze += convert_to_bronze(ing_data["price"], ing_data["currency"])
    return total_bronze

# DISPLAY FUNCTIONS
def display_ingredient(ingredient):
    data = alchemy_data["ingredients"][ingredient]
    clear_screen()
    print(f"\n=== {ingredient.upper()} ===")
    print(f"Price: {data['price']} {data['currency']} ({convert_to_bronze(data['price'], data['currency'])} Bronze)")
    print(f"Safety: {data['safety']} | Type: {data['type']}")

    print("\n=== STATES ===")
    print(f"[Natural] {data['states']['natural']}")
    print(f"[Heated]  {data['states']['heated']}")
    print(f"[Frozen]  {data['states']['frozen']}")

    input("\nPress Enter to continue...")

def display_mixture(mixture):
    data = alchemy_data["mixtures"][mixture]
    total_cost = calculate_mixture_cost(mixture)

    clear_screen()
    print(f"\n=== {mixture.upper()} ===")
    print("Ingredients:")
    for ing in data["ingredients"]:
        ing_data = alchemy_data["ingredients"][ing]
        print(
            f"  - {ing}: {ing_data['price']} {ing_data['currency']} ({convert_to_bronze(ing_data['price'], ing_data['currency'])} Bronze)")

    print(f"\nEffect: {data['effect']}")
    print(f"Total Cost: {format_currency(total_cost)} ({total_cost} Bronze)")
    print(f"Danger: {'★' * data['danger']} | Safety: {data['safety']}")
    print(f"Category: {data['category']}")
    input("\nPress Enter to continue...")

# MENU SYSTEM
def show_menu(title, options, back_option=True):
    clear_screen()
    print(f"\n=== {title.upper()} ===")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    if back_option:
        print(f"{len(options) + 1}. Back")

    while True:
        try:
            choice = input("\nSelect an option: ")
            if choice.lower() == 'q':
                return -1
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice - 1
            if back_option and choice == len(options) + 1:
                return -1
            print("Invalid choice. Try again.")
        except ValueError:
            print("Please enter a number.")

def ingredient_menu():
    ingredients = sorted(alchemy_data["ingredients"].keys())
    while True:
        choice = show_menu("Ingredients", ingredients)
        if choice == -1:
            return
        display_ingredient(ingredients[choice])

def mixture_menu():
    mixtures = sorted(alchemy_data["mixtures"].keys())
    while True:
        mixture_display = [f"{m} {'★' * alchemy_data['mixtures'][m]['danger']}" for m in mixtures]
        choice = show_menu("Mixtures", mixture_display)
        if choice == -1:
            return
        display_mixture(mixtures[choice])

def category_menu():
    while True:
        choice = show_menu("Categories", alchemy_data["categories"])
        if choice == -1:
            return

        selected_category = alchemy_data["categories"][choice].lower().split()[0]
        filtered = [m for m, data in alchemy_data["mixtures"].items()
                    if selected_category in data["category"].lower()]

        if not filtered:
            input("\nNo mixtures in this category! Press Enter to continue...")
            continue

        mix_display = [f"{m} {'★' * alchemy_data['mixtures'][m]['danger']}" for m in filtered]
        mix_choice = show_menu(alchemy_data["categories"][choice], mix_display)
        if mix_choice != -1:
            display_mixture(filtered[mix_choice])

def safety_menu():
    levels = ["Safe", "Mid", "Dangerous"]
    while True:
        choice = show_menu("Safety Levels", levels)
        if choice == -1:
            return

        filtered = [m for m, data in alchemy_data["mixtures"].items()
                    if data["safety"].lower() == levels[choice].lower()]

        if not filtered:
            input("\nNo mixtures at this safety level! Press Enter to continue...")
            continue

        safe_display = [f"{m} {'★' * alchemy_data['mixtures'][m]['danger']}" for m in filtered]
        safe_choice = show_menu(f"{levels[choice]} Mixtures", safe_display)
        if safe_choice != -1:
            display_mixture(filtered[safe_choice])

def main():
    while True:
        clear_screen()
        print("╔════════════════════════════╗")
        print("║        ALCHEMY LAB         ║")
        print("╚════════════════════════════╝")

        choice = show_menu("Main Menu", [
            "Browse Ingredients",
            "Browse Mixtures",
            "Search by Category",
            "Search by Safety Level",
            "Exit"
        ], back_option=False)

        if choice == 0:
            ingredient_menu()
        elif choice == 1:
            mixture_menu()
        elif choice == 2:
            category_menu()
        elif choice == 3:
            safety_menu()
        elif choice == 4 or choice == -1:
            sys.exit("Goodbye, Alchemist!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nExperiment terminated!")
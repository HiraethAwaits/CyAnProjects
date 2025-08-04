import random

# Tarot card data
tarot_deck = [
    {"name": "The Fool", "meaning": "New beginnings, Spontaneity, Innocence, Humor, Energy"},
    {"name": "The Magician", "meaning": "Manifestation, Power, Resourcefulness, Divine connection, Mastery"},
    {"name": "The High Priestess", "meaning": "Intuition, Mystery, The Subconscious, Intelligence, Wisdom"},
    {"name": "The Empress", "meaning": "Mother, Fertility, Pleasure, Beauty, Success"},
    {"name": "The Emperor", "meaning": "Authority, Stability, Leadership, Proficiency, Endurance"},
    {"name": "The Hierophant", "meaning": "Tradition, Convention, Symbolism, Religion, Morality"},
    {"name": "The Lovers", "meaning": "Love, Attraction, Harmony, Union, Virtue"},
    {"name": "The Chariot", "meaning": "Journey, Obstacle, Ambition, Conquest, Ordeal"},
    {"name": "Justice", "meaning": "Balance, Equality, Neutrality, Moderation, Integrity"},
    {"name": "The Hermit", "meaning": "Sage, Vigilance, Withdrawl, Contemplation, Safety"},
    {"name": "The Wheel of Fortune", "meaning": "Cycles of Life, Destiny, New Cycle, Success, Manifestation"},
    {"name": "Strength", "meaning": "Fortitude, Resilience, Resolve, Confidence, Resolve"},
    {"name": "The Hanged Man", "meaning": "Delay, Sacrifices, Review, Readjustment, Abandonment"},
    {"name": "Death", "meaning": "Alteration, Loss, Transformation, Boredom, Stagnation"},
    {"name": "Temperance", "meaning": "Moderation, Economy, Patience, Friendship, Self-control"},
    {"name": "The Devil", "meaning": "Magic, Strange occurrences, Fate, Prophecy, Catastrophe"},
    {"name": "The Tower", "meaning": "Disruption, Expulsion, Wrath, Punishment, Losses"},
    {"name": "The Star", "meaning": "Hope, Recovery, Gifts, Light, Prospects"},
    {"name": "The Moon", "meaning": "Twilight, Reflected light, Illusion, Uncertainty, Deception"},
    {"name": "The Sun", "meaning": "Peace, Contentment, Devotion, Joy, Pleasure"},
    {"name": "Judgement", "meaning": "Rebirth, Renewal, Rejuvenation, Result, Awakening"},
    {"name": "The World", "meaning": "Long Journey, Perfection, Completion, Reward, Conclusion"},

    # Minor Arcana
    # Starting with Cups
    {"name": "Ace of Cups", "meaning": ""},
    {"name": "Two of Cups", "meaning": ""},
    {"name": "Three of Cups", "meaning": ""},
    {"name": "Four of Cups", "meaning": ""},
    {"name": "Five of Cups", "meaning": ""},
    {"name": "Six of Cups", "meaning": ""},
    {"name": "Seven of Cups", "meaning": ""},
    {"name": "Eight of Cups", "meaning": ""},
    {"name": "Nine of Cups", "meaning": ""},
    {"name": "Ten of Cups", "meaning": ""},
    {"name": "Page of Cups", "meaning": ""},
    {"name": "Knight of Cups", "meaning": ""},
    {"name": "Queen of Cups", "meaning": ""},
    {"name": "King of Cups", "meaning": ""},
    #Second is Swords
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    {"name": "", "meaning": ""},
    # ... add more cards
]

# Card positions
card_positions = {
    1: "Past",
    2: "Present",
    3: "Future"
}

# Keywords for card interpretations
card_keywords = {
    "love": {"The Lovers", "The Empress", "The Two of Cups", "The Knight of Cups"},
    "career": {"The Emperor", "The Hierophant", "The Ten of Pentacles", "The Ace of Swords"},
    # ... add more keywords and associated cards
}

def generate_three_card_reading():
    # Shuffle the deck
    random.shuffle(tarot_deck)
    
    # Draw three cards for past, present, and future positions
    reading = {}
    for position, meaning in card_positions.items():
        card = tarot_deck.pop()
        reading[meaning] = {"card": card, "position": position}
    
    return reading

def generate_heart_reading():
    # Shuffle the deck
    random.shuffle(tarot_deck)
    
    # Draw three cards for the heart reading
    reading = {}
    for i in range(3):
        card = tarot_deck.pop()
        reading[f"Card {i+1}"] = {"card": card, "position": i+1}
    
    return reading

def generate_third_eye_reading():
    # Shuffle the deck
    random.shuffle(tarot_deck)
    
    # Draw three cards for the third eye reading
    reading = {}
    for i in range(3):
        card = tarot_deck.pop()
        reading[f"Insight {i+1}"] = {"card": card, "position": i+1}
    
    return reading

def interpret_tarot_reading(reading, topic="general"):
    interpretation = []
    for meaning, info in reading.items():
        card_name = info["card"]["name"]
        position = info["position"]
        
        # Customize interpretation based on topic
        if topic in card_keywords:
            relevant_cards = card_keywords[topic]
            if card_name in relevant_cards:
                interpretation.append(f"In the {position} position, {card_name} suggests {topic} opportunities.")
        
        # General interpretation
        interpretation.append(f"In the {position} position, {card_name} indicates {info['card']['meaning']}.")
    
    return "\n".join(interpretation)

# Get user input for the type of reading
user_input = input("Choose a Tarot reading type (Three Card Reading, Heart Reading, Third Eye Reading): ").lower()

# Validate user input and generate/interpret the reading accordingly
if user_input == "three card reading":
    reading = generate_three_card_reading()
    interpretation = interpret_tarot_reading(reading, topic="general")
    print(interpretation)
elif user_input == "heart reading":
    reading = generate_heart_reading()
    interpretation = interpret_tarot_reading(reading, topic="love")
    print(interpretation)
elif user_input == "third eye reading":
    reading = generate_third_eye_reading()
    interpretation = interpret_tarot_reading(reading, topic="insight")
    print(interpretation)
else:
    print("Invalid input. Please choose a valid Tarot reading type.")

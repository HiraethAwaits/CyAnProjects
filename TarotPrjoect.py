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
    {"name": "Ace of Cups", "meaning": "Cup overflows, Feelings, Pregnancy, Attraction, Creative beginnings"},
    {"name": "Two of Cups", "meaning": "Partnership, Couple, Soul Mate, Agreement, Teamwork"},
    {"name": "Three of Cups", "meaning": "Gathering, Social, Victory, Problems resolved, Group"},
    {"name": "Four of Cups", "meaning": "Boredom, Satiated, Preoccupation, Aversion, Disappointment"},
    {"name": "Five of Cups", "meaning": "Regret, Limited loss, Superficial relationships, Difficult relationships, Lacking"},
    {"name": "Six of Cups", "meaning": "Past connections, Childhood, Nostalgia, Renewal, New cycle"},
    {"name": "Seven of Cups", "meaning": "Not as it appears, Fantasies, Illusions, Corruption, Unrealistic expectations"},
    {"name": "Eight of Cups", "meaning": "Modesty, Decline, Letting go, Moving on, Abandoned plans"},
    {"name": "Nine of Cups", "meaning": "Abundance, Success, Wellbeing, Secure, Fulfillment"},
    {"name": "Ten of Cups", "meaning": "Joy, Pleasure in life, Peace, Loved, Ecstacy"},
    {"name": "Page of Cups", "meaning": "Helpful, Youthful, Studious, Affectionate, Meditative"},
    {"name": "Knight of Cups", "meaning": "Advancing, Reception, Proposition, Invitation, Financial opportunity"},
    {"name": "Queen of Cups", "meaning": "Mature, Honesty, Devoted, Wise, Visionary"},
    {"name": "King of Cups", "meaning": "Responsible, Honest, Educated, Professional, Kind"},

    #Second is Swords
    {"name": "Ace of Swords", "meaning": ""},
    {"name": "Two of Swords", "meaning": ""},
    {"name": "Three of Swords", "meaning": ""},
    {"name": "Four of Swords", "meaning": ""},
    {"name": "Five of Swords", "meaning": ""},
    {"name": "Six of Swords", "meaning": ""},
    {"name": "Seven of Swords", "meaning": ""},
    {"name": "Eight of Swords", "meaning": ""},
    {"name": "Nine of Swords", "meaning": ""},
    {"name": "Ten of Swords", "meaning": ""},
    {"name": "Page of Swords", "meaning": ""},
    {"name": "Knight of Swords", "meaning": ""},
    {"name": "Queen of Swords", "meaning": ""},
    {"name": "King of Swords", "meaning": ""},

    #Third is Wands
    {"name": "Ace of Wands", "meaning": ""},
    {"name": "Two of Wands", "meaning": ""},
    {"name": "Three of Wands", "meaning": ""},
    {"name": "Four of Wands", "meaning": ""},
    {"name": "Five of Wands", "meaning": ""},
    {"name": "Six of Wands", "meaning": ""},
    {"name": "Seven of Wands", "meaning": ""},
    {"name": "Eight of Wands", "meaning": ""},
    {"name": "Nine of Wands", "meaning": ""},
    {"name": "Ten of Wands", "meaning": ""},
    {"name": "Page of Wands", "meaning": ""},
    {"name": "Knight of Wands", "meaning": ""},
    {"name": "Queen of Wands", "meaning": ""},
    {"name": "King of Wands", "meaning": ""},

    #Last is Coins
    {"name": "Ace of Coins", "meaning": ""},
    {"name": "Two of Coins", "meaning": ""},
    {"name": "Three of Coins", "meaning": ""},
    {"name": "Four of Coins", "meaning": ""},
    {"name": "Five of Coins", "meaning": ""},
    {"name": "Six of Coins", "meaning": ""},
    {"name": "Seven of Coins", "meaning": ""},
    {"name": "Eight of Coins", "meaning": ""},
    {"name": "Nine of Coins", "meaning": ""},
    {"name": "Ten of Coins", "meaning": ""},
    {"name": "Page of Coins", "meaning": ""},
    {"name": "Knight of Coins", "meaning": ""},
    {"name": "Queen of Coins", "meaning": ""},
    {"name": "King of Coins", "meaning": ""},
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

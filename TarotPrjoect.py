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
    {"name": "Ace of Swords", "meaning": "Truth, Courage, Vision, Insight, Power"},
    {"name": "Two of Swords", "meaning": "Stalemate, Conformity, Inner Conflict, Duplicity, Disloyalty"},
    {"name": "Three of Swords", "meaning": "Disruptive forces, Incompatibility, Heartache, Distance, Absence"},
    {"name": "Four of Swords", "meaning": "Mental security, Retreat, Rest, Peace, Good ideas"},
    {"name": "Five of Swords", "meaning": "Brute force, Self-knowledge, Learning from mistakes, Persistence, Possible loss"},
    {"name": "Six of Swords", "meaning": "Journey, Moving towards better times, Messenger, Attention, Recovery"},
    {"name": "Seven of Swords", "meaning": "Cunning, Determination, Escape from bad circumstances, Backfiring manipulation, Treachery"},
    {"name": "Eight of Swords", "meaning": "Contradiction, Criticism, Reprimand, Crisis, Blame"},
    {"name": "Nine of Swords", "meaning": "Third eye, Good faith, Busy mind, Integrity, Suspicion"},
    {"name": "Ten of Swords", "meaning": "Affliction, Sadness, Grief, Pain, Difficulties"},
    {"name": "Page of Swords", "meaning": "Spy, Intelligence, Vigilance, Examination, Indiscretion"},
    {"name": "Knight of Swords", "meaning": "Brave, Defender, Skillful, Astute, Attractive"},
    {"name": "Queen of Swords", "meaning": "Fault-Finding, Belittling, Inner fragility, Widow, Barren"},
    {"name": "King of Swords", "meaning": "Authority, Power, Advisor, Justice, Fairness"},

    #Third is Wands
    {"name": "Ace of Wands", "meaning": "Birth, Force, First Fruits, Progress, Invention"},
    {"name": "Two of Wands", "meaning": "Restlessness, Boredom, Dissatisfaction, Restraint, Co-Dependency"},
    {"name": "Three of Wands", "meaning": "Business success, Busy, Ceasefire, Troubles ending, Strength"},
    {"name": "Four of Wands", "meaning": "Peace, Rest, Celebration, Joyful outcome, Harmony"},
    {"name": "Five of Wands", "meaning": "Competition, Conflicting opinion, Too many choices, Accommodation, Acting"},
    {"name": "Six of Wands", "meaning": "Good news, Victory, Fulfillment, Honor, Success"},
    {"name": "Seven of Wands", "meaning": "Bravery, Overcoming, Advantage, Integrity, Resolution"},
    {"name": "Eight of Wands", "meaning": "Progress, Breakthrough, Threshold, Promises, Proposals"},
    {"name": "Nine of Wands", "meaning": "Stamina, Discipline, Healing, Preparation, Strength"},
    {"name": "Ten of Wands", "meaning": "Honors but at a price, Fulfilling obligations, Striving, Precarious, Pressure"},
    {"name": "Page of Wands", "meaning": "News, Messages, Courageous, Loyal, Trusted"},
    {"name": "Knight of Wands", "meaning": "Travel, Departure, Altered Plans, Moving abroad, Away"},
    {"name": "Queen of Wands", "meaning": "Charming, Magnetic, Loving, Honorable, Practical"},
    {"name": "King of Wands", "meaning": "Wise, Conscientious, Educated, Mediator, Devoted"},

    #Last is Coins
    {"name": "Ace of Coins", "meaning": "Treasure, Riches, Attainment, Recognition, Contentment"},
    {"name": "Two of Coins", "meaning": "Flow of money, Obtaining money, Getting what you pay for, Fluctuations, On-going work"},
    {"name": "Three of Coins", "meaning": "Mastery, Reputation, Experience, Craftmanship, High status"},
    {"name": "Four of Coins", "meaning": "Inheritance, Gift, Status through wealth, Financial protection, Insurance"},
    {"name": "Five of Coins", "meaning": "Material struggle, Health struggle, Over-spending, Loss, Disadvantage"},
    {"name": "Six of Coins", "meaning": "Good Finances, Caring acts, Generosity, Charity, Benefactor"},
    {"name": "Seven of Coins", "meaning": "Profit, Growth, Assets, Learning curve, Labor"},
    {"name": "Eight of Coins", "meaning": "Apprenticeship, Employment, Commission, Planning, Calculating"},
    {"name": "Nine of Coins", "meaning": "Material comfort, Abundance, Little want, Accomplishment, Honors"},
    {"name": "Ten of Coins", "meaning": "Wealth, Security, Gain, Height of success, Posterity"},
    {"name": "Page of Coins", "meaning": "Study, Meditation, Concentration, Rule, Instruction"},
    {"name": "Knight of Coins", "meaning": "Trustworthy, Methodical, Reliable, Decency, Patience"},
    {"name": "Queen of Coins", "meaning": "Opulence, Generosity, Luxury, Assurance, Grace"},
    {"name": "King of Coins", "meaning": "Master, Valor, Intelligent, Victory, Bravery"},
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
    
    # Draw six cards for the heart reading
    reading = {}
    for i in range(6):
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

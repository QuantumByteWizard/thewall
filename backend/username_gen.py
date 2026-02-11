import random

ADJECTIVES = [
    "Radiant", "Happy", "Caring", "Gentle", "Brave", "Bright", "Calm", "Cheery",
    "Creative", "Dazzling", "Eager", "Fantastic", "Friendly", "Generous", "Gifted",
    "Glowing", "Graceful", "Helpful", "Hopeful", "Jolly", "Joyful", "Kind", "Lively",
    "Lucky", "Magic", "Merry", "Nice", "Optimistic", "Peaceful", "Playful", "Polite",
    "Positive", "Precious", "Proud", "Quiet", "Ready", "Reliable", "Safe", "Secure",
    "Silly", "Sincere", "Skilled", "Smart", "Smiling", "Special", "Splendid", "Sunny",
    "Super", "Sweet", "Talented", "Thankful", "Thoughtful", "Trusting", "Truthful",
    "Unique", "Upbeat", "Warm", "Wise", "Wonderful", "Worthy", "Zealous"
]

NOUNS = [
    "Dreamer", "Wanderer", "Thinker", "Artist", "Friend", "Guide", "Helper", "Hero",
    "Hope", "Joy", "Leader", "Light", "Love", "Maker", "Muse", "Optimist", "Partner",
    "Pathfinder", "Peacemaker", "Philosopher", "Pioneer", "Poet", "Protector", "Seeker",
    "Soul", "Spark", "Spirit", "Star", "Storyteller", "Sunbeam", "Support", "Teacher",
    "Traveler", "Visionary", "Volunteer", "Wish", "Writer", "Angel", "Beacon", "Bird",
    "Bloom", "Blossom", "Breeze", "Butterfly", "Cloud", "Dawn", "Dew", "Dove", "Flower",
    "Forest", "Garden", "Gem", "Glow", "Grove", "Harmony", "Heart", "Hill", "Island",
    "Jewel", "Leaf", "Meadow", "Melody", "Moon", "Mountain", "Music", "Nature", "Ocean",
    "Pearl", "Petal", "Rainbow", "Ray", "River", "Rose", "Sea", "Seed", "Sky", "Song",
    "Spring", "Stream", "Sunrise", "Sunset", "Tree", "Valley", "Voice", "Water", "Wave",
    "Wind", "Wing"
]

def generate_username():
    """Generates a random creative username."""
    adj = random.choice(ADJECTIVES)
    noun = random.choice(NOUNS)
    return f"{adj} {noun}"

if __name__ == "__main__":
    print(generate_username())

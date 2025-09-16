import random

subjects = [
    "sharukh khan",
    "virat kohli",
    "nirmala sitharaman",
    "A mumbai cat",
    "A group of monkey",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from delhi"
]

actions = [
    "launches",
    "cancels",
    "dance with",
    "eats",
    "delivers an on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at red fort",
    "in mumbai local train",
    "a plate of samosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "at india gate"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"🔴 BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day!")

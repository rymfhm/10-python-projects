#string concatenation
coder = "Student"

print("I am a " + coder)
print("I am a {}".format(coder))
print(f"I am a {coder}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
famous_person = input("Famous person: ")
madlib = f"I am a {coder} who is such a {adj} and requires {verb1}"
print(madlib)

import random

class Madlib:
    def __init__(self):
        self.categories = {
            "noun": ["dog", "city", "mountain", "ocean", "dream"],
            "verb": ["run", "swim", "fly", "dream", "dance"],
            "adjective": ["beautiful", "serene", "chaotic", "colorful", "gloomy"],
            "adverb": ["quickly", "gracefully", "wildly", "silently", "joyfully"],
            "place": ["Paris", "the jungle", "Mars", "a haunted house", "the library"],
            "person": ["a pirate", "an astronaut", "a teacher", "a wizard", "a detective"]
        }

        self.templates = [
            "Once upon a time, {person} went to {place} to {verb}. It was a {adjective} day, and everyone was {verb}-ing {adverb}.",
            "In the {adjective} {place}, {person} found a {noun} that could {verb}. This made everyone feel {adjective}.",
            "Every morning, {person} would {verb} {adverb} in the {adjective} {place}, dreaming of a {noun}.",
            "The {noun} decided to {verb} {adverb} because it wanted to impress {person} at {place}."
        ]

    def custom_madlib(self):
        print("Custom Madlib Project:")

        user_inputs = {
            "noun": input("Enter a noun: "),
            "verb": input("Enter a verb: "),
            "adjective": input("Enter an adjective: "),
            "adverb": input("Enter an adverb: "),
            "place": input("Enter a place: "),
            "person": input("Enter a person (e.g., a pirate, a doctor): ")
        }

        template = random.choice(self.templates)
        madlib = template.format(**user_inputs)

        return madlib



madlib_game = Madlib()
print(madlib_game.custom_madlib())
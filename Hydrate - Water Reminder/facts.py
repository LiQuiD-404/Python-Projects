# facts is a list that contains facts about water
import random

facts = [
    "There is the same amount of water on Earth as there was when the Earth was formed. The water from your "
    "faucet could contain molecules that dinosaurs drank.",
    "Nearly 97% of the world’s water is salty or otherwise undrinkable. Another 2% is locked in ice caps and "
    "glaciers. That leaves just 1% for all of humanity’s needs — all its agricultural, residential, manufacturing, "
    "community, and personal needs. ",
    "75% of the human brain is water and 75% of a living tree is water.",
    "A person can live about a month without food, but only about a week without water.",
    "Water expands by 9% when it freezes. Frozen water (ice) is lighter than water, which is why ice floats in water.",
    "Water regulates the Earth’s temperature. It also regulates the temperature of the human body, carries nutrients "
    "and oxygen to cells, cushions joints, protects organs and tissues, and removes wastes. ",
    "780 million people lack access to an improved water source.",
    "A jellyfish and a cucumber are each 95% water.",
    "80% of all illness in the developing world is water related.",
    "Up to 50% of water is lost through leaks in cities in the developing world.",
    "85% of the world population lives in the driest half of the planet.",
    "300 tons of water are required to manufacture 1 ton of steel.",  # 12
    "In a 100-year period, a water molecule spends 98 years in the ocean, 20 months as ice, about 2 weeks in lakes "
    "and rivers, and less than a week in the atmosphere. ",
    "A leaky faucet that drips at the rate of one drip per second can waste more than 3,000 gallons per year."
]


# random function to output a random fact out of the whole list
def fact_random():
    r = random.randint(0, 13)
    fct = facts[r]
    return fct



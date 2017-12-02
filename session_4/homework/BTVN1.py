inventory ={
"gold": 500,
"pounch": ["flint", "twine", "gemstone"],
"backpack": ["xylophone", "dagger", "bedroll", "bread loaf"],

}

inventory["pocket"] = "key"
print(inventory)

inventory["pocket"] = "seashell", "strange berry", "lint"
print(inventory)

inventory["backpack"].remove("dagger")
print(inventory)

inventory["gold"] += 50
print(inventory)

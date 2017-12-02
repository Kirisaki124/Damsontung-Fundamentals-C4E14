# tuananh = ["Tuan Anh", 22, "Moc Chau", 2, True, 4, 20]

# tuananh = {
#
# }

# tuananh = {
#     "name": "Tuan Anh"
# }

tuananh={
    "name": "Tuan Anh",
    "age": 22,
    "home": "Moc Chau",
    "in_relationship": True,
    "projects": 4,
}

print(tuananh["in_relationship"])

#
# tuananh["in_relationship"] = False
# print(tuananh["in_relationship"])

tuananh["projects"] += 1
print(tuananh)


tuananh["extra_hour"] = 20
print(tuananh)

del tuananh["in_relationship"]
print(tuananh)

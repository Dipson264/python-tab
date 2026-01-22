Field = {
    "first_row": ["00", "01", "02"],
    "Horn":50901
}

# print(Field.items())
# print(Field.keys())
# print(Field.values())



Field.update({"Horn":100,"Finger":200})
print(Field.get("Horn"))
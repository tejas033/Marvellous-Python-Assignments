# Dictionary

data = {"Name":"Let us C", "Author":"Y Kanetkar", "Price":340, "Publication":"BPB Publication", 0:"asdf"}

print("Loop to display keys")
for value in data:
    print(value)

print("Loop to display value")
for value in data.values():
    print(value)

print("Loop to display value using key")
for value in data:
    print(data[value])

print("Loop to display key & value :: ")
for key,value in data.items():
    print("key: ", key, ":: value: ", value)
import os

# Read File names in ../Items
item_files = os.listdir('../DungeonHouse\\Items')
# Grab ItemValue script
item_value_script = ""
with open("../DungeonHouse\\Shops\\GetItemValue.htsl", "r") as f:
    item_value_script = f.read()

for file_name in item_files:
    if file_name.endswith(".json"):
        item_name = file_name[:-5]

        if item_name in item_value_script:
            continue

        if item_name != item_name.lower():
            continue
    
        if item_name == "placeholder":
            continue

        if any(char.isdigit() for char in item_name):
            continue
        

        print(f"Adding {item_name} to GetItemValue.htsl")
        item_value_script += f'\nif (hasItem "../Items/{item_name}" metadata "Hand" anyAmount) {{\n    var "item_value" set 1\n    exit\n}}'

# Write back to GetItemValue.htsl
with open("../DungeonHouse\\Shops\\GetItemValue.htsl", "w") as f:
    f.write(item_value_script)
    print("Updated GetItemValue.htsl")

inventory = {
    "pen": 10,
    "notebook": 5,
    "eraser": 3
}

inventory["pen"] = 8
inventory["marker"] = 12
del inventory["eraser"]

print(inventory)
print(f"남은 항목 수: {len(inventory)}")
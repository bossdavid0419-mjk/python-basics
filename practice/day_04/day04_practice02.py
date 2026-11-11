current_slot = 0

while current_slot < 5:
    current_slot += 1  # CRUCIAL: Increment happens right at the start of the lap

    if current_slot == 3:
        print(f"Skipping item slot {current_slot}.")
        continue  # Aborts the rest of this lap and jumps back to the top

    # This processing code is skipped when current_slot is 3
    print(f"Successfully processed item in slot {current_slot}.")

print("Inventory scan complete!")
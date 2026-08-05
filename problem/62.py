def calculate_speeding_fine(speed: float, speed_limit: float) -> str:
    over = speed - speed_limit
    if over <= 0:
        return "No fine."
    # Fine tiers (over the limit)
    if 0 <= over <= 40:
        fine = 500
    elif 41 <= over <= 60:
        fine = 1000
    elif 61 <= over <= 80:
        fine = 1500
    elif over > 80:
        fine = 2000
    else:
        # No fine for small exceedances as per specification
        return "No fine."
    return f"Fine: {fine:,} Baht."
# Examples
print(calculate_speeding_fine(150.0, 60.0)) # over = 90 -> Fine: 500 Baht.
print(calculate_speeding_fine(200.0, 60.0)) # over = 140 -> Fine: 1,000 Baht.
print(calculate_speeding_fine(50.0, 60.0))
print(calculate_speeding_fine(70,60)) # No fine.

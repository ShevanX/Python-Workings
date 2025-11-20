def day_of_week(day):
    match (day):
        case 1:
            return "Its monday"
        case 2:
            return "Its tuesday"
        case 3:
            return "Its wednesday"
        case 4:
            return "Its thursday"
        case 5:
            return "Its friday"
        case 6:
            return "Its saturday"
        case 7:
            return "Its sunday"
        case _:
            return "Not a valid date"

def is_weekend(date):
    match (date):
        case "saturday" | "sunday":
            return "It is a weekend"
        case _:
            return "Not a weekend"

print(day_of_week(8))
print(is_weekend("tuesday"))


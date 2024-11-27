import csv

def load_data(filepath):
    """Load relatives' data from a CSV file."""
    relatives = []
    with open(filepath, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            relatives.append({
                "name": row["Name"].strip(),
                "coords": (float(row["Latitude"]), float(row["Longitude"])),
            })
    print("io_utils module loaded successfully!") 
    return relatives


def map_number_to_relative(number, relatives):
    """Map a number to the corresponding relative name."""
    try:
        # Convert number to integer and map to relative name
        number = int(number)
        if 1 <= number <= len(relatives):
            return relatives[number - 1]["name"]
        else:
            raise ValueError("Invalid number. Please enter a valid relative number.")
    except ValueError:
        # If input is not a valid integer, assume it's already a relative name
        return number




def get_user_input(relatives):
    """Prompt the user for route preferences."""
    print("Relatives Mapping:")
    for idx, relative in enumerate(relatives, start=1):
        print(f"{idx}: {relative['name']}")

    start = input("Enter the starting relative (number or name): ").strip()
    end = input("Enter the destination relative (number or name): ").strip()
    criterion = input("Optimization criterion (time/cost): ").strip().lower()

    # Map numbers to relative names if necessary
    start = map_number_to_relative(start, relatives)
    end = map_number_to_relative(end, relatives)

    if criterion not in ["time", "cost"]:
        raise ValueError("Invalid criterion. Choose 'time' or 'cost'.")
    return start, end, criterion



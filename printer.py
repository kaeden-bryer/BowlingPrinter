# Automatically re-generates the list of free agents and lanes

lanes = [
    ["Kaeden", "Julia", "Charlie", "Gavin"],
    ["Abby", "Matt", "liam", "John"]
]

free_agents = [
    "Sophia",
    "Emily",
    "Christian",
    "Yuvi",
    "Sun"
]

def generate():
    counter = 1
    counter = print_lanes(counter)
    counter = print_free_agents(counter)

def print_lanes(counter):
    print("Lanes:")
    for lane in enumerate(lanes):
        print("Lane", lane[0] + 1)
        for person in lane[1]:
            print(str(counter) + ". " + person)
            counter += 1
        print("\n")
    return counter

def print_free_agents(counter):
    print("Free Agents:")
    for person in free_agents:
        print(str(counter) + ". " + person)
        counter += 1
    return counter

generate()
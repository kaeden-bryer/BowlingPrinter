import json

with open("input.json", "r") as file:
    data = json.load(file)

lanes = data["Lanes"]
free_agents = data["Free_Agents"]

end_tokens = {
    6: "✅",
    5: "🟢",
    4: "🟠",
    3: "🟠",
    2: "⚠️",
    1: "⚠️"
}

def generate():
    with open("output.txt", "w") as output:
        counter = 1
        counter = print_lanes(counter, output)
        counter = print_free_agents(counter, output)

def print_lanes(counter, output):
    output.write("Lanes:\n")
    for lane in enumerate(lanes):
        slots_filled = len(lane[1])
        end_token = end_tokens[slots_filled]
        output.write(f"Lane {lane[0] + 1} –– " + lane[1][0] + f" ({slots_filled}/6 filled) {end_token}\n")
        for person in lane[1]:
            output.write(f"{counter}. {person}\n")
            counter += 1
        output.write("\n")
    return counter

def print_free_agents(counter, output):
    output.write("Free Agents:\n")
    for person in free_agents:
        output.write(f"{counter}. {person}\n")
        counter += 1
    return counter



generate()
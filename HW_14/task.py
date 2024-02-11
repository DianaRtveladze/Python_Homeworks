import json

def write_to_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def read_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def update_file_content(filename, updated_data):
    existing_data = read_from_file(filename)
    existing_data.extend(updated_data)
    write_to_file(filename, existing_data)


def add_to_file(filename, new_data):
    existing_data = read_from_file(filename)
    existing_data.extend(new_data)
    write_to_file(filename, existing_data)


file_name = 'chess_players.json'
chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]
write_to_file(file_name, chess_players)

data_from_file = read_from_file(file_name)
print("Data from file:")
print(data_from_file)

new_data = [
    {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
    {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
]
update_file_content(file_name, new_data)

updated_data_from_file = read_from_file(file_name)
print("\nUpdated Data from file:")
print(updated_data_from_file)

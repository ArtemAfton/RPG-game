import json




def load_user_data_rpg(data_path_rpg):
    try:
        with open(data_path_rpg, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data_rpg(user_data_rpg, data_path_rpg):
    with open(data_path_rpg, 'w+', encoding='utf8') as file:
        json.dump(user_data_rpg, file, ensure_ascii=False)



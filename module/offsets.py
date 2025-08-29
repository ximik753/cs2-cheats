# Offsets dumped by: https://github.com/a2x/cs2-dumper

from requests import get

# Сгенерировано нейронкой, поэтому метод не универсален
# Если искомый атрибут не уникальный, возвращает первое совпадение
# Во всех других случаях находит нужный элемент
def find_value_with_path_element(data, target_key, current_path=""):
    if isinstance(data, dict):
        for key, value in data.items():
            new_path = f"{current_path}:{key}" if current_path else key
            if key == target_key:
                return (new_path, value)
            if isinstance(value, (dict, list)):
                result = find_value_with_path_element(value, target_key, new_path)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for index, item in enumerate(data):
            new_path = f"{current_path}[{index}]"
            result = find_value_with_path_element(item, target_key, new_path)
            if result is not None:
                return result
    return None

def make_entry(obj, data, key):
    value = find_value_with_path_element(data, key)
    if value:
        setattr(obj, key, value)
    else:
        exit("Error: Key \"%s\" does not found. Check cs2-dumper." % (key))

class Offsets:
    pass

try:
    offset = get("https://raw.githubusercontent.com/a2x/cs2-dumper/refs/heads/main/output/offsets.json").json()
    client = get("https://raw.githubusercontent.com/a2x/cs2-dumper/refs/heads/main/output/client_dll.json").json()

    make_entry(Offsets, offset, "dwEntityList")
    make_entry(Offsets, offset, "dwViewMatrix")
    make_entry(Offsets, offset, "dwLocalPlayerPawn")
    make_entry(Offsets, offset, "dwLocalPlayerController")
    make_entry(Offsets, client, "m_iszPlayerName")
    make_entry(Offsets, client, "m_iHealth")
    make_entry(Offsets, client, "m_iTeamNum")
    make_entry(Offsets, client, "m_vOldOrigin")
    make_entry(Offsets, client, "m_pGameSceneNode")
    make_entry(Offsets, client, "m_hPlayerPawn")
    make_entry(Offsets, client, "m_iIDEntIndex")
    make_entry(Offsets, client, "m_vecViewOffset")
except:
    exit("Error: Invalid offsets, wait for an update")

from data import data


def resolve_structure(input_data):
    """
    create a dict for any type of input data
    """
    if isinstance(input_data, list):
        return {index: value for index, value in enumerate(input_data)}
    if isinstance(input_data, dict):
        return input_data


def resolve_node_index_formatting(node_index):
    if isinstance(node_index, str):
        return f'["{node_index}"]'
    if isinstance(node_index, int):
        return f'[{node_index}]'


def find_element_path(input_data, element, path, paths_list):
    input_data = resolve_structure(input_data)

    for index, value in input_data.items():
        this_path = path + resolve_node_index_formatting(index)
        if isinstance(value, (str, int, float, bool)):
            if value == element:
                paths_list.append(this_path)
        elif isinstance(value, (dict, list)):
            find_element_path(
                input_data=value,
                element=element,
                path=this_path,
                paths_list=paths_list
            )
    return paths_list


assert find_element_path(data, 'bazinga', 'tree', []) == [
    'tree["lose"]["muscle"][0]["orange"][0]["different"]["cap"]'
]
assert len(find_element_path(data, True, 'tree', [])) == 9
assert find_element_path(data, 42, 'tree', []) == [
    'tree["lose"]["muscle"][0]["orange"][0]["different"]["slabs"][1]["tomorrow"]'
]

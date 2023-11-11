def value_exists(input_dict: dict[str, int], input_int: int) -> bool:
    for key in input_dict: 
        if input_dict[key] == input_int:
            return True
    return False
"""Dictionary related utility functions."""

__author__ = "730663941"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Given a dictionary, returns another dictionary that inverts the keys and the values. The keys of the input list becomes the values of the output list and vice versa."""
    inverted_dict: dict[str, str] = {}
    for key in dictionary:
        if dictionary[key] in inverted_dict:
            raise KeyError("Error: Duplicate Key Found!")
        inverted_dict[dictionary[key]] = key
    return inverted_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Takes as input a dictionary of names and favorite colors. It returns a string which is the color that appears most frequently."""
    counter: dict[str, int] = {}
    for key in input_dict:
        if input_dict[key] not in counter:
            counter[input_dict[key]] = 1
        else:
            counter[input_dict[key]] += 1
    high_count: int = 0
    high_color: str = ""
    for key2 in counter: 
        if counter[key2] > high_count:
            high_count = counter[key2]
            high_color = key2
    return high_color


def count(input_list: list[str]) -> dict[str, int]:
    """Given a list, this function will produce a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    final_dict: dict[str, int] = {}
    for item in input_list:
        if item not in final_dict:
            final_dict[item] = 1
        else:
            final_dict[item] += 1
    return final_dict


def alphabetizer(word_list: list[str]) -> dict[str, list[str]]:
    """Given a list of words, this function will produce a dictionary where each key is a unique letter in the alphabet and each value is a list of the words that begin with that letter."""
    output_dict: dict[str, list[str]] = {}
    for word in word_list:
        letter = word[0].lower()
        if letter not in output_dict:
            output_dict[letter] = [word]
        else:
            output_dict[letter].append(word)
    return output_dict


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Given a dictionary of an initial attendance, it will update the attendance based on a given day of the week and a given student who attended on that day of the week."""
    if day not in log:
        log[day] = [student]
    else:  
        for x in range(len(log[day])): 
            if student == log[day][x]:
                return log
        log[day].append(student)
    return log

def short_words(input_list: list[str]) -> list[str]:
    output_list: list[str] = []
    for word in input_list: 
        if len(word) < 5:
            output_list.append(word)
        else:
            print(f"{word} is too long!")
    return output_list

my_list : list [str ] = ["sun", "cloud", "sky"]
print(short_words(my_list))
def odd_and_even(input_list: list[int]) -> list[int]:
    output_list: list[int] = []
    for num in range(len(input_list)):
        if input_list[num] % 2 == 1:
            if num % 2 == 0:
                output_list.append(input_list[num])
    return output_list


def remove_duplicates(data_list):
    unique_list = []

    for item in data_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


def strip_whitespaces(string_list):
    cleaned = []

    for s in string_list:
        cleaned.append(s.strip())

    return cleaned
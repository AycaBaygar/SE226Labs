from data_package import remove_duplicates, strip_whitespaces, calculate_mean, find_maximum, find_minimum


def main():
    user_input = input("Enter a comma-separated list of numbers (e.g., 12, 5, 12, 8 , 21): ")

    try:
        raw_list = user_input.split(",")
        stripped_list = strip_whitespaces(raw_list)

        num_list = []
        for item in stripped_list:
            if item != "":
                num_list.append(float(item))

        unique_list = remove_duplicates(num_list)
        print(f"Cleaned and unique data: {unique_list}")
        print("--------------------")
        print(f"Mean: {calculate_mean(unique_list):.2f}")
        print(f"Maximum: {find_maximum(unique_list)}")


    except ValueError:
        print("Data Error: Please make sure you only enter numbers separated by commas.")


if __name__ == "__main__":
    main()
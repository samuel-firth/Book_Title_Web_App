FILEPATH = 'titles.txt'


def get_titles(filepath=FILEPATH):
    """ Read a text file to return the list of Titles """
    with open(filepath, 'r') as file_local:
        titles_local = file_local.readlines()
    return titles_local


def write_titles(title_arg, filepath=FILEPATH):
    """ Write over text file with updated list of Titles """
    with open(filepath, 'w') as file_local:
        file_local.writelines(title_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_titles())


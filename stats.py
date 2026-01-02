def count_words(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        return len(words)
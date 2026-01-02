from stats import count_words
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    print(generate_report(file_path))

def print_text(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        return content
    
def character_count(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        char_count = {}
        for char in content:
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        return char_count
    
def generate_report(file_name):
    words = count_words(file_name)
    char_count = character_count(file_name)

    sorted_items = sorted(char_count.items(), key=lambda kv: kv[1], reverse=True)

    report = f"============ BOOKBOT ============\n" 
    report += f"Analyzing book found at {file_name}...\n"
    report += f"----------- Word Count ----------\n"
    report += f"Found {words} total words\n"
    report += f"--------- Character Count -------\n"
    for char, count in sorted_items:
        report += f"{char}: {count}\n"
    report += f"============= END ==============="

    return report
    

main()
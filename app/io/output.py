def write_to_console(text):
    """
    Prints the given text to the console.
    """
    print(text)

def write_to_file(text, filepath):
    """
    Writes text to a file using built-in open().
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

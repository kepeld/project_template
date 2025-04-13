def read_from_console():
    """
    Reads text input from the console.
    """
    return input("Enter some text: ")

def read_from_file(filepath):
    """
    Reads plain text from a file using built-in open().
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def read_with_pandas(filepath):
    """
    Reads a CSV file using pandas and returns a DataFrame.
    """
    import pandas as pd
    return pd.read_csv(filepath)

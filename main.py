from app.io.input import read_from_console, read_from_file, read_with_pandas
from app.io.output import write_to_console, write_to_file

def main():
    text1 = read_from_console()
    text2 = read_from_file("data/input.txt")
    df = read_with_pandas("data/input.csv")

    write_to_console(text1)
    write_to_console(text2)
    write_to_console(df.to_string())

    write_to_file(text1 + "\n" + text2 + "\n" + df.to_string(), "data/output.txt")

if __name__ == "__main__":
    main()

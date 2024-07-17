def main() -> None:
    file_name = input("Enter name of the file: ") + ".txt"
    file_lines = []
    while True:
        new_line = input("Enter new line of content: ")
        if new_line == "stop":
            break
        file_lines.append(new_line)
    with open(file_name, "w") as f:
        for file_line in file_lines:
            f.write(file_line + "\n")


if __name__ == "__main__":
    main()

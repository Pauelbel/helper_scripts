def read_file(file_name):
    """генератор для чтения файла"""

    with open(file_name) as file:
        for row in file:
            yield row


def find_errors(read_file):
     for row in read_file(
        "/home/apollon4eg/Repositories/helper_scripts/file_parsers/example.log"
    ):
         if "ERROR" in row:
            print(row)


def main():
    find_errors(read_file)
    
        

if __name__ == "__main__":
    main()

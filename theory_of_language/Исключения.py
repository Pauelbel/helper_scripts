
def main():
    try:
        input_string = int(input("введите число: "))
    except ValueError:
        print("введено не число")
        return
    return print("спасибо, ваше число: ", input_string)

if __name__ == "__main__":
    main()
def main():
    formatters = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list", "unordered-list",
                  "new-line"]

    while True:
        command = input('Choose a formatter: ')
        if command == '!help':
            print(f'Available formatters: {', '.join(formatters)}')
            print('Special commands: !help, !done')
        elif command == '!done':
            break
        else:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    main()

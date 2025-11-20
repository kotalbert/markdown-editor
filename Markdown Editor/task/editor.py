def handle_formatting(command: str) -> None:
    match command:
        case 'plain':
            pass
        case 'bold':
            pass
        case 'italic':
            pass
        case 'header':
            pass
        case 'link':
            pass
        case 'inline-code':
            pass
        case 'ordered-list':
            pass
        case 'unordered-list':
            pass


def main():
    formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list',
                  'new-line']

    while True:
        command = input('Choose a formatter: ')
        if command == '!help':
            print(f'Available formatters: {' '.join(formatters)}')
            print('Special commands: !help !done')
        elif command == '!done':
            break
        elif command in formatters:
            handle_formatting(command)
        else:
            print('Unknown formatting type or command')


if __name__ == '__main__':
    main()

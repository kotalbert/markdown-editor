markdown_list = []


def print_markdown() -> None:
    for item in markdown_list:
        print(item, end='')
    print()


def handle_plain_text() -> None:
    plain_text = input('Text: ')
    markdown_list.append(plain_text)
    print_markdown()


def handle_formatting(command: str) -> None:
    match command:
        case 'plain':
            handle_plain_text()
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

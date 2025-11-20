markdown_list = []


def print_markdown() -> None:
    for item in markdown_list:
        print(item, end='')
    print()


def handle_plain_text() -> None:
    plain_text = input('Text: ')
    markdown_list.append(plain_text)
    print_markdown()


def handle_bold_text() -> None:
    bold_text = input('Text: ')
    markdown_list.append(f'**{bold_text}**')
    print_markdown()


def handle_italic_text() -> None:
    italic_text = input('Text: ')
    markdown_list.append(f'*{italic_text}*')
    print_markdown()


def handle_header() -> None:
    while True:
        level = int(input('Level: '))
        if 1 <= level <= 6:
            break
        else:
            print('The level should be within the range of 1 to 6')
    header_text = input('Text: ')
    # add a line break before header if it's not the first element
    if len(markdown_list) > 0:
        add_new_line()
    markdown_list.append(f'{"#" * level} {header_text}')
    add_new_line()
    print_markdown()


def handle_link() -> None:
    label = input('Label: ')
    url = input('URL: ')
    markdown_list.append(f'[{label}]({url})')
    print_markdown()


def handle_inline_code() -> None:
    code_text = input('Text: ')
    markdown_list.append(f'`{code_text}`')
    print_markdown()


def handle_ordered_list() -> None:
    while True:
        try:
            num_rows = int(input('Number of rows: '))
            if num_rows <= 0:
                print('The number of rows should be greater than zero')
                continue
            break
        except ValueError:
            print('The number of rows should be greater than zero')
    for i in range(1, num_rows + 1):
        row_text = input(f'Row #{i}: ')
        markdown_list.append(f'{i}. {row_text}\n')
    print_markdown()


def handle_unordered_list() -> None:
    while True:
        try:
            num_rows = int(input('Number of rows: '))
            if num_rows <= 0:
                print('The number of rows should be greater than zero')
                continue
            break
        except ValueError:
            print('The number of rows should be greater than zero')
    for _ in range(num_rows):
        row_text = input(f'Row #{_ + 1}: ')
        markdown_list.append(f'* {row_text}\n')
    print_markdown()

def add_new_line() -> None:
    markdown_list.append('\n')

def handle_formatting(command: str) -> None:
    match command:
        case 'plain':
            handle_plain_text()
        case 'bold':
            handle_bold_text()
        case 'italic':
            handle_italic_text()
        case 'header':
            handle_header()
        case 'link':
            handle_link()
        case 'inline-code':
            handle_inline_code()
        case 'new-line':
            add_new_line()
            print_markdown()
        case 'ordered-list':
            handle_ordered_list()
        case 'unordered-list':
            handle_unordered_list()


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

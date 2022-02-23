import os, re

def main():
    """
    Crawls a directory tree, generates HTML document from text files
    Applies HTML span styling to selected words in the wordlist
    Customize the wordlist and directory as appropriate
    Can customize the span style to include text color, highlighting etc etc
    """
    wordlist = ['list', 'of', 'words', 'or phrases']
    directory = '/Users/User/Documents/DIRECTORY1'

    for root, dirs, files in os.walk(directory):
        for file in files:
            filetype = os.path.splitext(file)[1]
            if filetype == '.txt':
                filepath = os.path.join(root, file)
                with open(filepath) as f:
                    text = f.read()
                    text = '<div style="white-space: pre-wrap; word-break: keep-all;">' + text + '</div>'
                    for word in wordlist:
                        if word.lower() in text.lower():
                            # This part can be customized to be whatever color you want, highlighting etc
                            text = re.sub(word, '<span style="color: red">{}</span>'.format(word), text, flags=re.IGNORECASE)
                    with open(filepath[:-4] + '.html', mode='w+', encoding='utf-8') as h:
                        h.write('\r')
                        h.write(text)
                        h.write('\n')

if __name__ == '__main__':
    main()
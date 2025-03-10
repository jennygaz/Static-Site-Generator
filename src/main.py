from textnode import TextNode, TextType

def main():
    node = TextNode('Anchor text', TextType('link'), 'https://www.google.com')
    print(node)

if __name__ == '__main__':
    main()
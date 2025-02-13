from textnode import TextType
from textnode import TextNode

def main():
    node = TextNode("this is a test node", TextType.BOLD, "https://laernorsk.no")
    print(node)

if __name__ == "__main__":
    main()


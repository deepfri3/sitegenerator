from textnode import TextNode, TextType

def main():
    #print("Hello from 10-site-generator!")
    tnode = TextNode("This is some anchor test", TextType.LINKS_ANCHOR_TEXT, "https://www.boot.dev")
    print(tnode)

if __name__ == "__main__":
    main()

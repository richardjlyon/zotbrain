from zotero.api import Zotero

def main():
    client = Zotero()
    coll = client.get_collections()
    print(coll)


if __name__ == "__main__":
    main()


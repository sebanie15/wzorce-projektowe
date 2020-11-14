class Document:
    pass


class Catalog:
    def __init__(self):
        self._document = None

    def set_document(self, document: Document):
        self._document = document


if __name__ == "__main__":
    document = Document()
    catalog = Catalog()
    catalog.set_document(document)

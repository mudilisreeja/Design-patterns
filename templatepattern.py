from abc import ABC, abstractmethod
class DocumentGenerator(ABC):
    def generate_document(self):
        self.add_header()
        self.add_content()
        self.add_footer()

    def add_header(self):
        pass

    def add_content(self):
        pass

    def add_footer(self):
        pass
class PDFGenerator(DocumentGenerator):
    def add_header(self):
        print("Adding PDF Header")

    def add_content(self):
        print("Adding PDF Content")

    def add_footer(self):
        print("Adding PDF Footer")
class WordGenerator(DocumentGenerator):
    def add_header(self):
        print("Adding Word Header")

    def add_content(self):
        print("Adding Word Content")

    def add_footer(self):
        print("Adding Word Footer")
if __name__ == "__main__":
    print("Generating PDF Document:")
    pdf_generator = PDFGenerator()
    pdf_generator.generate_document()

    print("\nGenerating Word Document:")
    word_generator = WordGenerator()
    word_generator.generate_document()
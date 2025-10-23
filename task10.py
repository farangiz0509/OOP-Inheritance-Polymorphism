class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    def print_preview(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")
    

class WordDocument(Document):
    def print_preview(self):
        print(f"Word hujjat: {self.title}")
        print(f"Ichidagi matn: {self.content[:100]}")

class PdfDocument(Document):
    def print_preview(self):
        print(f"Word hujjat: {self.title.upper()}")
        print(f"Ichidagi matn: {self.content}")

word_doc = WordDocument("Dars jadvali", "Bugungi kun juda issiq bo'ldi")
pdf_doc = PdfDocument("Hisobot", "2025-yilning yozi juda issiq keldi")


word_doc.print_preview()
print()
pdf_doc.print_preview()
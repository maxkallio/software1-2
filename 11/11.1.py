class Publication:
    def init(self, name):
        self.name = name

    def print_information(self):
        print("Name:", self.name)


class Book(Publication):
    def init(self, name, toimittaja, page_count):
        super().init(name)
        self.toimittaja = toimittaja
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print("Toimittaja:", self.toimittaja)
        print("Page count:", self.page_count)


class Magazine(Publication):
    def init(self, name, pää_toimittaja):
        super().init(name)
        self.pää_toimittaja = pää_toimittaja

    def print_information(self):
        super().print_information()
        print("Pää toimittaja:", self.pää_toimittaja)


donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
hytti_no_6 = Book("Hytti No. 6", "Rosa Liksom", 192)

donald_duck.print_information()
print()
hytti_no_6.print_information()
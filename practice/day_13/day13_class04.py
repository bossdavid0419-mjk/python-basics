class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print(f"'{self.title}'은(는)) 이미 대출 중입니다.")
            return

        self.is_borrowed = True
        print(f"'{self.title}'(은/을) 대출했습니다.")

    def return_book(self):
        if not self.is_borrowed:
            print(f"'{self.title}'은(는) 이미 대출 중이 아닙니다.")
            return

        self.is_borrowed = False
        print(f"'{self.title}'(은/을) 반납했습니다.")

    def show(self):
        status = "대출 중" if self.is_borrowed else "대출 가능"
        print(f"{self.title} ({status})")


book1 = Book("파이썬 기초")
book2 = Book("C++ 입문")

book1.show()
book1.borrow()
book1.borrow()
book1.show()
book2.show()
book1.return_book()
book1.return_book()
book1.show()
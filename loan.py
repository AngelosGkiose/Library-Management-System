from datetime import date


class Loan:
    def __init__(self,book_id,member_id,borrow_date,loan_id=None):
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.loan_id = loan_id

    def days_borrowed(self):
        if self.borrow_date is None:
            return 0
        borrow_date = date.fromisoformat(self.borrow_date)
        return (date.today() - borrow_date).days


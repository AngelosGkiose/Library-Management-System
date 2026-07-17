from datetime import datetime


class Loan:
    def __init__(self,book_id,member_id,borrow_date,loan_id=None):
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.loan_id = loan_id

    def days_borrowed(self):
        if self.borrow_date is None:
            return 0
        return (datetime.now() - self.borrow_date).days


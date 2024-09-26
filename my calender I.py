class MyCalendar:

    def __init__(self):
        self.bookings = []

    def book(self, start, end):
        # Check for overlapping events in the current bookings
        for s, e in self.bookings:
            if not (end <= s or start >= e):  # if there is any overlap
                return False
        # If no overlap, add the new booking
        self.bookings.append((start, end))
        return True


# Example usage
myCalendar = MyCalendar()
print(myCalendar.book(10, 20))  # returns True
print(myCalendar.book(15, 25))  # returns False (overlap with 10, 20)
print(myCalendar.book(20, 30))  # returns True (no overlap)

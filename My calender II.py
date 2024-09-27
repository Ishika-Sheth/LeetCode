class MyCalendarTwo:
    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start, end):
        # Check if the new event would cause a triple booking
        for os, oe in self.overlaps:
            if start < oe and end > os:
                return False
        
        # Add to overlaps if the new event overlaps with any existing ones
        for cs, ce in self.calendar:
            if start < ce and end > cs:
                self.overlaps.append((max(start, cs), min(end, ce)))
        
        # Finally, add the new event to the calendar
        self.calendar.append((start, end))
        return True

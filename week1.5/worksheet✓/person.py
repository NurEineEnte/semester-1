# Worksheet 1.5: Person class

from datetime import date

class Person():
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name,birth):
        """hello world"""
        if name == "":
            raise ValueError
        if not isinstance(name, str):
            raise TypeError

        if not isinstance(birth, date):
            raise TypeError
        self.name = name
        self.birth = birth
    def initials(self):
        """returns initials of name"""
        x = self.name.title()
        initials = ""
        for i in x:
            if i == i.upper() and i != " ":
                initials += i
        return initials
    def is_birthday(self):
        """tells if the persons birthday is today"""
        if self.birth.day == date.today().day and self.birth.month == date.today().month:
            return True
        else:
            return False
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
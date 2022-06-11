'''
Declare a class named Notes and define the following attributes in it:

uid: 1005435
title: "Шутка"
author: "И.С. Бах"
pages: 2

Then, use the getattr() function to read and display the value of the author attribute.
'''


class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

print(getattr(Notes, 'author', False))
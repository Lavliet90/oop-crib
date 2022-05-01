class Women:
    title = 'object classes for field title'
    photo = 'object classes for field photo'
    ordering = 'object classes for field ordering'

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ['id']

        def __init__(self, access):
            self._access = access
            self._t = Women.title  # лучше не связывать с внешними классами


print(Women.ordering)
print(Women.Meta.ordering)

w = Women('toor', '123145')
print(w.ordering)
print(w.Meta.ordering)
print(w.__dict__)
print(w.meta.__dict__)

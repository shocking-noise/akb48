import optparse
import yaml
from datetime import date, timedelta


class AKB48(object):

    def __init__(self):
        with open("member.yaml", "r") as f:
            self.members = yaml.load(f.read().decode("utf-8"))
        self._initialize()

    def _initialize(self):
        for m in self.members:
            today = date.today()
            birthday = m["birthday"]
            age = today.year - birthday.year
            if today < self._yearbirthday(birthday, today.year):
                age -= 1
            m["age"] = age

    def _yearbirthday(self, b, y):
        try:
            return b.replace(year=y)
        except ValueError:
            b += timedelta(days=1)
            return b.replace(year=y)

    def member(self, **kwd):
        ret = self.members
        for key, value in kwd.items():
            if value:
                ret = filter(lambda x: x[key] == value, ret)
        return ret

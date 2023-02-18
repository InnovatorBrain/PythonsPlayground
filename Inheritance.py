# this contains only concepts of inheritance

class person():
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname

    def hello(self):
        print("hello!")

    def report(self):
        print(f"I am {self.fname} {self.lname}")


x = person("faizan", "ahmad")
x.hello()
x.report()


class agent(person):
    #overwrite report
    def report(self):
        print("I am here!")
    def check(self, passcode):
        if passcode == 47:
            print(f"I am agent")
        else:
            self.report()


y = person("faizy", "faizyy")
y.report()
z = agent("faizy", "faizyy")
z.check(47)

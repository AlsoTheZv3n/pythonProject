class Person:
    def __init__(self, lastname, firstname, age, job, relationshipStat):
        self.lastname = lastname
        self.firstname = firstname
        self.age = age
        self.job = job
        self.relationshipStat = relationshipStat


    def interdouce(self):
        print("hello, i'am", self.lastname, self.firstname)
        print("My age is", self.age)
        print("I work at", self.job)
        print("My Relationship Status is", self.relationshipStat)



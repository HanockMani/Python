class sem3:
    def __init__(self,name,role) :
        self.name = name
        self.role = role
    def duties(self) :
        print("Attendance, Discipline")

classrep1 = sem3('Revathi', 'classrep')
print(classrep1.name)
print(classrep1.role)
classrep1.duties()
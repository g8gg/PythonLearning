# Object & Class
# lesson 06
# No object is mysterious. The mysterious is your eye.
# Take an object. Do something to it. Do something else to it.


class AnObjectClass:
    pass


class TechTeam:
    def __init__(self, name):
        self.name = name
        self.leader = ''
        self.alias = ''

    def do(self):
        print('do from TechTeam')


class JavaTeam(TechTeam):  # 继承
    Skills = []

    def __init__(self, name='', leader=''):
        super().__init__(name)
        self.leader = leader

    def add_skill(self, skill):
        self.Skills.append(skill)

    def do(self):
        print('do from JavaTeam')


class SomeCertification:
    Certifications = ['PMP', 'OCP 10g', 'CMCDBA', 'MCSD']


class BackendTeam(JavaTeam, SomeCertification):  # 可以多重继承咯?
    def __init__(self, name='', leader=''):
        super().__init__(name, leader)

    def do(self):
        print('do from BackendTeam')


# class TempTeam(TechTeam, JavaTeam, SomeCertification):
#    """class TempTeam(TechTeam, JavaTeam, SomeCertification):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases JavaTeam, SomeCertification, TechTeam
# """
class TempTeam(JavaTeam, SomeCertification):  # JavaTeam already includes TechTeam, you don't need to include it again.
    def __init__(self, name=''):
        super().__init__(name)

    def __init__(self, name='', leader=''):
        super().__init__(name, leader)

    def do(self):  # override
        pass  # do nothing

    def new_do(self):  # add new method
        print('newdo from TempTeam')


print('tech_team', '-' * 60)
tech_team = TechTeam('column')
print(tech_team.name)
tech_team.name = tech_team.name.capitalize() + 'V'
print(tech_team.name)
tech_team.do()

print('java_team', '-' * 60)
java_team = JavaTeam('JTeam')
java_team.add_skill('SSH')
java_team.add_skill('SSH2')
java_team.add_skill('MyBatis3')
print(java_team.name)
print(java_team.Skills)
java_team.do()

print('backend_team', '-' * 60)
backend_team = BackendTeam('ThinkInLAMP', 'Majun')
print(backend_team.name)
print(backend_team.leader)
backend_team.add_skill('Nginx')
backend_team.add_skill('Resin')
backend_team.add_skill('OpenResty')
print(backend_team.Skills)
backend_team.do()

print('temp_team', '-' * 60)
temp_team = TempTeam('SwiftCon')
print(temp_team.name, temp_team.leader)
temp_team.do()
temp_team.new_do()

print('temp_team1', '-' * 60)
temp_team1 = TempTeam('SwiftCon', 'G8GG')
print(temp_team1.name, temp_team1.leader)
temp_team1.do()
temp_team1.new_do()

TempTeam.new_do(temp_team1)  # Note: Yes, Python pass self like this.

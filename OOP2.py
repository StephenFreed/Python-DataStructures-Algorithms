class School:
    def __init__(self, name, level, number_of_students):
      self.name = name
      self.level = level
      self.number_of_students = number_of_students

    def get_name(self):
      print(self.name)

    def get_level(self):
      print(self.level)

    def get_number_of_students(self):
      print(self.number_of_students)
    
    def set_number_of_students(self, number_students):
      self.number_of_students = number_students

    def __repr__(self):
      return 'A {} school name {} with {} students.'.format(self.level,self.name,self.number_of_students)
      
    def __str__(self):
      return 'yeahh'


class PrimarySchool(School):
    def __init__(self, name, number_of_students, pickup_policy):
      super().__init__(name, 'Primary', number_of_students)
      self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
      print(self.pickup_policy)

    def __repr__(self):
      return 'A Primary school {} with {} students and {} pickup policy.'.format(self.name,self.number_of_students,self.pickup_policy,self.pickup_policy)



class HighSchool(School):
    def __init__(self, name, number_of_students, pickup_policy, sports_teams):
      super().__init__(name, 'High School', number_of_students)
      self.pickup_policy = pickup_policy
      self.sports_teams = sports_teams

    def get_sports_teams(self):
      print(self.sports_teams)

    def __repr__(self):
      return 'A {} school {} with {} students and {} pickup policy and {} sports.'.format(self.level,self.name,self.number_of_students,self.pickup_policy,self.pickup_policy,self.sports_teams)



phillipsburg = HighSchool('Phillipsbug','High School', '500',['football','soccer','baseball'])
lopat = PrimarySchool('Lopat', '100', 'Yes')

print(repr(phillipsburg))
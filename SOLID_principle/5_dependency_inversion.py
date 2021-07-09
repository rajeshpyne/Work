# Dependency Inversion Principle
# a). High level module should not depend on low level modules. Both should depend on abstractions -> Open_Closed Principle
# b). Abstractions should not depend on details. Details should depend on abstractions -> Liskov Substitution
'''
We are directly using team_student_memberships.team_memberships In our high level class Analysis and
we are using the implementationof this list directly in high level class.
As of now this is fine but imagine a situation in which we need to change this implementation from list
to something else. In that case our high-level class Analysis would break as it is dependent on
implementation details of Low level class TeamMemberships.
'''

from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
  BLUE_TEAM = 1
  RED_TEAM = 2
  GREEN_TEAM = 3

class Student:
  def __init__(self, name):
    self.name = name

class TeamMemberships():
  def __init__(self):
    self.team_memberships = []

  def add_team_memberships(self, student, team):
    self.team_memberships.append((student, team))

class Analysis():
  def __init__(self, team_student_memberships):
    memberships = team_student_memberships.team_memberships
    for members in memberships:
      if members[1] == Teams.RED_TEAM:
        print(f'{members[0].name} is in RED team')


student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)


# Dependency Inversion Principle
# a). High level module should not depend on low level modules. Both should depend on abstractions
# b). Abstractions should not depend on details. Details should depend on abstractions
'''
To comply to Dependency Inversion Principle, we need to ensure that high level class Anslysis 
should not depend on concrete  implementation of low level class TeamMemberships. 
Instead it should depend on some abstraction. 
So, we create an interface TeamMembershipLookup that contains an abstract method `find_all_students_of_team`
which is passed to any class that inherits from this interface. 
We make our `TeamMembership` class to inherit from this interface and hence 
now `TeamMembership` class needs to provide an implementation of the find_all_students_of_team function. 
This function then yields the results to any other calling entity. 
We moved the processing that was done in high-level Analysis class to 
TeamMemberships class through the interface TeamMembershipLookup.
So, by doing this we have removed dependency of high level class Analysis from low level class TeamMemberships 
and transferred this dependency to interface TeamMembershipLookup. 
Now the high-level class doesn’t depend on implementation details of low level class. 
Any changes to the implementation details of low level class doesn’t impact the high-level class.
'''
from enum import Enum
from abc import ABC, abstractmethod


class Teams(Enum):
  BLUE_TEAM = 1
  RED_TEAM = 2
  GREEN_TEAM = 3


class TeamMembershipLookup(ABC):
  @abstractmethod
  def find_all_students_of_team(self, team):
    pass


class Student:
  def __init__(self, name):
    self.name = name


class TeamMemberships(TeamMembershipLookup):
  def __init__(self):
    self.team_memberships = []

  def add_team_memberships(self, student, team):
    self.team_memberships.append((student, team))

  def find_all_students_of_team(self, team):
    for members in self.team_memberships:
      if members[1] == team:
        yield members[0].name


class Analysis():
  def __init__(self, team_membership_lookup):
    for student in team_membership_lookup.find_all_students_of_team(Teams.RED_TEAM):
      print(f'{student} is in RED team.')


student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)
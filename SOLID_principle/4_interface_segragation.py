from abc import ABC, abstractmethod

# Interface Substitution Principle
# No client should be forced to depend on methods it does not use
'''
A larger interface bundled with all methods makes it mandatory for all classes to provide 
implementation of all the methods even if some methods are not relevant to them
'''

class CommunicationDevice(ABC):
  @abstractmethod
  def make_calls(self):
    pass

  @abstractmethod
  def send_sms(self):
    pass

  @abstractmethod
  def browse_internet(self):
    pass

class SmartPhone(CommunicationDevice):
  def make_calls(self):
    #implementation
    pass

  def send_sms(self):
    #implementation
    pass

  def browse_internet(self):
    #implementation
    pass

class LandlinePhone(CommunicationDevice):
    def make_calls(self):
      #implementation
      pass

    def send_sms(self):
      #just pass or raise exception as this feature is not supported
      pass

    def browse_internet(self):
      #just pass or raise exception as this feature is not supported
      pass


from abc import ABC, abstractmethod

# Interface Substitution Principle
# No client should be forced to depend on methods it does not use
'''
Smaller role interfaces are created for each feature and the classes would only extend the required interfaces and implement the
relevant methods
'''

class CallingDevice(ABC):
  @abstractmethod
  def make_calls(self):
    pass

class MessagingDevice():
  @abstractmethod
  def send_sms(self):
    pass

class InternetbrowsingDevice():
  @abstractmethod
  def browse_internet(self):
    pass

class SmartPhone(CallingDevice, MessagingDevice, InternetbrowsingDevice):
  def make_calls(self):
    #implementation
    pass

  def send_sms(self):
    #implementation
    pass

  def browse_internet(self):
    #implementation
    pass

class LandlinePhone(CallingDevice):
  def make_calls(self):
    #implementation
    pass
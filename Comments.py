import datetime

class user(object):
  def __init__(self, name):
    self.name = name
    self._logged_in = False
    self.last_logged_in_at = None
  
  def get_name(self, value = None):
    if(not value):
      return(self.name)
    else:
      self.name = value

  def is_logged_in(self):
    return(self._logged_in)
  
  def get_last_logged_in_at(self):
    return(self.last_logged_in_at)
  
  def log_in(self):
    self._logged_in = True
    self.last_logged_in_at = datetime.datetime.now()
  
  def log_out(self):
    self._logged_in = False
  
  def can_edit(self, comment):
    if (comment.author.name == self.name):
      return True
    else:
      return False
  
  def can_delete(self, comment):
    return False
  
  def to_string(self, comment):
    return("hello by " + comment.author.name) 

class moderator(user):
  def __init__(self, name):
    self.name = name

  def can_delete(self, comment):
    return True

class admin(moderator):
  def __init__(self, name):
      self.name = name

  def can_edit(self, comment):
      return True

class comment(object):
  def __init__(self, author, message, replied_to = None):
    self.author = author
    self.message = message
    self.replied_to = replied_to
    self.created_at = datetime.datetime.now()
    
  def get_author(self, value = None):
     if(not value):
      return(self.author)
     else:
      self.author = value

  def get_message(self, value = None):
    if(not value):
      return(self.message)
    else:
      self.message = value
    
  def get_created_at(self):
    return(self.created_at)
  
  def get_replied_to(self, value = None):
    if(not value):
      return(self.replied_to)
    else:
      self.replied_to = value
  
  def to_string(self):
    if(not self.replied_to):
      return(self.message + " by " + self.author.name)
    else:
      return(self.message + " by " + self.author.name + " (replied to " + self.replied_to.author.name + ")")

user1 = user("Stanley")
user1.log_in()
print(user1.last_logged_in_at)

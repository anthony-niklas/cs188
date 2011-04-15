import time
SLEEP_TIME = 0
class NullGraphics:
  def initialize(self, state, isBlue = False):
    pass
  
  def update(self, state):
    pass
  
  def pause(self):
    time.sleep(SLEEP_TIME)
    
  def draw(self, state):
    print state
  
  def finish(self):
    pass

  def updateDistributions(self,gb):
    pass
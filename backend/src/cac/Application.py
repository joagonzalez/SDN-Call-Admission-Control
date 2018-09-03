import sys
import logging

from .ryu.Controller import RyuController
from .caller.Controller import AriController

class Application:
  def __init__(self):
    ''' constructor '''
    self.listen = False
    self.args = sys.argv[1:]
    self.ryuController = RyuController()
    self.ariController = AriController(self.ryuController)

  def run(self):
    ''' Run application. Start listen in ari and exposes the ws-front-service to webapp '''
    try:
      self.ariController.start()
      self.listen = True
      logging.info('Start Stasis Application')
    except Exception as error:
      self.listen = False
      logging.error(error)

  def getMetrics(self):
    ''' public method that exposes requests to the internal api to the webapp '''
    return self.ariController.doSomething()

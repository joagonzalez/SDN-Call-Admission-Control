import sys
import logging
import ari

class AriController:
  def __init__(self, ryuApi):
    ''' Stasis Program '''
    self.base_url = 'http://localhost:8002/'
    self.username = 'user'
    self.password = 'pass'
    self.bridges = []
    self.client = None
    self.ryuApi = ryuApi

  def connect(self):
    try:
      # self.client = ari.connect(self.base_url, self.username, self.password)
      logging.info('Connecting ari service successful')
    except Exception as error:
      logging.error('Error on connect ari service::' + repr(error))
      sys.exit()
  
  def doSomething(self):
    return self.ryuApi.queryForGetNodes()

  def onStartCallback(self, channel, event):
    ''' initialize channels and events '''
    print(channel)
    print(event)

  def onEndCallback(self, channel, event):
    ''' Hangout bridges, channels and stop listening. Clean stuff '''

  def start(self):
    ''' Starts Stasis program and bind the events for the application '''
    self.client = self.connect()
    #self.client.on_event('StasisStart', self.onStartCallback)

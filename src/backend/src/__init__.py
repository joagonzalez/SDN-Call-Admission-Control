__version__ = '0.1'

from .config import logger
from .cac.Application import Application
from .front.Facade import FacadeWsService
from .front.Client import Client
from os import system

def setTopo1():
  system('sudo kill $(sudo ps ux | grep /usr/local/bin/mn | awk \'{print $2}\')')
  system('sudo mn --clean')
  system('sudo mn --topo=tree,3,3 --controller remote')

def setTopo2():
  system('sudo kill $(sudo ps ux | grep /usr/local/bin/mn | awk \'{print $2}\')')
  system('sudo mn --clean')
  system('sudo mn --topo=linear,6,3 --controller remote')

# Setup application
def run():
  frontClient = Client()
  Cac = Application(frontClient)
  Cac.run()

  if Cac.listen:
    FacadeApp = FacadeWsService()
    FacadeApp.register_command(Cac.getMetrics, 'getMetrics')
    FacadeApp.register_command(Cac.getPorts, 'getPorts')
    FacadeApp.register_command(setTopo1, 'setTopo1')
    FacadeApp.register_command(setTopo2, 'setTopo2')
    FacadeApp.run(frontClient)

# Controlador Faucet SDN

Faucet is an OpenFlow controller for multi-table OpenFlow 1.3 switches (including optional table features), that implements layer 2 switching, VLANs, ACLs, and layer 3 IPv4 and IPv6 routing, static and via BGP. The Openflow switch is deployed as a drop in replacement for a L2/L3 switch in the network to enable extra SDN based functionality. (fork del proyecto RYU).

Además, Faucet esta implementado en Python.

- https://faucet.nz/
- docs.faucet.nz (documentación)
- https://faucet-sdn.blogspot.com/

Otra cosa interesante de Faucet, es que utiliza Graphana para graficar datos recolectados por OpenFlow de forma nativa.

### Asteriks posee tres APIs para interactuar: ARI, AGI y AMI

# Asterisk RESTful Interface (ARI)

- https://wiki.asterisk.org/wiki/pages/viewpage.action?pageId=29395573


ARI consists of three different pieces that are - for all intents and purposes - interrelated and used together. They are:

        A RESTful interface that a client uses to control resources in Asterisk.
        A WebSocket that conveys events in JSON about the resources in Asterisk to the client.
        The Stasis dialplan application that hands over control of a channel from Asterisk to the client.

        ari = ARI('localhost', ('username', 'password'))
 
        #Hang up all channels
        channels = ari.get('channels')
        for channel in channels:
        ari.delete('channels', channel['id'])

##ARI Data Models Documentation

- https://wiki.asterisk.org/wiki/display/AST/Asterisk+12+REST+Data+Models

## Introduction to ARI and Channels

- https://wiki.asterisk.org/wiki/display/AST/Introduction+to+ARI+and+Channels



                #!/usr/bin/env python
 
                import ari
                import logging

                logging.basicConfig(level=logging.ERROR)

                client = ari.connect('http://localhost:8088', 'asterisk', 'asterisk')
 
                current_channels = client.channels.list()
                if (len(current_channels) == 0):
                    print "No channels currently :-("
                else:
                    print "Current channels:"
                   for channel in current_channels:
                       print channel.json.get('name')
 
                def stasis_start_cb(channel_obj, ev):
                    """Handler for StasisStart event"""
 
                   channel = channel_obj.get('channel')
                   print "Channel %s has entered the application" % channel.json.get('name')
 
                   for key, value in channel.json.items():
                       print "%s: %s" % (key, value)
 
                def stasis_end_cb(channel, ev):
                 """Handler for StasisEnd event"""
 
                   print "%s has left the application" % channel.json.get('name')
 
                client.on_channel_event('StasisStart', stasis_start_cb)
                client.on_channel_event('StasisEnd', stasis_end_cb)
 
                client.run(apps='channel-dump')

## ARI and Channels: Simple Media Manipulation

- https://wiki.asterisk.org/wiki/display/AST/ARI+and+Channels%3A+Simple+Media+Manipulation

# Asterisk Gateway Interface (AGI)

AGI is analogous to CGI in Apache. AGI provides an interface between the Asterisk dialplan and an external program that wants to manipulate a channel in the dialplan. In general, the interface is synchronous - actions taken on a channel from an AGI block and do not return until the action is completed.


- https://www.voip-info.org/asterisk-agi
- https://wiki.asterisk.org/wiki/pages/viewpage.action?pageId=29395573 - API Asterisk
- https://stackoverflow.com/questions/20043034/how-to-log-a-call-from-asterisk-to-external-web-service
- https://faucet.nz/ - Controlador
- https://www.youtube.com/channel/UChRZ5O2diT7QREazfQX0stQ/videos

## Python

- Fats http://sourceforge.net/projects/fats/ FastAGI & AMI for the Twisted framework, MIT license. Full code test covered, Mock Object pattern examples.
- PyAstre https://pypi.python.org/pypi/pyastre: Asterisk modules using Twisted framework.
- Python AGI http://sourceforge.net/projects/pyst
- Python AGI bindings py-Asterisk

##Manager interface with Plone/Zope atasterisk

- StarPy http://starpy.sourceforge.net/: Asterisk Twisted modules for AMI clients and FastAGI servers

#  Asterisk Manager Interface (AMI)

AMI provides a mechanism to control where channels execute in the dialplan. Unlike AGI, AMI is an asynchronous, event driven interface. For the most part, AMI does not provide mechanisms to control channel execution - rather, it provides information about the state of the channels and controls about where the channels are executing.

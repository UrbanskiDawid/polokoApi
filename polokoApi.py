#!/usr/bin/env python
__author__ = "Dawid Urbanski"
__license__ = "GPL"
__version__ = "1.0.0"

import requests
import json
import time

def _getPost(URL,DATA):
  res = requests.post(
    url="http://poloko.pl/polokoApi/timetables/{0}".format(URL),
    data=DATA,
    headers={'Content-Type': 'application/json;charset=UTF-8'})
  return res.json()
	
DIRECTION_TO="TO"
DIRECTION_FROM="FROM"

class timetables:

  #curl 'http://poloko.pl/polokoApi//timetables/search'
  #-H 'Content-Type: application/json;charset=UTF-8'
  #--data-binary '{"agencyIds":["mpk_krakow"],"searchString":"0"}'
  @staticmethod
  def searchAgency(agencyId,str):
    return _getPost(
      'search',
      '{{"agencyIds":["{0}"],"searchString":"{1}"}}'.format(agencyId,str)
    )#{u'routes':[], u'stops':[]}

  #curl 'http://poloko.pl/polokoApi/timetables/agencies'
  @staticmethod
  def getAgencies():
    res = requests.get('http://poloko.pl/polokoApi/timetables/agencies')
    return res.json() #agencies [ {groupId,inconUrl,id,name}] groups [{iconUrl,id,name}]

  #curl 'http://poloko.pl/polokoApi/timetables/routes'
  #-H 'Content-Type: application/json;charset=UTF-8'
  #--data-binary '["mpk_krakow"]'
  @staticmethod
  def getRoutes(AgencieName):
    return _getPost(
      'routes',
      '["{0}"]'.format(AgencieName)
      )

  @staticmethod
  def getRoute(RouteID,Direction):
    return _getPost('route','{{ "routeId":"{0}","direction":"{1}" }}'.format(RouteID,Direction))

  #get stops?

  @staticmethod
  def getStop(stopID):
    return _getPost('getStop',stopID)
  
  @staticmethod
  def getTimetable(routeId,direction,stopId):
    date=time.strftime("%d-%m-%Y")
    return _getPost('timetable',
      '{{"routeId":"{0}","direction":"{1}","stopId":"{2}","fromDate":"{3}","toDate":"{4}"}}'.format(routeId,direction,stopId,date,date)
    )

  #curl 'http://poloko.pl/polokoApi/timetables/departuresForRoute'
  #-H 'Content-Type: application/json;charset=UTF-8' 
  #--data-binary '{"stopId":"8-p033201B","routeId":"8-29","sinceTime":"14-10-2016 22:53"}'
  @staticmethod
  def getDeparturesForRoute(stopID,routeId):
    Time=time.strftime("%d-%m-%Y %H:%M")
    return _getPost('timetable','{{"stopId":"{0}","routeId":"{1}","sinceTime":"{2}"}}'.format(stopId,routeID,Time))

#curl 'http://poloko.pl/polokoApi/timetables/routeForStop' 
#-H 'Content-Type: application/json;charset=UTF-8' 
#--data-binary '{"routeId":"8-29","stopId":"8-p033201B","direction":"TO"}'

#curl 'http://poloko.pl/polokoApi/timetables/routeForStopAndTrip' 
#-H 'Content-Type: application/json;charset=UTF-8' 
#--data-binary '{"routeId":"8-0","stopId":"8-p012500T","direction":"FROM","tripId":"8-287"}'

#curl 'http://poloko.pl/polokoApi/timetables/nearTransfers' 
#-H 'Content-Type: application/json;charset=UTF-8' 
#--data-binary '{"lat":50.05304703257761,"lng":19.91668939590454,"agencyIds":["mpk_krakow"]}'

#curl 'http://poloko.pl/polokoService/departure' 
#-H 'Content-Type: application/json;charset=UTF-8' 
#--data-binary '{"dateTime":"14-10-2016 05:00","from":{"lat":"50.025711","lng":"19.920745"},"to":{"lat":"50.065245","lng":"19.877317"},"routingType":"OPTIMAL"}'


#curl 'http://poloko.pl/polokoApi//timetables/search' 
#-H 'Content-Type: application/json;charset=UTF-8' 
#--data-binary '{"agencyIds":["mpk_krakow"],"searchString":"0"}'
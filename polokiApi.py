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

STOP_ID_RUCZAJ="8-p055901T"
STOP_ID_RZEMIESNICZA="8-p070601T"

ROUTE_ID_23="8-20"

class timetables:

  #curl 'http://poloko.pl/polokoApi/timetables/agencies' -H 'Pragma: no-cache' -H 'DNT: 1' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en,pl;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' -H 'Accept: application/json, text/plain, */*' -H 'Referer: http://poloko.pl/' -H 'Cookie: lastSearched=%5B%7B%22id%22%3A%228-20%22%2C%22name%22%3A%2223%22%2C%22lastStop%22%3A%22Czerwone%20Maki%22%2C%22routeType%22%3A%22TRAM%22%2C%22direction%22%3A%22TO%22%2C%22agencyId%22%3Anull%2C%22resultType%22%3A%22route%22%7D%5D; lang=PL; _ga=GA1.2.1967863865.1476465638' -H 'Connection: keep-alive' -H 'Cache-Control: no-cache' --compressed
  @staticmethod
  def getAgencies():
    res = requests.get('http://poloko.pl/polokoApi/timetables/agencies')
    return res.json() #agencies [ {groupId,inconUrl,id,name}] groups [{iconUrl,id,name}]

  #curl 'http://poloko.pl/polokoApi/timetables/routes' -H 'Pragma: no-cache' -H 'Origin: http://poloko.pl' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: en,pl;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36' -H 'Content-Type: application/json;charset=UTF-8' -H 'Accept: application/json, text/plain, */*' -H 'Cache-Control: no-cache' -H 'Referer: http://poloko.pl/' -H 'Cookie: lastSearched=%5B%7B%22id%22%3A%228-20%22%2C%22name%22%3A%2223%22%2C%22lastStop%22%3A%22Czerwone%20Maki%22%2C%22routeType%22%3A%22TRAM%22%2C%22direction%22%3A%22TO%22%2C%22agencyId%22%3Anull%2C%22resultType%22%3A%22route%22%7D%5D; _gat=1; hideCookiesMsg=true; _ga=GA1.2.1967863865.1476465638; lang=PL' -H 'Connection: keep-alive' -H 'DNT: 1' --data-binary '["mpk_krakow"]' --compressed
  @staticmethod
  def getRoutes(AgencieName):
    return _getPost(
      'routes',
      '["{0}"]'.format(AgencieName)
      ) #{agentcyId,id,lastStop,name,routeType}

  "#route '8-20' 'TO'"
  @staticmethod
  def getRoute(RouteID,Direction):
    return _getPost('route','{{ "routeId":"{0}","direction":"{1}" }}'.format(RouteID,Direction))

  #getStop
  @staticmethod
  def getStop(stopID):
    return _getPost('getStop',stopID)
  
  #TODO
  @staticmethod
  def getRouteForStopAndTrip(self,routeId,stopId,direction,tripId):
    return _getPost(
      'routeForStopAndTrip',
      '{'+\
	  ' "routeId":"{0}"'+\
	  ',"stopId":"{1}"'+\
	  ',"direction":"{2}"'+\
	  ',"tripId":"{3}"'+\
	  '}'.format(routeId,stopId,direction,tripId)
	)

  #get timetable #date = 10-10-2016
  @staticmethod
  def getTimetable(routeId,direction,stopId):
    date=time.strftime("%d-%m-%Y")
    return _getPost('timetable',
      '{{"routeId":"{0}","direction":"{1}","stopId":"{2}","fromDate":"{3}","toDate":"{4}"}}'.format(routeId,direction,stopId,date,date)
    )

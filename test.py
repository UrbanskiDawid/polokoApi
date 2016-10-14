#!/usr/bin/env python

import polokiApi
import pprint

STOP_ID_RUCZAJ="8-p055901T"
STOP_ID_RZEMIESNICZA="8-p070601T"

ROUTE_ID_23="8-20"

#a=polokiApi.timetables.getAgencies()
#groups:=
#             {u'iconUrl': u'/agencies/photo/g_Krak\xf3w.png',
#              u'id': u'8',
#              u'name': u'MPK Krak\xf3w'},

#a=polokiApi.timetables.getRoutes('mpk_krakow')
#{u'agencyId': u'mpk_krakow',
#  u'direction': u'TO',
#  u'id': u'8-20',
#  u'lastStop': None,
#  u'name': u'23',
#  u'routeType': u'TRAM'},

#a=polokiApi.timetables.getRoute('8-20','TO')
#{u'directions': [u'TO'],
# u'lastStop': u'Czerwone Maki',
# u'name': u'23',
# u'routeId': u'8-20',
# u'routeType': u'TRAM',
# u'stops': [{u'active': True,
#             u'id': u'8-p029300T',
#             u'lat': 50.017779177529164,
#             u'lng': 19.89121913909912,
#             u'minutesToStop': None,
#             u'name': u'Czerwone Maki'},

#a=polokiApi.timetables.getStop('8-p055901T')

#{u'id': u'8-p055901T',
# u'lat': 50.033653004079234,
# u'lng': 19.938637912273407,
# u'name': u'Rzemie\u015blnicza'}

a=polokiApi.timetables.getTimetable(
    ROUTE_ID_23,
    polokiApi.DIRECTION_TO,
    STOP_ID_RUCZAJ)

#{u'groups': [{u'days': [u'FRIDAY'],
#              u'trips': {u'hours': {u'10': [{u'minutes': 1,
#                                             u'tripId': u'8-6440'},
#                                            {u'minutes': 21,
#                                             u'tripId': u'8-6441'},
#                                            {u'minutes': 41,
#                                             u'tripId': u'8-6442'},
#                                            {u'minutes': 49,

#pprint.pprint(a)
for group in a['groups']:
  days=group['days']
  trips=group['trips']
  for hourKey in sorted(trips['hours'].keys()):
    stops=trips['hours'][hourKey]
    stops=sorted(stops, key=lambda k: k['minutes'])
    for stop in stops:
      tripId=stop['tripId']
      minutes=int(stop['minutes'])
      hour=int(hourKey)
      print '{0:02d}:{1:02d} - tripID:{2}'.format(hour,minutes,tripId)

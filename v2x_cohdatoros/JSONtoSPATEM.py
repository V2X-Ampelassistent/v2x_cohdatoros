# Auto Generated by ASN1toROS2 tool
from v2x_cohdainterfaces.msg import *

def JSONtoSPATEM(mydata):
	# Spatem.msg
	# original asn1 type: SEQUENCE
	
	msg = Spatem()
	if mydata.get("header"):
		msg.header = JSONtoItsPduHeader(mydata.get("header"))
	if mydata.get("spat"):
		msg.spat = JSONtoSPAT(mydata.get("spat"))
	
	return msg

def JSONtoItsPduHeader(mydata):
	# Itspduheader.msg
	# original asn1 type: SEQUENCE
	
	msg = Itspduheader()
	if mydata.get("protocolVersion"):
		msg.protocolversion = JSONtoOrdinalNumber1B(mydata.get("protocolVersion"))
	if mydata.get("messageId"):
		msg.messageid = JSONtoMessageId(mydata.get("messageId"))
	if mydata.get("stationId"):
		msg.stationid = JSONtoStationId(mydata.get("stationId"))
	
	return msg

def JSONtoOrdinalNumber1B(mydata):
	# Ordinalnumber1b.msg
	# original asn1 type: INTEGER
	
	msg = Ordinalnumber1b()
	msg.ordinalnumber1b = mydata
	
	return msg

def JSONtoMessageId(mydata):
	# Messageid.msg
	# original asn1 type: INTEGER
	
	msg = Messageid()
	msg.messageid = mydata
	
	return msg

def JSONtoStationId(mydata):
	# Stationid.msg
	# original asn1 type: INTEGER
	
	msg = Stationid()
	msg.stationid = mydata
	
	return msg

def JSONtoSPAT(mydata):
	# Spat.msg
	# original asn1 type: SEQUENCE
	
	msg = Spat()
	if mydata.get("timeStamp"):
		msg.timestamp = JSONtoMinuteOfTheYear(mydata.get("timeStamp"))
	if mydata.get("name"):
		msg.name = JSONtoDescriptiveName(mydata.get("name"))
	if mydata.get("intersections"):
		msg.intersections = JSONtoIntersectionStateList(mydata.get("intersections"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoMinuteOfTheYear(mydata):
	# Minuteoftheyear.msg
	# original asn1 type: INTEGER
	
	msg = Minuteoftheyear()
	msg.minuteoftheyear = mydata
	
	return msg

def JSONtoDescriptiveName(mydata):
	# Descriptivename.msg
	# original asn1 type: IA5String
	
	msg = Descriptivename()
	msg.descriptivename = mydata
	
	return msg

def JSONtoIntersectionStateList(mydata):
	# Intersectionstatelist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Intersectionstatelist()
	for e in mydata:
		msg.intersectionstatelist.append(JSONtoIntersectionState(e))
	
	return msg

def JSONtoIntersectionState(mydata):
	# Intersectionstate.msg
	# original asn1 type: SEQUENCE
	
	msg = Intersectionstate()
	if mydata.get("name"):
		msg.name = JSONtoDescriptiveName(mydata.get("name"))
	if mydata.get("id"):
		msg.id = JSONtoIntersectionReferenceID(mydata.get("id"))
	if mydata.get("revision"):
		msg.revision = JSONtoMsgCount(mydata.get("revision"))
	if mydata.get("status"):
		msg.status = JSONtoIntersectionStatusObject(mydata.get("status"))
	if mydata.get("moy"):
		msg.moy = JSONtoMinuteOfTheYear(mydata.get("moy"))
	if mydata.get("timeStamp"):
		msg.timestamp = JSONtoDSecond(mydata.get("timeStamp"))
	if mydata.get("enabledLanes"):
		msg.enabledlanes = JSONtoEnabledLaneList(mydata.get("enabledLanes"))
	if mydata.get("states"):
		msg.states = JSONtoMovementList(mydata.get("states"))
	if mydata.get("maneuverAssistList"):
		msg.maneuverassistlist = JSONtoManeuverAssistList(mydata.get("maneuverAssistList"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoIntersectionReferenceID(mydata):
	# Intersectionreferenceid.msg
	# original asn1 type: SEQUENCE
	
	msg = Intersectionreferenceid()
	if mydata.get("region"):
		msg.region = JSONtoRoadRegulatorID(mydata.get("region"))
	if mydata.get("id"):
		msg.id = JSONtoIntersectionID(mydata.get("id"))
	
	return msg

def JSONtoRoadRegulatorID(mydata):
	# Roadregulatorid.msg
	# original asn1 type: INTEGER
	
	msg = Roadregulatorid()
	msg.roadregulatorid = mydata
	
	return msg

def JSONtoIntersectionID(mydata):
	# Intersectionid.msg
	# original asn1 type: INTEGER
	
	msg = Intersectionid()
	msg.intersectionid = mydata
	
	return msg

def JSONtoMsgCount(mydata):
	# Msgcount.msg
	# original asn1 type: INTEGER
	
	msg = Msgcount()
	msg.msgcount = mydata
	
	return msg

def JSONtoIntersectionStatusObject(mydata):
	# Intersectionstatusobject.msg
	# original asn1 type: BIT STRING
	
	msg = Intersectionstatusobject()
	bitlength = mydata[1]
	bitstring = int.from_bytes(mydata[0], "big")
	listoftruth = list()
	while bitlength:
		if (bitstring & (1 << ((len(mydata[0])*8)-1))):
			listoftruth.append(1)
		else:
			listoftruth.append(0)
		bitstring = bitstring << 1
		bitlength = bitlength - 1
	msg.manualcontrolisenabled = listoftruth[0]
	msg.stoptimeisactivated = listoftruth[1]
	msg.failureflash = listoftruth[2]
	msg.preemptisactive = listoftruth[3]
	msg.signalpriorityisactive = listoftruth[4]
	msg.fixedtimeoperation = listoftruth[5]
	msg.trafficdependentoperation = listoftruth[6]
	msg.standbyoperation = listoftruth[7]
	msg.failuremode = listoftruth[8]
	msg.off = listoftruth[9]
	msg.recentmapmessageupdate = listoftruth[10]
	msg.recentchangeinmapassignedlanesidsused = listoftruth[11]
	msg.novalidmapisavailableatthistime = listoftruth[12]
	msg.novalidspatisavailableatthistime = listoftruth[13]
	
	return msg

def JSONtoDSecond(mydata):
	# Dsecond.msg
	# original asn1 type: INTEGER
	
	msg = Dsecond()
	msg.dsecond = mydata
	
	return msg

def JSONtoEnabledLaneList(mydata):
	# Enabledlanelist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Enabledlanelist()
	for e in mydata:
		msg.enabledlanelist.append(JSONtoLaneID(e))
	
	return msg

def JSONtoLaneID(mydata):
	# Laneid.msg
	# original asn1 type: INTEGER
	
	msg = Laneid()
	msg.laneid = mydata
	
	return msg

def JSONtoMovementList(mydata):
	# Movementlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Movementlist()
	for e in mydata:
		msg.movementlist.append(JSONtoMovementState(e))
	
	return msg

def JSONtoMovementState(mydata):
	# Movementstate.msg
	# original asn1 type: SEQUENCE
	
	msg = Movementstate()
	if mydata.get("movementName"):
		msg.movementname = JSONtoDescriptiveName(mydata.get("movementName"))
	if mydata.get("signalGroup"):
		msg.signalgroup = JSONtoSignalGroupID(mydata.get("signalGroup"))
	if mydata.get("state-time-speed"):
		msg.state_time_speed = JSONtoMovementEventList(mydata.get("state-time-speed"))
	if mydata.get("maneuverAssistList"):
		msg.maneuverassistlist = JSONtoManeuverAssistList(mydata.get("maneuverAssistList"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoSignalGroupID(mydata):
	# Signalgroupid.msg
	# original asn1 type: INTEGER
	
	msg = Signalgroupid()
	msg.signalgroupid = mydata
	
	return msg

def JSONtoMovementEventList(mydata):
	# Movementeventlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Movementeventlist()
	for e in mydata:
		msg.movementeventlist.append(JSONtoMovementEvent(e))
	
	return msg

def JSONtoMovementEvent(mydata):
	# Movementevent.msg
	# original asn1 type: SEQUENCE
	
	msg = Movementevent()
	if mydata.get("eventState"):
		msg.eventstate = JSONtoMovementPhaseState(mydata.get("eventState"))
	if mydata.get("timing"):
		msg.timing = JSONtoTimeChangeDetails(mydata.get("timing"))
	if mydata.get("speeds"):
		msg.speeds = JSONtoAdvisorySpeedList(mydata.get("speeds"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoMovementPhaseState(mydata):
	# Movementphasestate.msg
	# original asn1 type: ENUMERATED
	
	msg = Movementphasestate()
	msg.movementphasestate = mydata
	
	return msg

def JSONtoTimeChangeDetails(mydata):
	# Timechangedetails.msg
	# original asn1 type: SEQUENCE
	
	msg = Timechangedetails()
	if mydata.get("startTime"):
		msg.starttime = JSONtoTimeMark(mydata.get("startTime"))
	if mydata.get("minEndTime"):
		msg.minendtime = JSONtoTimeMark(mydata.get("minEndTime"))
	if mydata.get("maxEndTime"):
		msg.maxendtime = JSONtoTimeMark(mydata.get("maxEndTime"))
	if mydata.get("likelyTime"):
		msg.likelytime = JSONtoTimeMark(mydata.get("likelyTime"))
	if mydata.get("confidence"):
		msg.confidence = JSONtoTimeIntervalConfidence(mydata.get("confidence"))
	if mydata.get("nextTime"):
		msg.nexttime = JSONtoTimeMark(mydata.get("nextTime"))
	
	return msg

def JSONtoTimeMark(mydata):
	# Timemark.msg
	# original asn1 type: INTEGER
	
	msg = Timemark()
	msg.timemark = mydata
	
	return msg

def JSONtoTimeIntervalConfidence(mydata):
	# Timeintervalconfidence.msg
	# original asn1 type: INTEGER
	
	msg = Timeintervalconfidence()
	msg.timeintervalconfidence = mydata
	
	return msg

def JSONtoAdvisorySpeedList(mydata):
	# Advisoryspeedlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Advisoryspeedlist()
	for e in mydata:
		msg.advisoryspeedlist.append(JSONtoAdvisorySpeed(e))
	
	return msg

def JSONtoAdvisorySpeed(mydata):
	# Advisoryspeed.msg
	# original asn1 type: SEQUENCE
	
	msg = Advisoryspeed()
	if mydata.get("type"):
		msg.type = JSONtoAdvisorySpeedType(mydata.get("type"))
	if mydata.get("speed"):
		msg.speed = JSONtoSpeedAdvice(mydata.get("speed"))
	if mydata.get("confidence"):
		msg.confidence = JSONtoSpeedConfidenceDSRC(mydata.get("confidence"))
	if mydata.get("distance"):
		msg.distance = JSONtoZoneLength(mydata.get("distance"))
	if mydata.get("class"):
		msg.classname = JSONtoRestrictionClassID(mydata.get("class"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoAdvisorySpeedType(mydata):
	# Advisoryspeedtype.msg
	# original asn1 type: ENUMERATED
	
	msg = Advisoryspeedtype()
	msg.advisoryspeedtype = mydata
	
	return msg

def JSONtoSpeedAdvice(mydata):
	# Speedadvice.msg
	# original asn1 type: INTEGER
	
	msg = Speedadvice()
	msg.speedadvice = mydata
	
	return msg

def JSONtoSpeedConfidenceDSRC(mydata):
	# Speedconfidencedsrc.msg
	# original asn1 type: ENUMERATED
	
	msg = Speedconfidencedsrc()
	msg.speedconfidencedsrc = mydata
	
	return msg

def JSONtoZoneLength(mydata):
	# Zonelength.msg
	# original asn1 type: INTEGER
	
	msg = Zonelength()
	msg.zonelength = mydata
	
	return msg

def JSONtoRestrictionClassID(mydata):
	# Restrictionclassid.msg
	# original asn1 type: INTEGER
	
	msg = Restrictionclassid()
	msg.restrictionclassid = mydata
	
	return msg

def JSONtoRegionalExtension(mydata):
	# Regionalextension.msg
	# original asn1 type: SEQUENCE
	
	msg = Regionalextension()
	if mydata.get("regionId"):
		msg.regionid = JSONtoREG_EXT_ID_AND_TYPE(mydata.get("regionId"))
	if mydata.get("regExtValue"):
		msg.regextvalue = JSONtoREG_EXT_ID_AND_TYPE(mydata.get("regExtValue"))
	
	return msg

def JSONtoREG_EXT_ID_AND_TYPE(mydata):
	# Reg-ext-id-and-type.msg
	# original asn1 type: CLASS
	
	msg = Regextidandtype()
	
	return msg

def JSONtoManeuverAssistList(mydata):
	# Maneuverassistlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Maneuverassistlist()
	for e in mydata:
		msg.maneuverassistlist.append(JSONtoConnectionManeuverAssist(e))
	
	return msg

def JSONtoConnectionManeuverAssist(mydata):
	# Connectionmaneuverassist.msg
	# original asn1 type: SEQUENCE
	
	msg = Connectionmaneuverassist()
	if mydata.get("connectionID"):
		msg.connectionid = JSONtoLaneConnectionID(mydata.get("connectionID"))
	if mydata.get("queueLength"):
		msg.queuelength = JSONtoZoneLength(mydata.get("queueLength"))
	if mydata.get("availableStorageLength"):
		msg.availablestoragelength = JSONtoZoneLength(mydata.get("availableStorageLength"))
	if mydata.get("waitOnStop"):
		msg.waitonstop = JSONtoWaitOnStopline(mydata.get("waitOnStop"))
	if mydata.get("pedBicycleDetect"):
		msg.pedbicycledetect = JSONtoPedestrianBicycleDetect(mydata.get("pedBicycleDetect"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoLaneConnectionID(mydata):
	# Laneconnectionid.msg
	# original asn1 type: INTEGER
	
	msg = Laneconnectionid()
	msg.laneconnectionid = mydata
	
	return msg

def JSONtoWaitOnStopline(mydata):
	# Waitonstopline.msg
	# original asn1 type: BOOLEAN
	
	msg = Waitonstopline()
	msg.waitonstopline = mydata
	
	return msg

def JSONtoPedestrianBicycleDetect(mydata):
	# Pedestrianbicycledetect.msg
	# original asn1 type: BOOLEAN
	
	msg = Pedestrianbicycledetect()
	msg.pedestrianbicycledetect = mydata
	
	return msg
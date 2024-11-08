# Auto Generated by ASN1toROS2 tool
from v2x_cohdainterfaces.msg import *

def JSONtoMAPEM(mydata):
	# Mapem.msg
	# original asn1 type: SEQUENCE
	
	msg = Mapem()
	if mydata.get("header"):
		msg.header = JSONtoItsPduHeader(mydata.get("header"))
	if mydata.get("map"):
		msg.map = JSONtoMapData(mydata.get("map"))
	
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

def JSONtoMapData(mydata):
	# Mapdata.msg
	# original asn1 type: SEQUENCE
	
	msg = Mapdata()
	if mydata.get("timeStamp"):
		msg.timestamp = JSONtoMinuteOfTheYear(mydata.get("timeStamp"))
	if mydata.get("msgIssueRevision"):
		msg.msgissuerevision = JSONtoMsgCount(mydata.get("msgIssueRevision"))
	if mydata.get("layerType"):
		msg.layertype = JSONtoLayerType(mydata.get("layerType"))
	if mydata.get("layerID"):
		msg.layerid = JSONtoLayerID(mydata.get("layerID"))
	if mydata.get("intersections"):
		msg.intersections = JSONtoIntersectionGeometryList(mydata.get("intersections"))
	if mydata.get("roadSegments"):
		msg.roadsegments = JSONtoRoadSegmentList(mydata.get("roadSegments"))
	if mydata.get("dataParameters"):
		msg.dataparameters = JSONtoDataParameters(mydata.get("dataParameters"))
	if mydata.get("restrictionList"):
		msg.restrictionlist = JSONtoRestrictionClassList(mydata.get("restrictionList"))
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

def JSONtoMsgCount(mydata):
	# Msgcount.msg
	# original asn1 type: INTEGER
	
	msg = Msgcount()
	msg.msgcount = mydata
	
	return msg

def JSONtoLayerType(mydata):
	# Layertype.msg
	# original asn1 type: ENUMERATED
	
	msg = Layertype()
	msg.layertype = mydata
	
	return msg

def JSONtoLayerID(mydata):
	# Layerid.msg
	# original asn1 type: INTEGER
	
	msg = Layerid()
	msg.layerid = mydata
	
	return msg

def JSONtoIntersectionGeometryList(mydata):
	# Intersectiongeometrylist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Intersectiongeometrylist()
	for e in mydata:
		msg.intersectiongeometrylist.append(JSONtoIntersectionGeometry(e))
	
	return msg

def JSONtoIntersectionGeometry(mydata):
	# Intersectiongeometry.msg
	# original asn1 type: SEQUENCE
	
	msg = Intersectiongeometry()
	if mydata.get("name"):
		msg.name = JSONtoDescriptiveName(mydata.get("name"))
	if mydata.get("id"):
		msg.id = JSONtoIntersectionReferenceID(mydata.get("id"))
	if mydata.get("revision"):
		msg.revision = JSONtoMsgCount(mydata.get("revision"))
	if mydata.get("refPoint"):
		msg.refpoint = JSONtoPosition3D(mydata.get("refPoint"))
	if mydata.get("laneWidth"):
		msg.lanewidth = JSONtoLaneWidth(mydata.get("laneWidth"))
	if mydata.get("speedLimits"):
		msg.speedlimits = JSONtoSpeedLimitList(mydata.get("speedLimits"))
	if mydata.get("laneSet"):
		msg.laneset = JSONtoLaneList(mydata.get("laneSet"))
	if mydata.get("preemptPriorityData"):
		msg.preemptprioritydata = JSONtoPreemptPriorityList(mydata.get("preemptPriorityData"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoDescriptiveName(mydata):
	# Descriptivename.msg
	# original asn1 type: IA5String
	
	msg = Descriptivename()
	msg.descriptivename = mydata
	
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

def JSONtoPosition3D(mydata):
	# Position3d.msg
	# original asn1 type: SEQUENCE
	
	msg = Position3d()
	if mydata.get("lat"):
		msg.lat = JSONtoLatitude(mydata.get("lat"))
	if mydata.get("long"):
		msg.lon = JSONtoLongitude(mydata.get("long"))
	if mydata.get("elevation"):
		msg.elevation = JSONtoElevation(mydata.get("elevation"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoLatitude(mydata):
	# Latitude.msg
	# original asn1 type: INTEGER
	
	msg = Latitude()
	msg.latitude = mydata
	
	return msg

def JSONtoLongitude(mydata):
	# Longitude.msg
	# original asn1 type: INTEGER
	
	msg = Longitude()
	msg.longitude = mydata
	
	return msg

def JSONtoElevation(mydata):
	# Elevation.msg
	# original asn1 type: INTEGER
	
	msg = Elevation()
	msg.elevation = mydata
	
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

def JSONtoLaneWidth(mydata):
	# Lanewidth.msg
	# original asn1 type: INTEGER
	
	msg = Lanewidth()
	msg.lanewidth = mydata
	
	return msg

def JSONtoSpeedLimitList(mydata):
	# Speedlimitlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Speedlimitlist()
	for e in mydata:
		msg.speedlimitlist.append(JSONtoRegulatorySpeedLimit(e))
	
	return msg

def JSONtoRegulatorySpeedLimit(mydata):
	# Regulatoryspeedlimit.msg
	# original asn1 type: SEQUENCE
	
	msg = Regulatoryspeedlimit()
	if mydata.get("type"):
		msg.type = JSONtoSpeedLimitType(mydata.get("type"))
	if mydata.get("speed"):
		msg.speed = JSONtoVelocity(mydata.get("speed"))
	
	return msg

def JSONtoSpeedLimitType(mydata):
	# Speedlimittype.msg
	# original asn1 type: ENUMERATED
	
	msg = Speedlimittype()
	msg.speedlimittype = mydata
	
	return msg

def JSONtoVelocity(mydata):
	# Velocity.msg
	# original asn1 type: INTEGER
	
	msg = Velocity()
	msg.velocity = mydata
	
	return msg

def JSONtoLaneList(mydata):
	# Lanelist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Lanelist()
	for e in mydata:
		msg.lanelist.append(JSONtoGenericLane(e))
	
	return msg

def JSONtoGenericLane(mydata):
	# Genericlane.msg
	# original asn1 type: SEQUENCE
	
	msg = Genericlane()
	if mydata.get("laneID"):
		msg.laneid = JSONtoLaneID(mydata.get("laneID"))
	if mydata.get("name"):
		msg.name = JSONtoDescriptiveName(mydata.get("name"))
	if mydata.get("ingressApproach"):
		msg.ingressapproach = JSONtoApproachID(mydata.get("ingressApproach"))
	if mydata.get("egressApproach"):
		msg.egressapproach = JSONtoApproachID(mydata.get("egressApproach"))
	if mydata.get("laneAttributes"):
		msg.laneattributes = JSONtoLaneAttributes(mydata.get("laneAttributes"))
	if mydata.get("maneuvers"):
		msg.maneuvers = JSONtoAllowedManeuvers(mydata.get("maneuvers"))
	if mydata.get("nodeList"):
		msg.nodelist = JSONtoNodeListXY(mydata.get("nodeList"))
	if mydata.get("connectsTo"):
		msg.connectsto = JSONtoConnectsToList(mydata.get("connectsTo"))
	if mydata.get("overlays"):
		msg.overlays = JSONtoOverlayLaneList(mydata.get("overlays"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoLaneID(mydata):
	# Laneid.msg
	# original asn1 type: INTEGER
	
	msg = Laneid()
	msg.laneid = mydata
	
	return msg

def JSONtoApproachID(mydata):
	# Approachid.msg
	# original asn1 type: INTEGER
	
	msg = Approachid()
	msg.approachid = mydata
	
	return msg

def JSONtoLaneAttributes(mydata):
	# Laneattributes.msg
	# original asn1 type: SEQUENCE
	
	msg = Laneattributes()
	if mydata.get("directionalUse"):
		msg.directionaluse = JSONtoLaneDirection(mydata.get("directionalUse"))
	if mydata.get("sharedWith"):
		msg.sharedwith = JSONtoLaneSharing(mydata.get("sharedWith"))
	if mydata.get("laneType"):
		msg.lanetype = JSONtoLaneTypeAttributes(mydata.get("laneType"))
	if mydata.get("regional"):
		msg.regional = JSONtoRegionalExtension(mydata.get("regional"))
	
	return msg

def JSONtoLaneDirection(mydata):
	# Lanedirection.msg
	# original asn1 type: BIT STRING
	
	msg = Lanedirection()
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
	msg.ingresspath = listoftruth[0]
	msg.egresspath = listoftruth[1]
	
	return msg

def JSONtoLaneSharing(mydata):
	# Lanesharing.msg
	# original asn1 type: BIT STRING
	
	msg = Lanesharing()
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
	msg.overlappinglanedescriptionprovided = listoftruth[0]
	msg.multiplelanestreatedasonelane = listoftruth[1]
	msg.othernonmotorizedtraffictypes = listoftruth[2]
	msg.individualmotorizedvehicletraffic = listoftruth[3]
	msg.busvehicletraffic = listoftruth[4]
	msg.taxivehicletraffic = listoftruth[5]
	msg.pedestrianstraffic = listoftruth[6]
	msg.cyclistvehicletraffic = listoftruth[7]
	msg.trackedvehicletraffic = listoftruth[8]
	msg.pedestriantraffic = listoftruth[9]
	
	return msg

def JSONtoLaneTypeAttributes(mydata):
	# Lanetypeattributes.msg
	# original asn1 type: CHOICE
	
	msg = Lanetypeattributes()
	chosendata = mydata[1]
	if mydata[0] == "vehicle":
		msg.vehicle.append(JSONtoLaneAttributes_Vehicle(chosendata))
	if mydata[0] == "crosswalk":
		msg.crosswalk.append(JSONtoLaneAttributes_Crosswalk(chosendata))
	if mydata[0] == "bikeLane":
		msg.bikelane.append(JSONtoLaneAttributes_Bike(chosendata))
	if mydata[0] == "sidewalk":
		msg.sidewalk.append(JSONtoLaneAttributes_Sidewalk(chosendata))
	if mydata[0] == "median":
		msg.median.append(JSONtoLaneAttributes_Barrier(chosendata))
	if mydata[0] == "striping":
		msg.striping.append(JSONtoLaneAttributes_Striping(chosendata))
	if mydata[0] == "trackedVehicle":
		msg.trackedvehicle.append(JSONtoLaneAttributes_TrackedVehicle(chosendata))
	if mydata[0] == "parking":
		msg.parking.append(JSONtoLaneAttributes_Parking(chosendata))
	
	return msg

def JSONtoLaneAttributes_Vehicle(mydata):
	# Laneattributes-vehicle.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributesvehicle()
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
	msg.isvehiclerevocablelane = listoftruth[0]
	msg.isvehicleflyoverlane = listoftruth[1]
	msg.hovlaneuseonly = listoftruth[2]
	msg.restrictedtobususe = listoftruth[3]
	msg.restrictedtotaxiuse = listoftruth[4]
	msg.restrictedfrompublicuse = listoftruth[5]
	msg.hasirbeaconcoverage = listoftruth[6]
	msg.permissiononrequest = listoftruth[7]
	
	return msg

def JSONtoLaneAttributes_Crosswalk(mydata):
	# Laneattributes-crosswalk.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributescrosswalk()
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
	msg.crosswalkrevocablelane = listoftruth[0]
	msg.bicyleuseallowed = listoftruth[1]
	msg.isxwalkflyoverlane = listoftruth[2]
	msg.fixedcycletime = listoftruth[3]
	msg.bidirectionalcycletimes = listoftruth[4]
	msg.haspushtowalkbutton = listoftruth[5]
	msg.audiosupport = listoftruth[6]
	msg.rfsignalrequestpresent = listoftruth[7]
	msg.unsignalizedsegmentspresent = listoftruth[8]
	
	return msg

def JSONtoLaneAttributes_Bike(mydata):
	# Laneattributes-bike.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributesbike()
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
	msg.bikerevocablelane = listoftruth[0]
	msg.pedestrianuseallowed = listoftruth[1]
	msg.isbikeflyoverlane = listoftruth[2]
	msg.fixedcycletime = listoftruth[3]
	msg.bidirectionalcycletimes = listoftruth[4]
	msg.isolatedbybarrier = listoftruth[5]
	msg.unsignalizedsegmentspresent = listoftruth[6]
	
	return msg

def JSONtoLaneAttributes_Sidewalk(mydata):
	# Laneattributes-sidewalk.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributessidewalk()
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
	msg.sidewalk_revocablelane = listoftruth[0]
	msg.bicyleuseallowed = listoftruth[1]
	msg.issidewalkflyoverlane = listoftruth[2]
	msg.walkbikes = listoftruth[3]
	
	return msg

def JSONtoLaneAttributes_Barrier(mydata):
	# Laneattributes-barrier.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributesbarrier()
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
	msg.median_revocablelane = listoftruth[0]
	msg.median = listoftruth[1]
	msg.whitelinehashing = listoftruth[2]
	msg.stripedlines = listoftruth[3]
	msg.doublestripedlines = listoftruth[4]
	msg.trafficcones = listoftruth[5]
	msg.constructionbarrier = listoftruth[6]
	msg.trafficchannels = listoftruth[7]
	msg.lowcurbs = listoftruth[8]
	msg.highcurbs = listoftruth[9]
	
	return msg

def JSONtoLaneAttributes_Striping(mydata):
	# Laneattributes-striping.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributesstriping()
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
	msg.stripetoconnectinglanesrevocablelane = listoftruth[0]
	msg.stripedrawonleft = listoftruth[1]
	msg.stripedrawonright = listoftruth[2]
	msg.stripetoconnectinglanesleft = listoftruth[3]
	msg.stripetoconnectinglanesright = listoftruth[4]
	msg.stripetoconnectinglanesahead = listoftruth[5]
	
	return msg

def JSONtoLaneAttributes_TrackedVehicle(mydata):
	# Laneattributes-trackedvehicle.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributestrackedvehicle()
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
	msg.spec_revocablelane = listoftruth[0]
	msg.spec_commuterrailroadtrack = listoftruth[1]
	msg.spec_lightrailroadtrack = listoftruth[2]
	msg.spec_heavyrailroadtrack = listoftruth[3]
	msg.spec_otherrailtype = listoftruth[4]
	
	return msg

def JSONtoLaneAttributes_Parking(mydata):
	# Laneattributes-parking.msg
	# original asn1 type: BIT STRING
	
	msg = Laneattributesparking()
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
	msg.parkingrevocablelane = listoftruth[0]
	msg.parallelparkinginuse = listoftruth[1]
	msg.headinparkinginuse = listoftruth[2]
	msg.donotparkzone = listoftruth[3]
	msg.parkingforbususe = listoftruth[4]
	msg.parkingfortaxiuse = listoftruth[5]
	msg.nopublicparkinguse = listoftruth[6]
	
	return msg

def JSONtoAllowedManeuvers(mydata):
	# Allowedmaneuvers.msg
	# original asn1 type: BIT STRING
	
	msg = Allowedmaneuvers()
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
	msg.maneuverstraightallowed = listoftruth[0]
	msg.maneuverleftallowed = listoftruth[1]
	msg.maneuverrightallowed = listoftruth[2]
	msg.maneuveruturnallowed = listoftruth[3]
	msg.maneuverleftturnonredallowed = listoftruth[4]
	msg.maneuverrightturnonredallowed = listoftruth[5]
	msg.maneuverlanechangeallowed = listoftruth[6]
	msg.maneuvernostoppingallowed = listoftruth[7]
	msg.yieldallwaysrequired = listoftruth[8]
	msg.gowithhalt = listoftruth[9]
	msg.caution = listoftruth[10]
	msg.reserved1 = listoftruth[11]
	
	return msg

def JSONtoNodeListXY(mydata):
	# Nodelistxy.msg
	# original asn1 type: CHOICE
	
	msg = Nodelistxy()
	chosendata = mydata[1]
	if mydata[0] == "nodes":
		msg.nodes.append(JSONtoNodeSetXY(chosendata))
	if mydata[0] == "computed":
		msg.computed.append(JSONtoComputedLane(chosendata))
	
	return msg

def JSONtoNodeSetXY(mydata):
	# Nodesetxy.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Nodesetxy()
	for e in mydata:
		msg.nodesetxy.append(JSONtoNodeXY(e))
	
	return msg

def JSONtoNodeXY(mydata):
	# Nodexy.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy()
	if mydata.get("delta"):
		msg.delta = JSONtoNodeOffsetPointXY(mydata.get("delta"))
	if mydata.get("attributes"):
		msg.attributes = JSONtoNodeAttributeSetXY(mydata.get("attributes"))
	
	return msg

def JSONtoNodeOffsetPointXY(mydata):
	# Nodeoffsetpointxy.msg
	# original asn1 type: CHOICE
	
	msg = Nodeoffsetpointxy()
	chosendata = mydata[1]
	if mydata[0] == "node-XY1":
		msg.node_xy1.append(JSONtoNode_XY_20b(chosendata))
	if mydata[0] == "node-XY2":
		msg.node_xy2.append(JSONtoNode_XY_22b(chosendata))
	if mydata[0] == "node-XY3":
		msg.node_xy3.append(JSONtoNode_XY_24b(chosendata))
	if mydata[0] == "node-XY4":
		msg.node_xy4.append(JSONtoNode_XY_26b(chosendata))
	if mydata[0] == "node-XY5":
		msg.node_xy5.append(JSONtoNode_XY_28b(chosendata))
	if mydata[0] == "node-XY6":
		msg.node_xy6.append(JSONtoNode_XY_32b(chosendata))
	if mydata[0] == "node-LatLon":
		msg.node_latlon.append(JSONtoNode_LLmD_64b(chosendata))
	if mydata[0] == "regional":
		msg.regional.append(JSONtoRegionalExtension(chosendata))
	
	return msg

def JSONtoNode_XY_20b(mydata):
	# Node-xy-20b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy20b()
	if mydata.get("x"):
		msg.x = JSONtoOffset_B10(mydata.get("x"))
	if mydata.get("y"):
		msg.y = JSONtoOffset_B10(mydata.get("y"))
	
	return msg

def JSONtoOffset_B10(mydata):
	# Offset-b10.msg
	# original asn1 type: INTEGER
	
	msg = Offsetb10()
	msg.offset_b10 = mydata
	
	return msg

def JSONtoNode_XY_22b(mydata):
	# Node-xy-22b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy22b()
	if mydata.get("x"):
		msg.x = JSONtoOffset_B11(mydata.get("x"))
	if mydata.get("y"):
		msg.y = JSONtoOffset_B11(mydata.get("y"))
	
	return msg

def JSONtoOffset_B11(mydata):
	# Offset-b11.msg
	# original asn1 type: INTEGER
	
	msg = Offsetb11()
	msg.offset_b11 = mydata
	
	return msg

def JSONtoNode_XY_24b(mydata):
	# Node-xy-24b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy24b()
	if mydata.get("x"):
		msg.x = JSONtoOffset_B12(mydata.get("x"))
	if mydata.get("y"):
		msg.y = JSONtoOffset_B12(mydata.get("y"))
	
	return msg

def JSONtoOffset_B12(mydata):
	# Offset-b12.msg
	# original asn1 type: INTEGER
	
	msg = Offsetb12()
	msg.offset_b12 = mydata
	
	return msg

def JSONtoNode_XY_26b(mydata):
	# Node-xy-26b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy26b()
	if mydata.get("x"):
		msg.x = JSONtoOffset_B13(mydata.get("x"))
	if mydata.get("y"):
		msg.y = JSONtoOffset_B13(mydata.get("y"))
	
	return msg

def JSONtoOffset_B13(mydata):
	# Offset-b13.msg
	# original asn1 type: INTEGER
	
	msg = Offsetb13()
	msg.offset_b13 = mydata
	
	return msg

def JSONtoNode_XY_28b(mydata):
	# Node-xy-28b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy28b()
	if mydata.get("x"):
		msg.x = JSONtoOffset_B14(mydata.get("x"))
	if mydata.get("y"):
		msg.y = JSONtoOffset_B14(mydata.get("y"))
	
	return msg

def JSONtoOffset_B14(mydata):
	# Offset-b14.msg
	# original asn1 type: INTEGER
	
	msg = Offsetb14()
	msg.offset_b14 = mydata
	
	return msg

def JSONtoNode_XY_32b(mydata):
	# Node-xy-32b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodexy32b()
	if mydata.get("x"):
		msg.x = JSONtoOffset_B16(mydata.get("x"))
	if mydata.get("y"):
		msg.y = JSONtoOffset_B16(mydata.get("y"))
	
	return msg

def JSONtoOffset_B16(mydata):
	# Offset-b16.msg
	# original asn1 type: INTEGER
	
	msg = Offsetb16()
	msg.offset_b16 = mydata
	
	return msg

def JSONtoNode_LLmD_64b(mydata):
	# Node-llmd-64b.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodellmd64b()
	if mydata.get("lon"):
		msg.lon = JSONtoLongitude(mydata.get("lon"))
	if mydata.get("lat"):
		msg.lat = JSONtoLatitude(mydata.get("lat"))
	
	return msg

def JSONtoNodeAttributeSetXY(mydata):
	# Nodeattributesetxy.msg
	# original asn1 type: SEQUENCE
	
	msg = Nodeattributesetxy()
	if mydata.get("localNode"):
		msg.localnode = JSONtoNodeAttributeXYList(mydata.get("localNode"))
	if mydata.get("disabled"):
		msg.disabled = JSONtoSegmentAttributeXYList(mydata.get("disabled"))
	if mydata.get("enabled"):
		msg.enabled = JSONtoSegmentAttributeXYList(mydata.get("enabled"))
	if mydata.get("data"):
		msg.data = JSONtoLaneDataAttributeList(mydata.get("data"))
	if mydata.get("dWidth"):
		msg.dwidth = JSONtoOffset_B10(mydata.get("dWidth"))
	if mydata.get("dElevation"):
		msg.delevation = JSONtoOffset_B10(mydata.get("dElevation"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoNodeAttributeXYList(mydata):
	# Nodeattributexylist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Nodeattributexylist()
	for e in mydata:
		msg.nodeattributexylist.append(JSONtoNodeAttributeXY(e))
	
	return msg

def JSONtoNodeAttributeXY(mydata):
	# Nodeattributexy.msg
	# original asn1 type: ENUMERATED
	
	msg = Nodeattributexy()
	msg.nodeattributexy = mydata
	
	return msg

def JSONtoSegmentAttributeXYList(mydata):
	# Segmentattributexylist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Segmentattributexylist()
	for e in mydata:
		msg.segmentattributexylist.append(JSONtoSegmentAttributeXY(e))
	
	return msg

def JSONtoSegmentAttributeXY(mydata):
	# Segmentattributexy.msg
	# original asn1 type: ENUMERATED
	
	msg = Segmentattributexy()
	msg.segmentattributexy = mydata
	
	return msg

def JSONtoLaneDataAttributeList(mydata):
	# Lanedataattributelist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Lanedataattributelist()
	for e in mydata:
		msg.lanedataattributelist.append(JSONtoLaneDataAttribute(e))
	
	return msg

def JSONtoLaneDataAttribute(mydata):
	# Lanedataattribute.msg
	# original asn1 type: CHOICE
	
	msg = Lanedataattribute()
	chosendata = mydata[1]
	if mydata[0] == "pathEndPointAngle":
		msg.pathendpointangle.append(JSONtoDeltaAngle(chosendata))
	if mydata[0] == "laneCrownPointCenter":
		msg.lanecrownpointcenter.append(JSONtoRoadwayCrownAngle(chosendata))
	if mydata[0] == "laneCrownPointLeft":
		msg.lanecrownpointleft.append(JSONtoRoadwayCrownAngle(chosendata))
	if mydata[0] == "laneCrownPointRight":
		msg.lanecrownpointright.append(JSONtoRoadwayCrownAngle(chosendata))
	if mydata[0] == "laneAngle":
		msg.laneangle.append(JSONtoMergeDivergeNodeAngle(chosendata))
	if mydata[0] == "speedLimits":
		msg.speedlimits.append(JSONtoSpeedLimitList(chosendata))
	for e in mydata[0]:
		if mydata[0][0] == "regional":
			msg.regional.append(JSONtoRegionalExtension(chosendata))
	
	return msg

def JSONtoDeltaAngle(mydata):
	# Deltaangle.msg
	# original asn1 type: INTEGER
	
	msg = Deltaangle()
	msg.deltaangle = mydata
	
	return msg

def JSONtoRoadwayCrownAngle(mydata):
	# Roadwaycrownangle.msg
	# original asn1 type: INTEGER
	
	msg = Roadwaycrownangle()
	msg.roadwaycrownangle = mydata
	
	return msg

def JSONtoMergeDivergeNodeAngle(mydata):
	# Mergedivergenodeangle.msg
	# original asn1 type: INTEGER
	
	msg = Mergedivergenodeangle()
	msg.mergedivergenodeangle = mydata
	
	return msg

def JSONtoComputedLane(mydata):
	# ComputedLane.msg
	# original asn1 type: SEQUENCE
	
	msg = Computedlane()
	if mydata.get("referenceLaneId"):
		msg.referencelaneid = JSONtoLaneID(mydata.get("referenceLaneId"))
	if mydata.get("offsetXaxis"):
		offx = mydata.get("offsetXaxis")
		if offx[1] == "DrivenLineOffsetSm":
			msg.offsetxaxissmall.append(JSONtoLaneID(offx[1]))
		elif offx[1] == "DrivenLineOffsetLg":
			msg.offsetxaxislarge.append(JSONtoLaneID(offx[1]))
	if mydata.get("offsetYaxis"):
		offy = mydata.get("offsetYaxis")
		if offy[1] == "DrivenLineOffsetSm":
			msg.offsetyaxissmall.append(JSONtoLaneID(offx[1]))
		elif offy[1] == "DrivenLineOffsetLg":
			msg.offsetyaxislarge.append(JSONtoLaneID(offx[1]))
	if mydata.get("rotateXY"):
		msg.rotatexy = JSONtoAngle(mydata.get("rotateXY"))
	if mydata.get("scaleXaxis"):
		msg.scalexaxis = JSONtoScale_B12(mydata.get("scaleXaxis"))
	if mydata.get("scaleYaxis"):
		msg.scaleyaxis = JSONtoScale_B12(mydata.get("scaleYaxis"))
	if mydata.get("regional"):
		msg.regional = JSONtoRegionalExtension(mydata.get("regional"))
	
	return msg

def JSONtoDrivenLineOffsetLg(mydata):
	# Drivenlineoffsetlg.msg
	# original asn1 type: INTEGER
	
	msg = Drivenlineoffsetlg()
	msg.drivenlineoffsetlg = mydata
	
	return msg

def JSONtoDrivenLineOffsetSm(mydata):
	# Drivenlineoffsetsm.msg
	# original asn1 type: INTEGER
	
	msg = Drivenlineoffsetsm()
	msg.drivenlineoffsetsm = mydata
	
	return msg

def JSONtoAngle(mydata):
	# Angle.msg
	# original asn1 type: INTEGER
	
	msg = Angle()
	msg.angle = mydata
	
	return msg

def JSONtoScale_B12(mydata):
	# Scale-b12.msg
	# original asn1 type: INTEGER
	
	msg = Scaleb12()
	msg.scale_b12 = mydata
	
	return msg

def JSONtoConnectsToList(mydata):
	# Connectstolist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Connectstolist()
	for e in mydata:
		msg.connectstolist.append(JSONtoConnection(e))
	
	return msg

def JSONtoConnection(mydata):
	# Connection.msg
	# original asn1 type: SEQUENCE
	
	msg = Connection()
	if mydata.get("connectingLane"):
		msg.connectinglane = JSONtoConnectingLane(mydata.get("connectingLane"))
	if mydata.get("remoteIntersection"):
		msg.remoteintersection = JSONtoIntersectionReferenceID(mydata.get("remoteIntersection"))
	if mydata.get("signalGroup"):
		msg.signalgroup = JSONtoSignalGroupID(mydata.get("signalGroup"))
	if mydata.get("userClass"):
		msg.userclass = JSONtoRestrictionClassID(mydata.get("userClass"))
	if mydata.get("connectionID"):
		msg.connectionid = JSONtoLaneConnectionID(mydata.get("connectionID"))
	
	return msg

def JSONtoConnectingLane(mydata):
	# Connectinglane.msg
	# original asn1 type: SEQUENCE
	
	msg = Connectinglane()
	if mydata.get("lane"):
		msg.lane = JSONtoLaneID(mydata.get("lane"))
	if mydata.get("maneuver"):
		msg.maneuver = JSONtoAllowedManeuvers(mydata.get("maneuver"))
	
	return msg

def JSONtoSignalGroupID(mydata):
	# Signalgroupid.msg
	# original asn1 type: INTEGER
	
	msg = Signalgroupid()
	msg.signalgroupid = mydata
	
	return msg

def JSONtoRestrictionClassID(mydata):
	# Restrictionclassid.msg
	# original asn1 type: INTEGER
	
	msg = Restrictionclassid()
	msg.restrictionclassid = mydata
	
	return msg

def JSONtoLaneConnectionID(mydata):
	# Laneconnectionid.msg
	# original asn1 type: INTEGER
	
	msg = Laneconnectionid()
	msg.laneconnectionid = mydata
	
	return msg

def JSONtoOverlayLaneList(mydata):
	# Overlaylanelist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Overlaylanelist()
	for e in mydata:
		msg.overlaylanelist.append(JSONtoLaneID(e))
	
	return msg

def JSONtoPreemptPriorityList(mydata):
	# Preemptprioritylist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Preemptprioritylist()
	for e in mydata:
		msg.preemptprioritylist.append(JSONtoSignalControlZone(e))
	
	return msg

def JSONtoSignalControlZone(mydata):
	# Signalcontrolzone.msg
	# original asn1 type: SEQUENCE
	
	msg = Signalcontrolzone()
	if mydata.get("zone"):
		msg.zone = JSONtoRegionalExtension(mydata.get("zone"))
	
	return msg

def JSONtoRoadSegmentList(mydata):
	# Roadsegmentlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Roadsegmentlist()
	for e in mydata:
		msg.roadsegmentlist.append(JSONtoRoadSegment(e))
	
	return msg

def JSONtoRoadSegment(mydata):
	# Roadsegment.msg
	# original asn1 type: SEQUENCE
	
	msg = Roadsegment()
	if mydata.get("name"):
		msg.name = JSONtoDescriptiveName(mydata.get("name"))
	if mydata.get("id"):
		msg.id = JSONtoRoadSegmentReferenceID(mydata.get("id"))
	if mydata.get("revision"):
		msg.revision = JSONtoMsgCount(mydata.get("revision"))
	if mydata.get("refPoint"):
		msg.refpoint = JSONtoPosition3D(mydata.get("refPoint"))
	if mydata.get("laneWidth"):
		msg.lanewidth = JSONtoLaneWidth(mydata.get("laneWidth"))
	if mydata.get("speedLimits"):
		msg.speedlimits = JSONtoSpeedLimitList(mydata.get("speedLimits"))
	if mydata.get("roadLaneSet"):
		msg.roadlaneset = JSONtoRoadLaneSetList(mydata.get("roadLaneSet"))
	if mydata.get("regional"):
		for e in mydata.get("regional"):
			msg.regional.append(JSONtoRegionalExtension(e))
	
	return msg

def JSONtoRoadSegmentReferenceID(mydata):
	# Roadsegmentreferenceid.msg
	# original asn1 type: SEQUENCE
	
	msg = Roadsegmentreferenceid()
	if mydata.get("region"):
		msg.region = JSONtoRoadRegulatorID(mydata.get("region"))
	if mydata.get("id"):
		msg.id = JSONtoRoadSegmentID(mydata.get("id"))
	
	return msg

def JSONtoRoadSegmentID(mydata):
	# Roadsegmentid.msg
	# original asn1 type: INTEGER
	
	msg = Roadsegmentid()
	msg.roadsegmentid = mydata
	
	return msg

def JSONtoRoadLaneSetList(mydata):
	# Roadlanesetlist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Roadlanesetlist()
	for e in mydata:
		msg.roadlanesetlist.append(JSONtoGenericLane(e))
	
	return msg

def JSONtoDataParameters(mydata):
	# Dataparameters.msg
	# original asn1 type: SEQUENCE
	
	msg = Dataparameters()
	if mydata.get("processMethod"):
		msg.processmethod = mydata.processMethod
	if mydata.get("processAgency"):
		msg.processagency = mydata.processAgency
	if mydata.get("lastCheckedDate"):
		msg.lastcheckeddate = mydata.lastCheckedDate
	if mydata.get("geoidUsed"):
		msg.geoidused = mydata.geoidUsed
	
	return msg

def JSONtoRestrictionClassList(mydata):
	# Restrictionclasslist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Restrictionclasslist()
	for e in mydata:
		msg.restrictionclasslist.append(JSONtoRestrictionClassAssignment(e))
	
	return msg

def JSONtoRestrictionClassAssignment(mydata):
	# Restrictionclassassignment.msg
	# original asn1 type: SEQUENCE
	
	msg = Restrictionclassassignment()
	if mydata.get("id"):
		msg.id = JSONtoRestrictionClassID(mydata.get("id"))
	if mydata.get("users"):
		msg.users = JSONtoRestrictionUserTypeList(mydata.get("users"))
	
	return msg

def JSONtoRestrictionUserTypeList(mydata):
	# Restrictionusertypelist.msg
	# original asn1 type: SEQUENCEOF
	
	msg = Restrictionusertypelist()
	for e in mydata:
		msg.restrictionusertypelist.append(JSONtoRestrictionUserType(e))
	
	return msg

def JSONtoRestrictionUserType(mydata):
	# Restrictionusertype.msg
	# original asn1 type: CHOICE
	
	msg = Restrictionusertype()
	chosendata = mydata[1]
	if mydata[0] == "basicType":
		msg.basictype.append(JSONtoRestrictionAppliesTo(chosendata))
	for e in mydata[0]:
		if mydata[0][0] == "regional":
			msg.regional.append(JSONtoRegionalExtension(chosendata))
	
	return msg

def JSONtoRestrictionAppliesTo(mydata):
	# Restrictionappliesto.msg
	# original asn1 type: ENUMERATED
	
	msg = Restrictionappliesto()
	msg.restrictionappliesto = mydata
	
	return msg

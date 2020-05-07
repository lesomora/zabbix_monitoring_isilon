#!/usr/bin/python 
import isi_sdk_8_0
from isi_sdk_8_0.rest import ApiException
import json 

def ISISnapShot(Client): 
	instance = isi_sdk_8_0.SnapshotApi(Client)
	try: 
		api_response = instance.get_snapshot_snapshots_summary()
		dic = api_response.to_dict() 
		return dic
	except: 
		pass 

def ISINodeDisc(Client, key): 
	instance = isi_sdk_8_0.StatisticsApi(Client)
	devid = ['all']
	try: 
		api_response = instance.get_statistics_current(keys=key, key=key, timeout='56', devid=devid, substr='true', degraded='true', expand_clientid='true')
		r =  api_response.to_dict()
		data = []
    		for abc in (r['stats']):
        		id = (abc['devid']) 
        		data.append({'{#NID}':"%s" %(id)}) 
    		reply = json.dumps({'data':data})
   		return reply 
	except: 
		pass 

def ISINodeNFSBalance(Client, key, node): 
	instance = isi_sdk_8_0.StatisticsApi(Client)
	devid = ['all']
	try: 
		api_response = instance.get_statistics_current(keys=key, key=key, timeout='56', devid=devid, substr='true', degraded='true', expand_clientid='true')
                r =  api_response.to_dict()
		for values in r['stats']: 
			r1 = [values[x] for x in 'devid', 'value']
			if int(node) == r1[0]: 
				return (r1[1])
	except: 
		pass 

def ISIGetNodeInformation(Client, node): 
	instance = isi_sdk_8_0.ClusterApi(Client)
	try: 
		api_response = instance.get_cluster_node(node)
		return api_response.to_dict() 
	except: 
		pass 

def ISINodeDiskDiscovery(Client): 
	instance = isi_sdk_8_0.ClusterApi(Client)
	DN = []
	try: 
		api_response = instance.get_cluster_nodes()
		dic = api_response.to_dict() 	
		for values in dic['nodes']:
			for diskname in values['drives']: 
				devicename = (diskname['devname'])
				if len(devicename) > 0: 
					DN.append({"{#DEVICENAME}":"%s" %(devicename), "{#NODEID}":"%s"%(values['id'])})	             
				else: 
					pass

	except: 
		pass
    	reply = json.dumps({'data':DN})
	return reply
#!/usr/bin/python
import argparse 
from connection import ISIConnection
c = ISIConnection()

def run(args): 
	Client = c.Conn(args.hostname)
	if args.item == 'snapshot': 
		from isi_functions import ISISnapShot
		r = ISISnapShot(Client)
		print (r) 
	elif args.item == 'nodediscovery': 
		from isi_functions import ISINodeDisc 
		print (ISINodeDisc(Client, "node.clientstats.connected.nfs"))
	elif args.item == 'nodebalance':
		from isi_functions import ISINodeNFSBalance 
		print (ISINodeNFSBalance(Client, "node.clientstats.connected.nfs", int(args.nodeid)))
	elif args.item == 'uptime': 
		from isi_functions import ISIGetNodeInformation
		query = [x['status']['uptime'] for x in ISIGetNodeInformation(Client, int(args.nodeid))['nodes']]
	 	print query[0] 
	elif args.item == 'battery': 
		from isi_functions import ISIGetNodeInformation
		query = [x['status']['batterystatus']['status1'] for x in ISIGetNodeInformation(Client, int(args.nodeid))['nodes']]
	 	if query[0] == 'Ready and enabled': 
			print "OK"
		else: 
			print "Problem"
	elif args.item == 'nodedisk': 
		from isi_functions import ISIGetNodeInformation
		for values in ISIGetNodeInformation(Client, args.nodeid)['nodes']:
			for diskvalues in values['drives']:
				if args.diskname in diskvalues['devname']:
					print diskvalues	 
					
	elif args.item == 'nodediskdiscovery': 
		from isi_functions import ISINodeDiskDiscovery 
		print ISINodeDiskDiscovery(Client)
	else: 
		pass


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='ISILON - Monitoring')
	parser.add_argument('--item', action = 'store', dest = 'item', help="""Informe o item de Monitoracao""")
	parser.add_argument('--hostname', action = 'store', dest = 'hostname', help="""Informe o hostname do storage""")
	parser.add_argument('--node', action = 'store', dest = 'nodeid', help="""Informe o node ID""")
	parser.add_argument('--diskname', action = 'store', dest = 'diskname', help="""Informe o diskname do node""")
	args = parser.parse_args()
    run(args)
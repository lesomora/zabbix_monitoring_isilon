# zabbix_monitoring_isilon
ISILON - Monitoring

This monitoring is basead in SDK ISILON Monitoring and SNMP 

SNMP Monitoring Items Support: 

Health Cluster: 
  * Node Count 
  * Online Nodes
  * Offline Nodes
  * IFS used
  * IFS free
  * IFS Total
  * Cluster Network Out bits PerSecond
  * Cluster Network In bits PerSecond
  * Cluster IFS Out Bytes and Bytes PerSecond
  * Cluster IFS in Bytes and Bytes PerSecond

Protocols: 
  * Support ftp 
  * Support http 
  * Support nfs3 
  * Support nfs4 
  * Support nlm 
  * Support smb1 
  * Support smb2 
  * Support synciq

Dataset Info: 
  * Dataset Quota Used 
  * Dataset Quota Used With Overhead

Python Monitoring RestAPI Items Support:

  * Node Balance Connection
  * Snapshot Used 
  * Battery State PerNode 
  * Disk State PerNode
  * Node Uptime
  
Installation Guide: 

Import zabbix template in frontweb interface: 

* Configuration -> Templates -> Import -> Choose files

Adding file mibs in proxy or server path is running SNMP:

* mv ISILON-MIB.mib /usr/share/snmp/mibs/

Python is 2.7 soon will upgrade to 3.7 

Install requiriments packages: 

* pip install -r requiriments.txt 

Adding scripts "connection.py, isi_functions.pyc and isi_monitoring.py" to externalscripts path: 

* mv *.py /usr/lib/zabbix/externalscripts/ 

Only need configurate User and Password in connection.py

Help: 

usage: isi_monitoring.py [-h] [--item ITEM] [--hostname HOSTNAME]
                         [--node NODEID] [--diskname DISKNAME]

ISILON - Monitoring

optional arguments:
  -h, --help           show this help message and exit
  --item ITEM          Informe o item de Monitoracao
  --hostname HOSTNAME  Informe o hostname do storage
  --node NODEID        Informe o node ID
  --diskname DISKNAME  Informe o diskname do node

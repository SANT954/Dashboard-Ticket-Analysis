import cx_Oracle

''' queries here '''

incident_sr_count="select CATEGORY , count(*) from report where created>sysdate-2 group by CATEGORY"
incident_sr_inflow="select to_char(Created) as Created , Incident, SR from (SELECT trunc(created) as Created,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report  group by trunc(created) order by created )"
incident_sr_outflow="select to_char(Closed) as Closed , Incident, SR from (SELECT trunc(Closed) as Closed,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report where Closed is not null group by trunc(Closed) order by Closed )"


def getConnection():
    
 
    
    return cx_Oracle.connect('REPORTDB/REPORTDB@127.0.0.1:1522/SYSTEM')
     
    

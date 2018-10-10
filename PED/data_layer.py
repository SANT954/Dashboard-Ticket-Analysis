import cx_Oracle

''' queries here '''

incident_sr_count="select CATEGORY , count(*) from report where created>sysdate-5 group by CATEGORY"
daily_ticket_inflow="select to_char(Created,'MM-DD-YYYY') as Created , Incident, SR from (SELECT trunc(created) as Created,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report   group by trunc(created) order by created )"
daily_ticket_outflow="select to_char(Closed) as Closed , Incident, SR from (SELECT trunc(Closed) as Closed,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report where Closed is not null group by trunc(Closed) order by Closed )"
weekly_ticket_inflow="select to_char(Created) as Created , Incident, SR from (SELECT trunc(created) as Created,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report  group by trunc(created) order by created )"
weekly_ticket_outflow="select to_char(Closed) as Closed , Incident, SR from (SELECT trunc(Closed) as Closed,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report where Closed is not null group by trunc(Closed) order by Closed )"
daily_ticket_inflow_="SELECT to_char(Created,'MM-DD-YYYY') as Created,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report    group by to_char(Created,'MM-DD-YYYY')order by created "

def getConnectionCursor():
    
 
    con=cx_Oracle.connect('REPORTDB/REPORTDB@127.0.0.1:1522/SYSTEM')
    return con.cursor()
     
    

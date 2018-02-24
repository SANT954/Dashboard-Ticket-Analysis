import cx_Oracle

''' queries here '''
truncate_table="truncate table report"
incident_sr_count="select CATEGORY , count(*) from report where created>sysdate-1 group by CATEGORY"
daily_ticket_inflow="select to_char(Created,'MM-DD-YYYY') as Created , Incident, SR from (SELECT trunc(created) as Created,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report   group by trunc(created) order by created )"
daily_ticket_outflow="select to_char(Closed) as Closed , Incident, SR from (SELECT trunc(Closed) as Closed,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report where Closed is not null group by trunc(Closed) order by Closed )"
daily_ticket_inflow_="SELECT to_char(Created,'MM-DD-YYYY') as Created,sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report    group by to_char(Created,'MM-DD-YYYY')order by created "
ticket_status="select status,count(*) from report where created>sysdate-10 group by status"
ticket_source="select SOURCE_SYSTEM,count(*) from report where created>sysdate-10 group by SOURCE_SYSTEM"
open_tickets_by_queue="select QUEUE ,count(*) from report where status not in ('Solved') group by QUEUE "
open_sr_ticket_source="select SOURCE_SYSTEM,count(*) from report where CATEGORY in ('Incident') and status not in ('Solved') and created>sysdate-10 group by SOURCE_SYSTEM"
open_incident_ticket_source="select SOURCE_SYSTEM,count(*) from report where CATEGORY in ('Service Request') and status not in ('Solved') and created>sysdate-10 group by SOURCE_SYSTEM"
ticketicket_data_report="Select TICKET, CATEGORY, DISPOSITION,STATUS, ASSIGNED,trim(BUG_NUMBER),  CONTROL_NUMBER, CREATED from report "
t_data_report="Select TICKET, CATEGORY, CREATED from report where rownum<4"
weekly_data="select TRUNC(created)-TO_NUMBER(TO_CHAR(created,'D'))+1 week_start_date, count(*) from report group by TRUNC(created)-TO_NUMBER(TO_CHAR(created,'D'))+1"
weekly_ticket_inflow="select (TRUNC(created)-TO_NUMBER(TO_CHAR(created,'D'))+1) week_start_date, sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report group by (TRUNC(created)-TO_NUMBER(TO_CHAR(created,'D'))+1) order by (TRUNC(created)-TO_NUMBER(TO_CHAR(created,'D'))+1)"  
weekly_ticket_outflow="select COALESCE(t.week_start_date,sysdate),t.incident,t.sr from (select (TRUNC(CLOSED)-TO_NUMBER(TO_CHAR(CLOSED,'D'))+1) week_start_date, sum(DECODE(CATEGORY, 'Incident',1,0)) as Incident ,sum(DECODE(CATEGORY, 'Service Request',1,0)) as  SR from report group by (TRUNC(CLOSED)-TO_NUMBER(TO_CHAR(CLOSED,'D'))+1) order by (TRUNC(CLOSED)-TO_NUMBER(TO_CHAR(CLOSED,'D'))+1))  t "  



current_open_count ="select count(*) from report where status not in ('Solved')"
current_open_incidents="select count(*) from report where status not in ('Solved') and category in ('Incident')"
current_open_srs="select count(*) from report where status not in ('Solved') and category in ('Service Request')"
current_open_auto_incidents="select count(*) from report where status not in ('Solved') and category in ('Incident') and CONTROL_NUMBER is not null"
current_open_manual_incidents="select count(*) from report where status not in ('Solved') and category in ('Incident') and CONTROL_NUMBER is null"
current_open_p1s="select count(*) from report where status not in ('Solved') and SEVERITY ='1 - Severe Business Impact' "
current_open_aged_7="select count(*) from report where  status not in ('Solved')  and created< sysdate-7 and created > sysdate-30 "
current_open_aged_30="select count(*) from report where  created < sysdate-30 and status not in ('Solved')"



ticketicket_data_7="Select TICKET,CATEGORY,DISPOSITION,ASSIGNED,trim(BUG_NUMBER),  CONTROL_NUMBER   from report where status not in ('Solved')  and created< sysdate-7 and created > sysdate-30"

def getConnectionCursor():
    
 
    con=cx_Oracle.connect('REPORTDB/REPORTDB@127.0.0.1:1522/SYSTEM')
    return con
     
    

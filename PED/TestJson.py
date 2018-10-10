import requests
from PED import data_layer

def pullLatestData():
    

    url='https://oihap.oraclecorp.com/osbcommon/TicketingService/TicketingRest/reports?id=103784&system=oal%20osvc'
    response = requests.get(url)
    response.encoding = 'utf-8'
    jsonResponse= response.json()
    
    jsonData = jsonResponse["report"]
    column=jsonData[0].get('columns')
    data=jsonData[0].get('rows')
    dat=data
    print(len(dat))
    con = data_layer.getConnectionCursor()
    cur=con.cursor()
    for rec in dat:
        '''name = item.get("rows")
        campaignID = item.get("lookupName")
        print(name)
        print(campaignID)'''
        item=rec.split(',')
         
     #   print(item)
        if len(item[11])==0:
            item[11]="''"
            
        cur.execute("INSERT INTO REPORTtt ( TICKET, QUEUE, PRODUCT_ID, SOURCE_SYSTEM, CATEGORY, DISPOSITION, CONTROL_NUMBER, BUG_NUMBER, SEVERITY, STATUS,CREATED, CLOSED, ASSIGNED, UPDATED,  PRODUCT_HIERARCHY,  CREATED_BY ) VALUES ('"
        + str(item[0]) + '\',\'' +  str(item[1])+ '\',\'' 
        + str(item[2]) + '\',\'' +  str(item[3])+ '\',\''
        + str(item[4]) + '\',\'' +  str(item[5])+ '\',\''  
        + str(item[6]) + '\',\'' +  str(item[7])+ '\',\''  
        + str(item[8]) + '\',\'' +  str(item[9])+ '\','  
        #+ item[10] + '\',\'' +  item[11]+ '\',\''  
        + "to_date("  +  str(item[10])  +",'yyyy-mm-dd hh24:mi:ss')" +','
        + "to_date("  +  str(item[11])  +",'yyyy-mm-dd hh24:mi:ss')"+  ',\'' 
        + str(item[12]) + '\',' 
        + "to_date("  +  str(item[13])  +",'yyyy-mm-dd hh24:mi:ss')"+  ',\''  
        + str(item[14]) + '\',\''  
       # + "q\"[" +item[15] + "]\""+ '\',\'' +  str(item[16])+  "')")
        +  str(item[15])+  "')")
        con.commit()
    
    print("executed")
       
       
       
    #cur.execute(query)
    
    
        
    con.commit()
    print("executed")
    import datetime
    current_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S");
    sync_job_status='Success'
    cur.execute("INSERT INTO sync_job_status (last_updated_status, last_updated) VALUES ('" + sync_job_status +"'," + "to_date('"  +  str(current_date)  +"','yyyy-mm-dd hh24:mi:ss')"+ ")")    
    con.commit()    
'''    cur.execute("INSERT INTO REPORT ( TICKET, CATEGORY, DISPOSITION, CONTROL_NUMBER, trim(BUG_NUMBER), STATUS, CREATED, ASSIGNED ) VALUES ("
        + str(item[0]) + ',' +  str(item[1])+ 
    ',' +str(item[2])+ ',' +str(item[3])+ 
    ',' +str(item[4])+ ',' +str(item[5])+ 
    ',' +str(item[6])+ ',' +str(item[7]) +")"
    )
'''
    
    


if __name__ == '__main__':
    pullLatestData()
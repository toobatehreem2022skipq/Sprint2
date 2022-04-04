import urllib3
import datetime
URL_TO_MONITOR = "skipq.org"
def lambda_handler(event, context):
   
    values=dict()

    #Using for loop to get availability and latency of three urls
    # for i in url_To_Monitor:
    #     dimensions= {                     #Need To Ask
    #                  'Name': 'URL',
    #                  'Value': i
    #              },
    avail=availability()
        
        # calling put metric data method from CloudWatchMetric Class through its instance
        # cw.put_metric_data(url_Monitor_NameSpace,url_Monitor_METRIC_AVAILABILITY,dimensions,avail)
        
    late=latency()
        
        # cw.put_metric_data(url_Monitor_NameSpace,url_Monitor_METRIC_LATENCY,dimensions,late)
       # Updating values of availability and latency in dictionary variable
    # values[i]={"availability":avail,"latency":late}
    values={"availability":avail,"latency":late}

    return values


    
    
#return availability of specified url


def availability():
    http=urllib3.PoolManager() #Need To Ask
    response=http.request('GET',URL_TO_MONITOR)
    if response.status==200:
        return 1.0
    else:
        return 0.0
        
        
#return latency of specified url

def latency():
    http=urllib3.PoolManager()
    start=datetime.datetime.now()
    response=http.request("GET",URL_TO_MONITOR)
    end=datetime.datetime.now()
    delta=end-start
    latencySec=round(delta.microseconds* .000001,6)
    return latencySec


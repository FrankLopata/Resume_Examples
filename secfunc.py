
from ast import Num
import urllib.error
import urllib.request
import json
import urllib.parse
import math





def Pollution__AQI(num:float)-> int:
#Returns first AQI above num
    if num > 500.5:
        return 501
    prevx=0
    index = 0 
    ranges = [12.1,35.5,55.5,150.5,250.5,350.5,500.5]
    aqis=[51.0,101.0,151.0,201.0,301.0,401.0,501.0]
    for x in ranges:
        if(num<x):
            output = aqis[index] +((num-math.floor(x)) * ((aqis[index+1]-1)-aqis[index]))/(x-prevx)
            return math.ceil(output)
        index = index + 1
        prevx = x

def Coordinate_Calc(centerloc:str,lat1:str,lon1:str)->float:
    try:
        centerloc = centerloc.split()
        if(lat1==None or lon1==None):
            return None
        lat2=centerloc[0]
        lat2 = float(lat2[:-2])*(math.pi/180)
        lon2 = centerloc[1]
        lon2 = float(lon2[:-2])*(math.pi/180)
        lon1=float(lon1)*(math.pi/180)
        lat1=float(lat1)*(math.pi/180)
        lon = lon2 - lon1
        lat = lat2 - lat1
        alat = (lat1+lat2)/2
        r = 3958.8
        x=lon*math.cos(alat)
        return math.sqrt(x**2 + lat**2) * r
    except Exception as e:
        print(e)


class center_cord_loc:
    def __init__(self,loc:str):
        self._loc = loc
    def Center_Location(self)->str:
        try:
            locat = urllib.parse.urlencode([("q", self._loc), ("format", "json")])
            url = 'https://nominatim.openstreetmap.org/search?' + locat
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            text = response.read()
            response.close()
            text = text.decode(encoding = 'utf-8')
            text = json.loads(text)
            if text[0]['lat'][0] == "-":
                lat = text[0]['lat'][0:] +"/S"
            else:
                lat = text[0]['lat']+"/N"
            if text[0]['lon'][0] == "-":
                lon = text[0]['lon'][0:] +"/W"
            else:
                lon = text[0]['lon']+"/E"
            string =" "+lat +" "+ lon
            return string
        except urllib.error.HTTPError as e:
            print("FAILED")
            print('https://nominatim.openstreetmap.org/search?' + locat)
            print('Status code: {}'.format(e.code))

class center_cord_fileloc:
    def __init__(self,path):
        self._path = path
    def Center_FileLoc(self)->str:
        try:
            with open(self._path) as file:
                try:
                    data = file.read()
                except:
                    print("FAILED")
                    print(self._path)
                    print("MISSING")
            text = json.loads(data)
            if text[0]['lat'][0] == "-":
                lat = text[0]['lat'][0:] +"/S"
            else:
                lat = text[0]['lat']+"/N"
            if text[0]['lon'][0] == "-":
                lon = text[0]['lon'][0:] +"/W"
            else:
                lon = text[0]['lon']+"/E"
            string =" "+lat +" "+ lon
            return string
        except Exception as e:
            print("FAILED")
            print(self._path)
            if(e[:10]=="[Errno 2]"):
                print("MISSING")
            else:
                print("FORMAT")
    
class pol_aqi_web:
    def __init__(self):
        try:
            response = urllib.request.urlopen('https://www.purpleair.com/data.json')
            text = response.read()
            response.close()
            text = text.decode(encoding = 'utf-8')
            text = json.loads(text)
            sensorl=[]
            for sensors in text['data']:
                sensorl.append(sensors)
            self._sensors=sensorl
        except urllib.error.HTTPError as e:
            print("FAILED")
            print('https://www.purpleair.com/data.json')
            print('Status code: {}'.format(e.code))
    def raw_sensor_list(self)->list:
        return self._sensors
class pol_aqi_file:
    def __init__(self,path):
        self._path = path
    def Sensors_files(self):
        try:
            with open(self._path) as file:
                data = file.read()
            data = json.loads(data)
            sensorl=[]
            for sensors in data['data']:
                sensorl.append(sensors)
            return sensorl
        except Exception as e:
            print("FAILED")
            print(self._path)
            if(e[:10]=="[Errno 2]"):
                print("MISSING")
            else:
                print("FORMAT")
class reverse_nominatim:
    def __init__(self,lat:str,lon:str):
        self._lat = lat
        self._lon = lon
    def reverse_nominatim_func(self)->dict:
        try:
            response = urllib.request.urlopen('https://nominatim.openstreetmap.org/reverse?lat='+str(self._lat)+'&lon='+str(self._lon)+"&format=json")
            text = response.read()
            response.close()
            text = text.decode(encoding = 'utf-8')
            text = json.loads(text)
            return text['display_name']
        except urllib.error.HTTPError as e:
            print("FAILED")
            print('https://nominatim.openstreetmap.org/reverse?lat=' + str(self._lat) + '&lon=' +str(self._lon)+"&format=json")
            print('Status code: {}'.format(e.code))
            
class reverse_file():
    def __init__(self,path:str):
        self._path = path
    def reverse_file_func(self):
        try:
            with open(self._path) as file:
                data = file.read()
            data = json.loads(data)
            return data['display_name']
        except Exception as e:
            print("FAILED")
            print(self._path)
            if(e[:10]=="[Errno 2]"):
                print("MISSING")
            else:
                print("FORMAT")
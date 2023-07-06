import json
from secfunc import center_cord_fileloc, center_cord_loc, pol_aqi_file, pol_aqi_web
import secfunc
import os
import sys
if __name__ == '__main__':
    try:
        inpt1 = input()
        Range=input()
        Range=Range.split()
        Range = int(Range[1])
        thresholdAQI= int(input().split()[1])
        maxnumber=input().split()
        maxnumber = int(maxnumber[1])
        inpt2 = input()
        #if its AQI PURPLEAIR get ur airquality through urple air
        #if its AQI FILE path get it from teh file on ur harddrive or return error if neither
        reverse = input()
        #if REVERSE NOMINATIM  use the Nominatim API to do reverse geocoding
        #if REVERSE FILES path1 path2 ...,  use files stored on our hard drive containing
        #the results of previous calls to Nominatim's reverse geocoding API instead
        #return error is its neither OR if files paths have spaces OR if there are fewer opaths than MAX
        if(inpt1[7:11]=="FILE"):
            location = center_cord_fileloc(inpt1[12:]).Center_FileLoc()
        elif(inpt1[0:16]=="CENTER NOMINATIM"):
            location = center_cord_loc(inpt1[17:]).Center_Location()
        else:
            print("Invalid input")
            os.execl(sys.executable, sys.executable, *sys.argv)
        max = 0
        print('Center' + location)
        if(inpt2=="AQI PURPLEAIR"):
            sensors = pol_aqi_web().raw_sensor_list()
        elif(inpt2[0:9]=="AQI FILES"):
            sensors= pol_aqi_file(inpt2[9:]).Sensors_files()
        else:
            print("INVALID INPUT")
            os.execl(sys.executable, sys.executable, *sys.argv)

        if(reverse == "REVERSE FILES"):
            revl = reverse.split(' ')
            index = 2
        for sensor in sensors:
            lat = str(sensor[27])
            lon = str(sensor[28])
            if(max==maxnumber):
                break
            age =  int(sensor[4])
            if(age <= 3600):
                continue
            if(sensor[25]=="1"):
                continue
            if(secfunc.Coordinate_Calc(location,sensor[27],sensor[28])>Range or secfunc.Coordinate_Calc(location,sensor[27],sensor[28])==None):
                continue
            aqi = secfunc.Pollution__AQI(float(sensor[1]))
            if(aqi<thresholdAQI):
                continue
            max = max+1
            print("AQI " + str(aqi))
            if lat[0]=="-":
                lat = lat[1:]
            if lon[0]=="-":
                lon = lon[1:]
            print(lat+" "+lon)
            if(reverse=="REVERSE NOMINATIM"):
                output=secfunc.reverse_nominatim(sensor[27],sensor[28])
                print(output.reverse_nominatim_func())
            elif(reverse == "REVERSE FILES"):
                output=secfunc.reverse_file(revl[index])
                print(output.reverse_file_func())
                index = index + 1
    except:
       os.execl(sys.executable, sys.executable, *sys.argv)


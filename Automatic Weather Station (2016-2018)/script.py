import sys
import datetime
import unicodedata
import calendar
from influxdb import InfluxDBClient



def main():

    f= open("Tudo-sergio.txt","r")
    lines = f.readlines()
    '''
    ET_cm = 0
    UV = 0
    outTemp_C = 0
    highOutTemp = 0
    lowOutTemp =0
    outHumidity=0
    dewpoint_C=0
    windSpeed_kph=0
    windDir=0
    windrun_km=0
    windchill_C = 0
    heatindex_C=0
    barometer_mbar=0
    rain_cm =0
    rainRate_cm_per_hour = 0
    radiation_Wpm2=0
    highRadiation =0
    highUV=0
    appTemp_C=0
    inHumidity=0
    inDewpoint_C=0
    inTemp_C=0
    '''
    
    for x in lines[2:]:
        '''
        global ET_cm
        global UV
        global outTemp_C
        global highOutTemp
        global outHumidity
        global dewpoint_C
        global windSpeed_kph
        global windDir
        global windrun_km
        global windchill_C
        global heatindex_C
        global barometer_mbar
        global rain_cm
        global rainRate_cm_per_hour
        global radiation_Wpm2
        global highRadiation
        global highUV
        global appTemp_C
        global inHumidity
        global inDewpoint_C
        global inTemp_C
        '''
        try:
            
            #result.append(x.split('\t')[0])
            time = x.split('\t')[0]
            real_time = str(time)
            dia,mes,fake_ano = real_time.split("/")
            ano = '20' + fake_ano
        
            hora = x.split('\t')[1]
            
            formated_timestamp = ano + '-' + mes + '-' + dia + 'T' + str(hora) + ':00Z'
        
            outTemp_C = float(x.split('\t')[2])
            highOutTemp = float(x.split('\t')[3])
            lowOutTemp = float(x.split('\t')[4])
            outHumidity = float(x.split('\t')[5])
            dewpoint_C = float(x.split('\t')[6])
            windSpeed_kph = float(x.split('\t')[7])
            
            windDir = str(x.split('\t')[8])
            if(windDir=='N'):
                windDir = 0
            if(windDir=='NNE'):
                windDir = 30
            if(windDir=='NE'):
                windDir = 45
            if(windDir=='ENE'):
                windDir = 75
            if(windDir=='E'):
                windDir = 90
            if(windDir=='ESE'):
                windDir = 120
            if(windDir=='SE'):
                windDir = 135
            if(windDir=='SSE'):
                windDir = 165
            if(windDir=='S'):
                windDir = 180
            if(windDir=='SSW'):
                windDir = 210
            if(windDir=='SW'):
                windDir = 225
            if(windDir=='WSW'):
                windDir = 255
            if(windDir=='W'):
                windDir = 270
            if(windDir=='WNW'):
                windDir = 300
            if(windDir=='NW'):
                windDir = 315
            if(windDir=='NNW'):
                windDir = 345
                
            windrun_km = float(x.split('\t')[9])
            hi_speed = x.split('\t')[10]
            hi_direction = x.split('\t')[11]
        
            windchill_C = float(x.split('\t')[12])
            heatindex_C = float(x.split('\t')[13])
            thw_index = x.split('\t')[14]
            thsw_index = x.split('\t')[15]
            barometer_mbar = float(x.split('\t')[16])
            rain_cm = float(x.split('\t')[17])
            rainRate_cm_per_hour = float(x.split('\t')[18])
            radiation_Wpm2 = float(x.split('\t')[19])
            solar_energy = x.split('\t')[20]
            highRadiation = float(x.split('\t')[21])
            index = x.split('\t')[22]
            highUV = float(x.split('\t')[23])
            UV = float(x.split('\t')[24])
            hi_d_d = x.split('\t')[25]
            heat_d_d = x.split('\t')[26]
            appTemp_C = float(x.split('\t')[27])
            inHumidity = float(x.split('\t')[28])
            inDewpoint_C = float(x.split('\t')[29])
            inTemp_C = float(x.split('\t')[30])
            in_emc = x.split('\t')[31]
            in_density = x.split('\t')[32]
            ET_cm = float(x.split('\t')[33])
            samp = x.split('\t')[34]
            wind_tx = x.split('\t')[35]
            wind_recept = x.split('\t')[36]
            iss_int = x.split('\t')[37]
            #arc = x.split('\t')[38]
        
            
            
            #print(appTemp_C)
            
            user =''
            password = ''
            host = 'localhost'
            dbname = 'weewx_default' 
        
            json_body = [
                {
                    "measurement":"default_vantage_pro2",
                    "tags":{
                        "location": "IGUP",
                        "instrument":"VantagePro2",
                        "latitude": 41.13861111,
                        "longitude": 8.60250000,
                        "altitude": 93.515,
                    },
                    "time": formated_timestamp,
                    "fields": {  
                        "ET_cm": ET_cm,
                        "UV": UV,
                        "appTemp_C": appTemp_C,
                        "barometer_mbar": barometer_mbar,
                        "dewpoint_C": dewpoint_C,
                        "heatindex_C": heatindex_C,
                        "highOutTemp": highOutTemp,
                        "highRadiation": highRadiation,
                        "highUV": highUV,
                        "inDewpoint_C": inDewpoint_C,
                        "inHumidity": inHumidity,
                        "inTemp_C": inTemp_C,
                        "lowOutTemp": lowOutTemp,
                        "outHumidity": outHumidity,
                        "outTemp_C": outTemp_C,
                        "radiation_Wpm2": radiation_Wpm2,
                        "rainRate_cm_per_hour": rainRate_cm_per_hour,
                        "rain_cm": rain_cm,
                        "windDir": float(windDir),
                        "windSpeed_kph": windSpeed_kph,
                        "windchill_C": windchill_C,
                        "windrun_km": windrun_km
                    }
                }
            ]
            

            client = InfluxDBClient(host,8086,user,password,dbname)
        
            client.write_points(json_body)
            
        except ValueError:
            pass
                         

if __name__=="__main__":
    main()


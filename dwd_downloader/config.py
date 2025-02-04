"""
Configuration file with required Path settings, parameters and options
relevant for RCM Project
use .env file to set local paths

"""
from decouple import config


#-----------------------------------------------------
# DEFINE MAIN PATHS (LOCAL/SERVER)

# path to SQLite Database
db_path = config('DB_PATH')

# dwd catch folder to write temporary extracted from internet file
dwd_catch_folder = config('DWD_CATCH_FOLDER_PATH')

#log_path = config('LOGGING_CONFIG')


start_date = '2017-01-01'
end_date = '2017-03-31'

shp_buffer_dist = {
                  'DEMM': -20
                , 'FRIEN': -30
                , 'MRKN': -10
                }

crs_utm = {
              'DEMM': '32633'
            , 'FRIEN': '32632'
            , 'MRKN': '32633'
          }

#-----------------------------------------------------
# DEFINE AREAS OF INTEREST ('AOI_symb': 'AOI_full_name')
#-----------------------------------------------------
aoi_dict = {
      'DEMM': 'Demmin'
    , 'FRIEN': 'Frienstedt'
    , 'MRKN': 'Markneukirchen'
    }

#-----------------------------------------------------
# DEFINE DWD VARIABLES
#-----------------------------------------------------
# selected DWD (Pheno-) Stations close to AOI's
    # ftp://ftp-cdc.dwd.de/climate_environment/CDC/help/PH_Beschreibung_Phaenologie_Stationen_Jahresmelder.txt
    # ftp://ftp-cdc.dwd.de/climate_environment/CDC/help/PH_Beschreibung_Phaenologie_Stationen_Sofortmelder.txt
pheno_stations = {
          'DEMM': [12508, 12615, 12561, 1757, 12709]
        , 'FRIEN': [13410, 13400, 13586, 13589, 15460, 3302]
        , 'MRKN': [1780, 13030, 12784, 12780, 14129, 12978]
        }

# selected DWD (Weather-) Stations close to AOI's
    #ftp://ftp-cdc.dwd.de/climate_environment/CDC/help/KL_Tageswerte_Beschreibung_Stationen.txt
wd_stations = {
          'DEMM': [167, 15003] #['Anklam']
        , 'FRIEN': [1270] # ['Erfurt-Weimar']
        , 'MRKN': [1207, 1282] # [' Elster, Bad-Sohl']
        }


aoi_wkt_poly = {
                  'DEMM': 'POLYGON ((13.2926817673174 53.8144078294447, ' \
                         '13.1224129280849 53.819658352906,  ' \
                         '13.1333593424838 53.9308789477431, ' \
                         '13.303999810205 53.9245950444735,  ' \
                         '13.2926817673174 53.8144078294447))'

                , 'FRIEN': 'POLYGON ((10.892265825967732 50.96867157517775,' \
                         '10.992215665354548 50.96700905641184, ' \
                         '10.990858842100174 50.935271874856, ' \
                         '10.890976973250734 50.93693252445378, ' \
                         '10.892265825967732 50.96867157517775))'

                , 'MRKN': 'POLYGON ((12.2458007191639 50.2619386357066,' \
                        '12.2458007191639 50.4076010991433, ' \
                        '12.3879750421914 50.4076010991433, ' \
                        '12.3879750421914 50.2619386357066, ' \
                        '12.2458007191639 50.2619386357066))'
                }


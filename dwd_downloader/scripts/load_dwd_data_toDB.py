"""
@author: Aranil

This is a script to run functions defined in DB_utility_dwd.py to web-scrap data from HTTP server and collect them in SQLite DB

"""
from datetime import date
from dateutil.parser import parse
import numpy as np
from dbflow.src.db_utility import connect2db, create_sql, query_sql

from dwd_downloader import config as cfg
import DB_utility_dwd as db_dwd



# additional functions for submodules
def generate_year_list(start_date, end_date):
    '''
    Helper function - generates list of years through definition of the start and end date

    Parameters
    ----------
    start_date: str
        date to start a search, only the year will be extracted
    end_date
        date to stop search, only the year will be extracted
    Returns
    -------
        list of str
            list of years (i.g. ['2017', '2018'])
    '''
    START_DATE = parse(start_date)
    END_DATE = parse(end_date)

    # generate year list
    if START_DATE.year != END_DATE.year:
        year = np.arange(START_DATE.year, END_DATE.year + 1, 1).tolist()
        return [str(x) for x in year]
    else:
        return [str(START_DATE.year)]





# connect to DB - will automatically create DB if not exist in the location defined in .env file
dbarchive = connect2db(cfg.db_path)


def loadwd2(
            start_date=cfg.start_date,
            end_date=cfg.end_date,
            #study_area=list(cfg.aoi_dict.keys()),
            study_area=['FRIEN'],
            crops=['Sommergerste', 'Sommerweizen', 'Winterweizen', 'Winterraps', 'Mais', 'Zucker-Rübe'],
            tempdir=cfg.dwd_catch_folder,
            rcmarchive=dbarchive
            ):

    START_DATE = date.strftime(parse(start_date), '%Y%m%d%H')
    END_DATE = date.strftime(parse(end_date), '%Y%m%d%H')

    year = generate_year_list(start_date, end_date)

    # collect all possible combinations of element pairs in one list
    pattern_list = [(AOI, YEAR) for AOI in study_area for YEAR in year]


    # TODO: Implement deleting Table from DB !!! select Update or Load !!!!

    #---- PHENO DATA
    phen_hist_immediate = db_dwd.DWDData(data_type="phenology", report_type="historical", report_resolution="immediate")
    phen_hist_annual = db_dwd.DWDData(data_type="phenology", report_type="historical", report_resolution="annual")
    phen_recent_immediate = db_dwd.DWDData(data_type="phenology", report_type="recent", report_resolution="immediate")
    phen_recent_annual = db_dwd.DWDData(data_type="phenology", report_type="recent", report_resolution="annual")

    # ---- WEATHER DATA only hourly!!
    wd_recent_hourly = db_dwd.DWDData(data_type="climate", report_type="recent", report_resolution="hourly")
    wd_hist_hourly = db_dwd.DWDData(data_type="climate", report_type="historical", report_resolution="hourly")

    wd_recent_hourly.query_weather_stations(db=rcmarchive)
    wd_hist_hourly.query_weather_stations(db=rcmarchive)


    # --------- run processing for each AOI
    for (AOI, YEAR) in pattern_list:
        print("aoi:", AOI, " --- year:", YEAR)


        #------- Insert STATIONS
        # imports the same station as for (report_type="historical", report_resolution="immediate") and ("historical", report_resolution="annual")
        pheno_stations = cfg.pheno_stations[AOI]
        phen_hist_immediate.query_pheno_stations(db=rcmarchive, station=pheno_stations, ingest=True, update=False)
        phen_hist_annual.query_pheno_stations(db=rcmarchive, station=pheno_stations, ingest=True, update=False)
        #print(query)
        # TODO: Implement selection after stations into query_pheno_stations() and crop types !!!!! no main_object in stations txt file!!
        # TODO: update=False, does not work for geometries!!!
        # TODO: add Documentation!!

        # ------- Insert DATA
        phen_recent_immediate.query_pheno_data(db=rcmarchive, crop=crops, date=[START_DATE, END_DATE], station=pheno_stations, ingest=True, update=False)
        phen_recent_annual.query_pheno_data(db=rcmarchive, crop=crops, date=[START_DATE, END_DATE], station=pheno_stations)
        phen_hist_immediate.query_pheno_data(db=rcmarchive, crop=crops, date=[START_DATE, END_DATE], station=pheno_stations, ingest=True, update=False) #UPDATE does not work!!
        phen_hist_annual.query_pheno_data(db=rcmarchive, crop=crops, date=[START_DATE, END_DATE], station=pheno_stations)



        #---- WEATHER DATA only hourly!!
        wd_stations = cfg.wd_stations[AOI]
        wd_recent_hourly.query_weather_data(db=rcmarchive, station=wd_stations, date=[START_DATE, END_DATE],
                                            tempdir=tempdir, ingest=False,
                                            new_colname='aoi',
                                            colname_value=AOI
                                            )
        wd_hist_hourly.query_weather_data(db=rcmarchive,
                                          date=[START_DATE, END_DATE],
                                          station=wd_stations,
                                          tempdir=tempdir,
                                          ingest=True,
                                          update=False,
                                          new_colname='aoi',
                                          colname_value=AOI)



if __name__ == '__main__':
    loadwd2(
        start_date='2020-11-15',
        end_date='2020-12-10',
        #crops = ['Sommergerste', 'Sommerweizen']
        #study_area=['FRIEN']
        )


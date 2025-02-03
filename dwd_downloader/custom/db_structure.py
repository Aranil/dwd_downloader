"""
@author: Aranil

DB Table structure definition

ForeignKey(s) are set to RCM Project specific tables
"""

from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, CLOB,  Text, UnicodeText, UniqueConstraint, ForeignKey, ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry
from sqlalchemy.sql import func



Base = declarative_base()


class DataCatalogue(Base):
    """
    Template for an auxiliary Overview table for all Management and Sentinel Data ....
    """
    __tablename__ = 'datacatalogue'

    # id = Column(Integer)
    datatype_code = Column(String, primary_key=True)
    datatype_name = Column(String, primary_key=True)
    datatype = Column(String, primary_key=True)
    datatype_description = Column(String)
    source = Column(String)
    year = Column(Integer, primary_key=True)
    aoi = Column(String, primary_key=True)
    ForeignKeyConstraint(columns=['datacatalogue.aoi'],
                         refcolumns=['aoilegend.aoi'],
                         onupdate="CASCADE", ondelete="SET NULL")


# ----------------------------------------------------
# DWD Data (Weather)
# ----------------------------------------------------

class DWDCatalogue(Base):
    """
    Template for an auxiliary Overview table for a DWD Data
    """
    __tablename__ = 'dwdcatalogue'

    station_id = Column(Integer, primary_key=True)
    year = Column(Integer, primary_key=True)
    datatype_code = Column(String, primary_key=True)  # climate, phenology
    report_type = Column(String, primary_key=True)  # recent, historical >> fils table only for historical, why???
    report_resolution = Column(String, primary_key=True)  # hourly, daily,  annual, immidiate
    parameter_code = Column(String, primary_key=True)  # TT_TU, RF_TU
    parameter = Column(String, primary_key=True)  # air_temperature, precipitation_height, wind ...  phenological observation
    aoi = Column(String)
    ForeignKeyConstraint(columns=['dwdcatalogue.parameter_code', 'dwdcatalogue.parameter'],
                         refcolumns=['dwdparametercode.parameter_code', 'dwdparametercode.parameter'],
                         onupdate="CASCADE", ondelete="SET NULL")


class DWDParameterCode(Base):
    """
    Template for an auxiliary atomic table to store Parameter Codes of the DWD data
    """
    __tablename__ = 'dwdparametercode'

    parameter_code = Column(String, primary_key=True)  # TT_TU, RF_TU
    parameter = Column(String)  # air_temperature, precipitation_height, wind ...  phenological observation
    parameter_dwd = Column(String)  # original name of the parameter from dwd joind with parameter code >> air_temperature_tt_tu,air_temperature_rf_tu
    parameter_description = Column(String)  # can be complited by customer
    unit = Column(String)
    ForeignKeyConstraint(columns=['dwdparametercode.parameter_code'],
                         refcolumns=['dwdprametercode.parameter_code'],
                         onupdate="CASCADE", ondelete="SET NULL")
    UniqueConstraint('parameter_dwd')


class WeatherData(Base):
    """
    Template for the WeatherData Table (not atomic, the structure not corresponds to the DWD HTTP server)
    """
    __tablename__ = 'weatherdata'

    station_id = Column(Integer, primary_key=True)  # STATIONS_ID                       >>> Station identification number   Integer
    datetime = Column(DateTime, primary_key=True)  # MESS_DATUM                        >>> Measurement time                 YYYYMMDDHH
    year = Column(Integer)
    datatype_code = Column(String)  # climate
    report_type = Column(String)  # 'recent' or 'historical' # dont set to primary_key, because the recent data will be redirected to historical data with a time after data_quality check
    report_resolution = Column(String, primary_key=True)  # hourly or daily
    quality_level = Column(Integer)
    quality_level_code = Column(String)# air_temperature_quality_level     >>> Quality level                   Integer: 1-10 and -999, for coding see paragraph "Quality information" in PDF.
    parameter_code = Column(String, primary_key=True)  # air_temperature_tt_tu             >>> Air temperature 2m              °C
    parameter_value = Column(Float)  # air_temperature_tt_tu

    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())
    ForeignKeyConstraint(
        columns=['weatherdata.station_id', 'weatherdata.year', 'weatherdata.datatype_code', 'weatherdata.report_type',
                 'weatherdata.report_resolution'],
        refcolumns=['weatherstations.station_id', 'dwdcatalogue.year', 'dwdcatalogue.datatype_code',
                    'dwdcatalogue.report_type', 'dwdcatalogue.report_resolution'],
        onupdate="CASCADE", ondelete="SET NULL")


class WeatherMetaData(Base):
    """
    Template for the WeatherMetaData Table
    """
    __tablename__ = 'weathermetadata'

    station_id = Column(Integer, primary_key=True)  # 127
    date_start = Column(Integer)  # 19500401
    date_end = Column(Integer)  # 20110331
    # station_name = Column(String)
    parameter_code = Column(String, primary_key=True)  # TT_TU, ....
    # parameter = Column(String, primary_key=True)               # air_temperature # TODO change it value  !!! change SKRIPT!
    # parameter_description = Column(String)
    # unit = Column(String)
    source = Column(String)
    additional_info = Column(String)
    special_features = Column(String)
    bibliography = Column(String)
    report_type = Column(String)  # historical or recent   # set to primary_key=True if needed!
    report_resolution = Column(String, primary_key=True)  # hourly or daily  # set to , primary_key=True if needed!
    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())
    ForeignKeyConstraint(columns=['weathermetadata.station_id', 'weathermetadata.report_type',
                                  'weathermetadata.report_resolution', 'weathermetadata.parameter_code'],
                         refcolumns=['weatherstations.station_id', 'dwdcatalogue.report_type',
                                     'dwdcatalogue.report_resolution', 'dwdparametercode.parameter_code'],
                         onupdate="CASCADE", ondelete="SET NULL")
    UniqueConstraint('date_start', 'date_end')


class WeatherStations(Base):
    """
    Template for the WeatherStations Table (not quiet atomic, multiple station_id after date_star & date_end)
    """
    __tablename__ = 'weatherstations'

    station_id = Column(Integer, primary_key=True)  # 127
    date_start = Column(Integer)  # 19500401
    date_end = Column(Integer)  # 20110331
    geo_lon = Column(Float)  # 6.0941
    geo_lat = Column(Float)  # 50.7827
    height = Column(Integer)  # 202
    name = Column(String)  # Aachen
    state = Column(String)  # Nordrhein-Westfalen
    access = Column(String)
    #access = Column(Boolean)  # Boolean column

    # column was Changed!!! was PARAMETER !!!
    # parameter_code = Column(String, primary_key=True)                          # TU, ...
    station_pos = Column(Geometry('POINT', srid=4326))  # BLOB, Geometry
    report_type = Column(String)  # recent or historical
    report_resolution = Column(String, primary_key=True)
    aoi = Column(String)
    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())
    ForeignKeyConstraint(
        columns=['weatherstations.station_id', 'weatherstations.report_type',
                 'weatherstations.report_resolution'],
        refcolumns=['dwdcatalogue.station_id', 'dwdcatalogue.report_type',
                    'dwdcatalogue.report_resolution'])
    UniqueConstraint('date_start', 'date_end')



# ----------------------------------------------------
# DWD Data (Phenology)
# ----------------------------------------------------

class PhenoStations(Base):
    """
    Template for the PhenoStations Table
    """
    __tablename__ = 'phenostations'

    station_id = Column(Integer, primary_key=True)  # , sqlite_on_conflict_unique='REPLACE'
    name = Column(String)
    geo_lat = Column(Float)
    geo_lon = Column(Float)
    station_pos = Column(Geometry('POINT', srid=4326))  # calculate this!!
    height = Column(Integer)
    naturegroup_code = Column(Integer)
    naturegroup = Column(String)
    nature_code = Column(Integer)
    nature = Column(String)
    date_stationliquidation = Column(DateTime)  # was datetime
    state = Column(String)
    # column was changed, was PARMETER !!!
    # parameter = Column(String, primary_key=True)                  # vine, ...
    report_type = Column(String)  # exist only historical!! no such info for 'recent'
    report_resolution = Column(String)  # immediate or annual
    aoi = Column(String)
    ForeignKeyConstraint(
        columns=['phenostations.report_resolution', 'phenostations.report_type'],
        refcolumns=['dwdcatalogue.report_resolution', 'dwdcatalogue.report_type'],
        onupdate="CASCADE", ondelete="SET NULL")
    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())


class PhenoData(Base):
    """
    Template for the PhenoData Table
    """
    __tablename__ = 'phenodata'

    station_id = Column(Integer, primary_key=True)  # Stations_id
    reference_year = Column(Integer, primary_key=True)  # Referenzjahr
    quality_level = Column(Integer)  # Qualitaetsniveau
    object_id = Column(Integer, primary_key=True)  # Objekt_id
    phase_id = Column(Integer, primary_key=True)  # Phase_id
    reporting_date = Column(DateTime)  # Eintrittsdatum  # was datetime
    reporting_date_qb = Column(Integer)  # Eintrittsdatum_QB
    jultag = Column(Integer)  # Jultag
    report_type = Column(String)  # recent or historical; ## dont set to primary_key, because the recent data will be redirected to historical data with a time after data_quality check
    # main_object = Column(String, primary_key=True)          # Kartofel, Winterraps >>> defined in rcm.archive.knowledge.phenodata_codes
    report_resolution = Column(String, primary_key=True)  # immediate or annual
    parameter = Column(String)
    datatype_code = Column(String)
    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())
    ForeignKeyConstraint(
        columns=['phenodata.station_id', 'phenodata.reference_year',
                 'phenodata.object_id', 'phenodata.phase_id',
                 'phenodata.report_resolution', 'phenodata.report_type',
                 'phenodata.parameter', 'phenodata.datatype_code'],
        refcolumns=['phenostations.station_id', 'dwdcatalogue.year',
                    'phenoobjectcode.object_id', 'phenophasecode.phase_id',
                    'dwdcatalogue.report_resolution', 'dwdcatalogue.report_type',
                    'dwdcatalogue.parameter', 'dwdcatalogue.datatype_code'],
        onupdate="CASCADE", ondelete="SET NULL")
    UniqueConstraint('jultag')


class PhenoMetaData(Base):
    """
    Template for the PhenoMetaData Table to record Phenological description for an phenological Object
    """
    __tablename__ = 'phenometadata'
    object_id = Column(Integer, primary_key=True)
    # object = Column(String)         # => main_object
    phase_id = Column(Integer, primary_key=True)
    # phase = Column(String)
    phase_definition = Column(String)
    bbch_code = Column(String)
    reference_bbch = Column(String)
    report_type = Column(String)  # dont set to primary_key, because the recent data will be redirected to historical data with a time after data_quality check
    report_resolution = Column(String, primary_key=True)  # immediate or annual
    parameter = Column(String)
    parameter_code = Column(String)
    # main_object = Column(String)
    ForeignKeyConstraint(columns=['phenometadata.object_id', 'phenometadata.phase_id',
                                  'phenometadata.parameter_code', 'phenometadata.parameter',
                                  'phenometadata.report_resolution', 'phenometadata.report_type'],
                         refcolumns=['phenoobjectcode.object_id', 'phenophasecode.phase_id',
                                     'dwdparametercode.parameter_code', 'dwdparametercode.parameter',
                                     'dwdcatalogue.report_resolution', 'dwdcatalogue.report_type'],
                         onupdate="CASCADE", ondelete="SET NULL")
    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())


class PhenoAnomaly(Base):
    """
    Template for the PhenoAnomaly Table to record Anomalies for data_type='phenology'
    exist only for a report_type='historical', no such info for  report_type='recent'
    """
    __tablename__ = 'phenoanomaly'
    object_id = Column(Integer, primary_key=True)
    phase_id = Column(Integer, primary_key=True)
    year_end = Column(String)
    year_start = Column(String)
    comments = Column(String)
    anomaly_description = Column(String)
    short_name = Column(String)
    report_type = Column(String)  # exist only for historical no such info for 'recent'
    report_resolution = Column(String, primary_key=True)  # immediate or annual
    parameter = Column(String, primary_key=True)
    datatype_code = Column(String)
    parameter_code = Column(String)
    datetime_inserted = Column(DateTime(timezone=True), server_default=func.current_timestamp())
    ForeignKeyConstraint(columns=['phenoanomaly.object_id', 'phenoanomaly.phase_id',
                                  'phenoanomaly.report_resolution', 'phenoanomaly.report_type',
                                  'phenoanomaly.datatype_code', 'phenoanomaly.parameter_code',
                                  'phenoanomaly.parameter'],
                         refcolumns=['phenoobjectcode.object_id', 'phenophasecode.phase_id',
                                     'dwdcatalogue.report_resolution', 'dwdcatalogue.report_type',
                                     'dwdcatalogue.datatype_code', 'dwdparametercode.parameter_code',
                                     'dwdoparametercode.parameter'],
                         onupdate="CASCADE", ondelete="SET NULL")


class PhenoObjectCode(Base):
    """
    Template for an auxiliary atomic table PhenoObjectCode; values defined by DWD
    """
    __tablename__ = 'phenoobjectcode'
    object_id = Column(Integer, primary_key=True)  # 201, 202...
    object = Column(String)  # Dauergrünland, Winterweizen...


class PhenoPhaseCode(Base):
    """
    Template for an auxiliary atomic table PhenoPhaseCode; values defined by DWD
    """
    __tablename__ = 'phenophasecode'
    phase_id = Column(Integer, primary_key=True)  # 1, 5...
    phase = Column(String)  # Ergrünen Beginn, Blüte Beginn...




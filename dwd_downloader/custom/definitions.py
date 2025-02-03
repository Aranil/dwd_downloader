# -*- coding: utf-8 -*-
"""
@author: Aranil, Markus Zehner

Storage for needed variables

"""


#  DWD code (precipitation hourly): [color to plot, hex color code to plot,  nglish annotation of the precipitation code']
precip_hourly_label = {
        '0':["white", '#FFFFFF', 'no fallen precipitation or too little deposition (e.g., dew or frost) to form a precipitation height larger than 0.0']
      , '1': ["gainsboro", '#DCDCDC', 'precipitation height only due to deposition (dew or frost) or if it cannot decided how large the part from deposition is']
      , '2': ["lightblue", '#ADD8E6',  'precipitation height only due to liquid deposition']
      , '3': ["thistle", '#D8BFD8', 'precipitation height only due to solid precipitation']
      , '6': ["royalblue", '#4169E1', 'precipitation height due to fallen liquid precipitation, may also include deposition of any kind']
      , '7': ["indigo", '#4B0082', 'precipitation height due to fallen solid precipitation,may also include deposition of any kind']
      , '8': ["slategray", '#708090','fallen precipitation in liquid and solid form']
      , '9': ["black", '#000000', 'no precipitation measurement, form of precipitation cannot be determined']
      , 'nan':["white", '#FFFFFF', ' ']
     # , '-999':["white", '#FFFFFF', ' ']
        }

precip_hourly_label2 = {
        0:["white", '#FFFFFF', 'no fallen precipitation \nor too little deposition \n(e.g., dew or frost)\nto form a precipitation \nheight larger than 0.0']
      , 1: ["gainsboro", '#DCDCDC', 'precipitation height only \ndue to deposition \n(dew or frost) or if \nit cannot decided how \nlarge the part from deposition is']
      , 2: ["lightblue", '#ADD8E6',  'precipitation height only \ndue to liquid deposition']
      , 3: ["thistle", '#D8BFD8', 'precipitation height only \ndue to solid precipitation']
      , 6: ["royalblue", '#4169E1', 'precipitation height due \nto fallen liquid precipitation, \nmay also include deposition \nof any kind']
      , 7: ["indigo", '#4B0082', 'precipitation height due \nto fallen solid precipitation,\nmay also include deposition \nof any kind']
      , 8: ["slategray", '#708090','fallen precipitation in \nliquid and solid form']
      , 9: ["black", '#000000', 'no precipitation measurement, \nform of precipitation \ncannot be determined']
      , 'nan':["white", '#FFFFFF', ' ']
     # , '-999':["white", '#FFFFFF', ' ']
        }



# this is needed for update of phenodata to convert numbers back to
phenodata_codes = {'25': 'Rüben', '101': 'Beifuß', '102': 'Busch-Windröschen', '103': 'Eberesche', '104': 'Esche',
                   '105': 'Europäische', '106': 'Falscher', '107': 'Fichte', '108': 'Flieder', '109': 'Forsythie',
                   '110': 'Goldregen', '111': 'Birke', '112': 'Hänge-Birke', '113': 'Hasel', '114': 'Heidekraut',
                   '115': 'Herbstzeitlose', '116': 'Huflattich', '117': 'Hunds-Rose', '118': 'Kiefer',
                   '119': 'Kornelkirsche', '120': 'Löwenzahn', '121': 'Robinie', '122': 'Rosskastanie',
                   '123': 'Rotbuche', '124': 'Sal-Weide', '125': 'Schlehe', '126': 'Schneebeere',
                   '127': 'Schneeglöckchen', '128': 'Schwarz-Erle', '129': 'Schwarzer Holunder', '130': 'Sommer-Linde',
                   '131': 'Spitz-Ahorn', '132': 'Stiel-Eiche', '133': 'Tanne', '134': 'Traubenkirsche',
                   '135': 'Wiesen-Fuchsschwanz', '136': 'Wiesen-Knäuelgras', '137': 'Winter-Linde',
                   '138': 'Zweigriffliger', '139': 'Erle', '201': 'Dauergrünland', '202': 'Winterweizen',
                   '203': 'Winterroggen', '204': 'Wintergerste', '205': 'Winterraps', '206': 'Sommerweizen',
                   '207': 'Sommergerste', '208': 'Hafer', '209': 'Sonnenblume', '210': 'Mais', '215': 'Mais',
                   '231': 'Kartoffel', '232': 'Frühkartoffel', '233': 'Frühkartoffel', '234': 'Spätkartoffel',
                   '241': 'Grünpflück-Bohne', '242': 'Grünpflück-Erbse', '243': 'Tomate', '244': 'Weißkohl',
                   '245': 'Luzerne', '246': 'Rotklee', '250': 'Sorte', '252': 'Futter-Rübe', '253': 'Zucker-Rübe',
                   '310': 'Apfel', '311': 'Apfel', '312': 'Apfel', '313': 'Apfel', '320': 'Birne', '321': 'Birne',
                   '322': 'Birne', '330': 'Süßkirsche', '331': 'Süßkirsche', '332': 'Süßkirsche', '340': 'Sauerkirsche',
                   '350': 'Stachelbeere', '360': 'Rote', '361': 'Johannisbeere', '370': 'Pflaume', '371': 'Pflaume',
                   '372': 'Pflaume', '380': 'Aprikose', '381': 'Pfirsich', '382': 'Himbeere', '383': 'Brombeere',
                   '384': 'Erdbeere', '410': 'Weinrebe', '411': 'Weinrebe', '412': 'Weinrebe', '413': 'Weinrebe',
                   '414': 'Weinrebe', '501': 'Feldarbeit', '601': 'Weidegang', '4111': 'Müller-Thurgau',
                   '4112': 'Faber', '4131': 'Riesling', '4132': 'Scheurebe'}


# definition of more readable column names for table 'WeatherDataHourly'
colnames_WDH = { # original_dwd_names: created_names_for_DB
                  'STATIONS_ID': 'station_id'
                , 'MESS_DATUM': 'datetime'
                , 'air_temperature_tt_tu': 'air_temperature_200'
                , 'air_temperature_rf_tu': 'relative_humidity_200'
                , 'air_temperature_quality_level': 'air_temperature_quality_level'
                , 'cloudiness_v_n_i': 'cloudiness_source'
                , 'cloudiness_v_n': 'cloudiness_total_cover'
                , 'cloudiness_quality_level': 'cloudiness_quality_level'
                , 'precipitation_r1': 'precipitation_height'
                , 'precipitation_rs_ind': 'precipitation_fallen'
                , 'precipitation_wrtr': 'precipitation_form'
                , 'precipitation_quality_level': 'precipitation_quality_level'
                , 'pressure_p': 'pressure_normalized'
                , 'pressure_p0': 'pressure_station'
                , 'pressure_quality_level': 'pressure_quality_level'
                , 'soil_temperature_v_te002': 'soil_temperature_002'
                , 'soil_temperature_v_te005': 'soil_temperature_005'
                , 'soil_temperature_v_te010': 'soil_temperature_010'
                , 'soil_temperature_v_te020': 'soil_temperature_020'
                , 'soil_temperature_v_te050': 'soil_temperature_050'
                , 'soil_temperature_v_te100': 'soil_temperature_100'
                , 'soil_temperature_quality_level': 'soil_temperature_quality_level'
                , 'sun_sd_so': 'sun_duration'
                , 'sun_quality_level': 'sun_quality_level'
                , 'visibility_v_vv_i': 'visibility_source'
                , 'visibility_v_vv': 'visibility_value'
                , 'visibility_quality_level': 'visibility_quality_level'
                , 'wind_f': 'wind_speed'
                , 'wind_d': 'wind_direction'
                , 'wind_quality_level': 'wind_quality_level'
                }


colnames_WMeta = {
                  'Stations_ID': 'station_id'
                , 'Von_Datum': 'date_start'
                , 'Bis_Datum': 'date_end'
                , 'Stationsname': 'station_name'
                , 'Parameter': 'parameter_code'
                , 'Parameterbeschreibung': 'parameter_description'
                , 'Einheit': 'unit'
                #, 'Unnamed: 12': 'Unnamed'
                , 'Datenquelle (Strukturversion=SV)': 'source'
                , 'Zusatz-Info': 'additional_info'
                , 'Besonderheiten': 'special_features'
                , 'Literaturhinweis': 'bibliography'
                }


colnames_WStat = {
                  'Stations_id': 'station_id'
                , 'von_datum': 'date_start'
                , 'bis_datum': 'date_end'
                , 'Stationshoehe': 'height'
                , 'geoBreite': 'geo_lat'
                , 'geoLaenge': 'geo_lon'
                , 'geometry_wkt': 'station_pos' #should be calculated
                , 'Stationsname': 'name'
                , 'Bundesland': 'state'
                #,  'parameter': >>> WD parameter

                }


colnames_PD = {
              'Stations_id': 'station_id'
            , 'Referenzjahr': 'reference_year'
            , 'Qualitaetsniveau': 'quality_level'
            , 'Objekt_id': 'object_id'
            , 'Phase_id': 'phase_id'
            , 'Eintrittsdatum': 'reporting_date'
            , 'Eintrittsdatum_QB': 'reporting_date_qb'
            , 'Jultag': 'jultag'
            #, 'eor': 'eor'
            #, 'Unnamed: 9': ''

            }


colnames_PMeta = {
                  'Objekt_id': 'object_id'
                , 'Objekt': 'object'
                , 'Phasen_id': 'phase_id'
                , 'Phase': 'phase'
                , 'Phasendefinition': 'phase_definition'
                , 'BBCH_Code': 'bbch_code'
                , 'Hinweis BBCH': 'reference_bbch'
                , 'eor': 'eor'
               # , 'Unnamed: 8': ''
                 }


colnames_PStat = {
                  'Stations_id': 'station_id'
                , 'Stationsname': 'name'
                , 'geograph.Breite': 'geo_lat'
                , 'geograph.Laenge': 'geo_lon'
                , 'geometry_wkt': 'station_pos' #should be calculated
                , 'Stationshoehe': 'height'
                , 'Naturraumgruppe_Code': 'naturegroup_code'
                , 'Naturraumgruppe': 'naturegroup'
                , 'Naturraum_Code': 'nature_code'
                , 'Naturraum': 'nature'
                , 'Datum Stationsaufloesung': 'date_stationliquidation'
                , 'Bundesland': 'state'
                , 'eor': 'eor'
                #, 'Unnamed: 12': ''
                }


colnames_PAnnomal = {
                      'Jahr_Ende': 'year_end'
                    , 'Bemerkungen': 'comments'
                    , 'Besonderheitenbeschreibung': 'anomaly_description'
                    , 'Jahr_Beginn': 'year_start'
                    , 'Objekt_id': 'object_id'
                    , 'Kurzbezeichnung': 'short_name'
                    , 'Phasen_id': 'phase_id'
                    }


dict_phen_report_types = {
                  'Sofortmelder': 'immediate'
                , 'Jahresmelder': 'annual'
                }


dict_phen_parameter_types = {
                  'Landwirtschaft': 'crops'
                , 'Obst': 'fruit'
                , 'Wein': 'vine'
                , 'Weinrebe': 'vine'
                , 'Wildwachsende': 'wild'
                , 'Feldarbeit': 'farm'
                , 'Weidegang': 'farm'
                }

crops = {
              'Sommergerste': ['Spring barley', 'greenyellow', 'A']
            , 'Wintergerste':  ['Winter barley', 'olive', 'B']
            , 'Winterweizen': ['Winter wheat', 'teal', 'C']
            , 'Winterraps': ['Rapeseed',  'gold', 'D']
            , 'Raps': ['Rapeseed',  'gold', 'D']
            , 'Koernermais': ['Corn', 'darkgreen', 'E']
            , 'Mais': ['Corn', 'darkgreen', 'E']
            , 'Mais (ohne Sortenangabe)': ['Corn (unknown cultivar)', 'darkgreen', 'J']
            , 'Zuckerrueben': ['Sugar beet', 'limegreen', 'F']
            , 'Zuckerruebe': ['Sugar beet', 'limegreen', 'F']
            , 'Zucker-Rübe': ['Sugar beet', 'limegreen', 'F']
            , 'Ackerbohnen': ['Field bean', 'black', 'G']
            , 'Winterdurum': ['Durum wheat', 'black', 'H']
            , 'Hartweizen': ['Durum wheat', 'black', 'H']
            , 'Bluehflaeche': ['Grassland', 'black', 'H']
        }

crop_code = {
              'Sommergerste': ['SG']
            , 'Wintergerste':  ['WG']
            , 'WGerste': ['WG']
            , 'Winterweizen': ['WW']
            , 'Weizen': ['WW']
            , 'WWeizen': ['WW']
            , 'Winterraps': ['WR']
            , 'WRaps': ['WR']
            , 'WIR u. Mais': ['WR'] # WinterRaps unter Mais
            , 'Raps': ['WR']
            , 'Koernermais': ['KM']
            , 'SMais': ['SM']
            , 'Mais': ['SM']
            , 'Ackerbohne und Koernermais': ['KM']
            , 'Zuckerrueben': ['ZR']
            , 'ZRueben': ['ZR']
            , 'ZRüben': ['ZR']
            , 'Zuckerruebe': ['ZR']
            , 'Zucker-Rübe': ['ZR']
            , 'Herbst Zwischenfrüchte/Zuckerrueben': ['ZR']
            , 'Ackerbohnen': ['AB']
            , 'Winterroggen': ['WRg']
            , 'Roggen': ['WRg']
            , 'Winterdurum': ['WD']
            , 'Hartweizen': ['HW']
            , 'Bluehflaeche': ['BF']
            , 'Hafer': ['HA']
            , 'Unkraut_Kamele_usw': ['UNK']
            , 'Zwischenfrucht': ['ZwFr']
            , '':['']
            , 'Unknown':['UkN']
            , 'Wiese':['W']
            , 'ZRueben, WWeizen': ['ZR-WW']



        }

# ------------------------------------------
# # MARKERS for DWD Phase on English!!!
# ------------------------------------------
##      Phase_id (DWD): [ marker to plot,  Phase (DWD) on english, Phase (DWD) on german, color to plot]
# TODO: check the englisch labels after BBCH Buch!!!
markers = {

    # sugar beet
    14: ["*", 'begin of rosette formation/leaf development', 'Rosettenbildung Beginn', 'lightgreen'],
    13: ['o', 'crop cover complete/rosette growth', 'Bestand geschlossen', 'darkolivegreen'],

    ## rapeseed
    67: ["v", 'begin of stem elongation', 'Längenwachstum Beginn', 'green'],
    17: ["+", 'begin of flower buds formation', 'Knospenbildung Beginn', 'olivedrab'],
    5: ['^', 'begin of flowering', 'Blüte Beginn', 'yellow'],
    6: ['^', 'full flowering/anthesis', 'Vollblüte', 'yellow'],
    7: ["v", 'end of flowering', 'Blüte Ende', 'gold'],
    22: ["1", 'begin of full ripening', 'Vollreife Beginn', 'orangered'],

    # cereals
    18: ["s", 'begin of heading', 'Ährenschieben Beginn', 'darkslategray'],
    19: ["2", 'begin of milk ripening', 'Milchreife Beginn', 'tomato'],
    20: ['D', 'begin of early dough ripening', 'Teigreife Beginn', 'brown'],
    21: ['D', 'begin of hard dough ripening', 'Gelbreife Beginn', 'brown'],

    10: [",", 'begin of germination', 'Bestellung Beginn', 'peru'],
    12: [",", 'leaf development', 'Auflaufen Beginn', 'lightgreen'],
    15: ["v", 'stem elongation', 'Schossen Beginn', 'green'],

    # corn
    65: ["x", 'begin of tassel emergence', 'Fahnenschieben Beginn', 'greenyellow'],
    37: ['o', 'tips of stigmata visible', 'Narbenfädenschieben Beginn', 'yellow'],


    # harvest
    23: ["p", 'manual harvest', 'Ernte von Hand', 'k'],
    24: ["p", 'harvest', 'Ernte', 'k'],
    38: ['p', 'harvest of kernels', 'Körner-Ernte Beginn', 'k'],
    39: ["v", 'begin of silage harvesting', 'Silo-Ernte Beginn', 'k'],

# 'palevioletred',  'tomato', 'teal', 'goldenrod', 'saddlebrown', 'darkkhaki'
}



station_colors_dict = {
                        # FRIEN
                        'Dachwig (Ph)':['red', '15km', '*'],
                        'Günstedt (Ph)':['steelblue', '30km', '+'],
                        'Gangloffsömmern':["orange", '26km', 'x'],
                        'Gierstädt': ["olive", '14.5km', 'o'],
                        'Ballstädt':["green", '17.6km', 'D'],
                        'Erfurt-Mittelhausen':["slategrey", '11.3 km', 's'],
                        # DEMM
                        'Greifswald': ['red', '15km', '*'],
                        'Tützpatz': ['steelblue', '30km', '+'],
                        'Wendisch Baggendorf-Leyerhof': ["orange", '26km', 'x'],
                        'Dargun': ["olive", '14.5km', 'o'],
                        'Teterow (Kerngemeinde)': ["green", '17.6km', 'D'],
                        # MRKN
                        'Burgstein-Grobau': ['red', '15km', '*'],
                        'Hundshübel': ['steelblue', '30km', '+'],
                        'Zschorlau (Beob.-Stelle 1)': ["orange", '26km', 'x'],
                        'Mylau': ["olive", '14.5km', 'o'],
                        'Hartmannsdorf b. Kirchberg/SN (Beob. 1)': ["green", '17.6km', 'D'],
                        'Breitenbrunn/Erzgebirge': ["slategrey", '11.3 km', 's']
                        }




#  code of crop stages: [ english annotation of the stage ]
crop_stages = {
               1: [' I. stem elongation  '],
               2: [' II. heading'],
               #22: [' II. flower buds\nformation'],
               22: [' II. flower buds formation'],
               222: [' II. flowering'],
               2222: [' II. fruit development'],
               3: [' III. ripening'],
               4: ['   harvest ']
                }

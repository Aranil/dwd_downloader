# dwd_downloader
This module is a customized extension of dbflow, designed to automate downloading DWD (Deutscher Wetterdienst) data from the HTTP(S) web server and import it in an SQLite database. It leverages web scraping technique.




### If required module can be customized and extended 


### Update `config.ini`

Edit `config.ini` in the `dwd_downloader` module to point to the other than `custom` folder in your project:
Paths should be defined relative to the location of this config.ini file.
Use forward slashes (`/`) for cross-platform compatibility.

```ini
[paths]
custom_sql_dir = ./custom/sql
custom_db_structure = ./custom/db_structure.py
executed_sql_dir = ../_sql_executed
```

Edit `.env` File with Paths to a location of the DB to be stored and temp folder 
```env
DB_PATH=F:\...\dwd_downloader\_DB\dwd.db
DWD_CATCH_FOLDER_PATH=F:\...\dwd_downloader\_temp
```


```
#### **Application Directory (`dwd_downloader/`)**
```plaintext
├── custom/                 
│   ├── sql/               
│   │   ├── db_structure.py         # defintion of the DB table structure, DWD specific
│   │   ├── DB_utility_dwd.py       # DWD specific module for web-scraping data from FTP
│   │   ├── definitions.py          # defintions of the column names for renaming (from german to english), DWD specific
├── scripts/        
│   ├── load_dwd_data_toDB.py       # script to run the data download, project specific
├── .env               # Setting paths to DB loaction
├── config.ini         # Configuration file for paths
├── config.py          # RCM Project specific configuration 

```


As the main focus of the module is on parameters required for the RCM project, some DWD-specific parameters may be missing.
If a parameter is missing, it may not be defined in definitions.py yet. In such cases, you will see the message:

"... not defined in definitions.py yet!"

in the following database overview tables:

    dwdparametercode (parameter) – Contains DWD-specific parameter codes and unit definitions.
    dwdcatalogue (parameter) – Provides an overview of DWD-specific data.
    datacatalogue (datatype_name) – A general overview table for global project metadata, including RCM and other data sources beyond DWD.

Next Steps:
Check definitions.py to verify or extend the list of supported parameters as needed.


## Citation
If you use this project in your work, please cite it using the information in the [CITATION.cff](./CITATION.cff) file or via the "Cite this repository" button on GitHub.

Thank you for supporting open science! 🙌


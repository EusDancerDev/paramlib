#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Thu Jun  9 12:14:15 2022

@author: jon ander

** DISCLAIMER **
This program serves as a module to store parameters that are used frequently or globally.

*GLOBAL PARAMETERS MODULE STRUCTURE*

1. Time-Related Parameters
2. Mathematical Concepts
3. Programming Concepts
4. Socio-Economical Concepts

All constant names in this module are in uppercase following Python naming conventions.
"""

#%% 1. TIME-RELATED PARAMETERS

#------#
# Time #
#------#

# Basic time format strings
BASIC_TIME_FORMAT_STRS = {
    "H": "%Y-%m-%d %H:%M:%S",
    "H_NODATESEP": "%Y%m%d %H:%M:%S",
    "D": "%Y-%m-%d",
    "D_NODATESEP": "%Y%m%d",
    "M": "%Y-%m",
    "Y": "%Y"
}

# Non-standard time format strings
NON_STD_TIME_FORMAT_STRS = {
    "CFT_H": "%a %b %d %H:%M:%S %Y",
    "CFT_D": "%a %b %d %Y",
    "CFT_M": "%b %Y"
}

# Custom time format strings
CUSTOM_TIME_FORMAT_STRS = {
    "CT_EXCEL_SPANISH_H": "%d/%m/%y %H:%M:%S",
    "CT_EXCEL_SPANISH_NOBAR_H": "%d%m%y %H:%M:%S",
    "CT_EXCEL_SPANISH_D": "%d/%m/%y",
    "CT_EXCEL_SPANISH_NOBAR_D": "%d%m%y"
}

# Month number to letter mapping
MONTH_NUMBER_DICT = {
    1: "J", 2: "F", 3: "M", 4: "A", 5: "M", 6: "J", 7: "J", 
    8: "A", 9: "S", 10: "O", 11: "N", 12: "D"
}

# Seasonal time frequency dictionary
SEASON_TIME_FREQ_DICT = {
    1: "Q-JAN", 2: "Q-FEB", 3: "Q-MAR", 4: "Q-APR", 
    5: "Q-MAY", 6: "Q-JUN", 7: "Q-JUL", 8: "Q-AUG", 
    9: "Q-SEP", 10: "Q-OCT", 11: "Q-NOV", 12: "Q-DEC"
}

# Mathematical approximation for year length
MATHEMATICAL_YEAR_DAYS = 360

# Time frequencies
TIME_FREQUENCIES_COMPLETE = ["year", "season", "month", "day", "hour", "minute", "second"]
TIME_FREQUENCIES_SHORT_1 = ["yearly", "seasonal", "monthly", "daily", "hourly"]
TIME_FREQUENCIES_SHORTER_1 = ["year", "seas", "mon", "day", "hour"]

# Supported date units
PANDAS_DATE_UNIT_LIST = ['D', 'ms', 'ns', 's', 'us']
NUMPY_DATE_UNIT_LIST = ['Y', 'M', 'D', 'h', 'm', 's', 'ms', 'us', 'ns']

UNIT_FACTOR_DICT = {
    "D": 1000,
    "s": 1,
    "ms": 1e-3,
    "us": 1e-6,
    "ns": 1e-9
}

#%% 2. MATHEMATICAL CONCEPTS

# Basic operators
BASIC_FOUR_RULES = ["+", "-", "*", "/"]

# Set algebra
OPERATIONS_SETS_LIST = [
    "union", "difference", "intersection", 
    "symmetric_difference", "comparison"
]

#%% 3. PROGRAMMING CONCEPTS

# Operative Systems
FILESYSTEM_CONTEXT_MODULES = ["os", "Path", "shutil", "subprocess"]  # 'Path' from 'pathlib' module
STORAGE_ENTITY_TYPES = ["file", "directory"]

# Regular expressions
REGEX_PASSWORDS = r"^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_\W]).+$"

# Strings
COMMON_DELIM_LIST = ["_", "-", ";", ":", ",", "\n", "\t", " "]

#%% 4. SOCIO-ECONOMICAL CONCEPTS

# Climate change
EMISSION_RCP_SCENARIOS = ["historical", "rcp26", "rcp45", "rcp85"]
CLIMATE_FILE_EXTENSIONS = ["nc", "grib", "netcdf_zip", "csv"]

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
** DISCLAIMER **
This program serves as a module to store configuration data
like credentials, host info, etc.

*GLOBAL PARAMETERS MODULE STRUCTURE*

1. Programming Concepts
"""

#%% 1. PROGRAMMING CONCEPTS

# Databases
DATABASE_CREDENTIALS = {
    "username": "username",
    "password": "cool-password",
    "host": "host",
    "database_name": "dbname"
}

data_uploading_error_dict = {
    "1007": "Database already exists",
    "1045": "Wrong username",
    "1049": "Unknown database name",
    "1698": "Wrong password",
    "2003": "Wrong host name"
}
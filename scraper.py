import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import json      # library for working with JSON-formatted text strings
import pprint as pp    # library for cleanly printing Python data structures
import seaborn as sns
import twitterscraper as ts
from twitterscraper import query_tweets #library downloaded
import os as os

import subprocess #this enables us to pass CL code directly from Jupyter Notebooks
from subprocess import Popen

def json_to_df(json_file):
    with open(json_file) as f:
        data = json.load(f)

    d = {'username': [x['username'] for x in data],
        'time': [x['timestamp'] for x in data],
        'tweet': [x['text'] for x in data],
        'likes': [x['likes'] for x in data],
        'replies': [x['replies'] for x in data],
        'user_ID' : [x['screen_name'] for x in data]}


    return pd.DataFrame.from_dict(d)

def combine_data(*data_frames): #this will allow us to merge dataframes "*" allows us to pass X dataframes
    return pd.concat(data_frames)

def buildQuery(accounts):
    scraper_query = ''

    #this builds our search query
    for index, each_account in enumerate (accounts):
        next_index = index + 1 #this is so that we don't have an extra "OR" at the end, it "knows" the last thing
        if next_index > len(accounts) - 1:
            scraper_query = scraper_query + "from:"+ each_account
        else:
            scraper_query = scraper_query + "from:"+ each_account + " OR "

    return scraper_query

def launch(command, output):
    print (command)

    outputFile = open(output, 'w+')
    p = Popen(command, stdout=outputFile, stderr=outputFile, universal_newlines=True)
    output, errors = p.communicate()
    #p.wait() # Wait for sub process to finish before moving on to make frame

    print (errors)
    myoutput.close()

def scrape(accounts):

    #twitterscraper_query = buildQuery(accounts)
    for user in accounts:
        path_to_output_file = user + ".txt" #we'll get both txt and json, but just ignore txt
        path_to_data_file = user + ".JSON"

        command = ["twitterscraper", 'from: ' + user,
                   "--lang", "en", "-o", path_to_data_file, "--all", "-ow", "-p", "40"]
        launch(command, path_to_output_file)

    #command = ["twitterscraper", twitterscraper_query, "--lang", "en", "-o", path_to_data_file, "--all", "-ow", "-p", "40"]

    #launch(command, path_to_output_file)

    return path_to_data_file



def __main__():
    # "SeattleOPCD", "CityofSeattle", "seattledot", "SeattleOSE", "kcmetrobus",
    climate_emergency_accounts = [ "LACity", "LADOTofficial", "lacountyparks", "HCIDLA", "Planning4LA", "metrolosangeles", "PortofLA",
                             "NYC_DOT", "NYCParks", "NYCHA", "NYCPlanning", "nycemergencymgt", "MTA" ,
                             "chicago", "ChicagoDOT", "ChicagoParks", "ChicagoDOH", "ChicagoDPD", "ChicagoOEMC", "cta",
                             "CityofSanDiego", "sandiegoparks", "SanDiegoPlan", "ReadySanDiego", "sdcountydpw", "sdmts", "portofsandiego",
                             "CityofSanJose", "SanJoseDOT", "sjparksandrec", "sjcityhousing", "buildingsanjose", "VTA",
                             "austintexasgo", "austinmobility", "AustinCityParks", "Hacanet", "ImagineAustin", "AustinHSEM", "AusPublicHealth", "CapMetroATX",
                             "SFEnvironment", "sfmta_muni", "RecParkSF", "sfplanning", "SF_emergency", "sfpublicworks", "SFPort",
                             "CityOfBoston", "BostonEnviro", "BostonBTD", "BostonParksDept", "BHA_Boston", "BostonPlans", "AlertBoston", "HealthyBoston", "MBTA",
                             "DenverCityGov", "SustainableDen", "DenverDOTI", "denverparksrec", "DenverCPD", "DDPHE"]
    climate_emergency_output = scrape(climate_emergency_accounts)

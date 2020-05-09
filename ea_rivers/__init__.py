# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:25:31 2020

@author: User
"""

import pandas as pd
import requests

def get_stations():
    """Get details of river monitoring stations from EA API

      :return: a pandas data frame of river monitoring stations

      >>> get_stations()
  """
    
    api_url = "https://environment.data.gov.uk/flood-monitoring/id/stations"
    
    # Get data about stations from the EA API
    response = requests.get(api_url)

    # Extract JSON data from the response
    data = response.json()

    # Load data to a data frame
    stations = pd.DataFrame(data["items"])

    return(stations)



def get_measures():
    api_url = "http://environment.data.gov.uk/flood-monitoring/id/measures"
    """Get details of measures available from river monitoring stations on the EA API

      :return: a pandas data frame of river monitoring measures

      >>> get_stations()
  """
    # Get data about measures from the EA API
    response = requests.get(api_url)

    # Extract JSON data from the response
    data = response.json()

    # Load data to a data frame
    measures = pd.DataFrame(data["items"])

    return(measures)
    

def get_readings_for_measure(measure_id):
    """Gets readings for a given measure from the EA river monitoring API

      :param measure_id: EA API measure id
      :return: a pandas data frame of readings for the measure

      >>> get_readings_for_measure('http://environment.data.gov.uk/flood-monitoring/id/measures/L0215-level-stage-i-15_min-m')
  """
    api_url = measure_id + "/readings"
    
    # Get data about readings from the EA API
    response = requests.get(api_url)

    # Extract JSON data from the response
    data = response.json()

    # Load data to a data frame
    readings = pd.DataFrame(data["items"])

    return(readings)

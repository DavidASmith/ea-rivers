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
    
    # Get data about measures from the EA API
    response = requests.get(api_url)

    # Extract JSON data from the response
    data = response.json()

    # Load data to a data frame
    measures = pd.DataFrame(data["items"])

    return(measures)
    

def get_readings_for_measure(measure_id):
    """Gets readings for a given measure from the EA river monitoring API

      :param measure_id: text to be tokenized
      :return: a pandas data frame of readings for the measure

      >>> get_readings_for_measure('the rain in spain')
  """
    api_url = measure_id + "/readings"
    
    # Get data about readings from the EA API
    response = requests.get(api_url)

    # Extract JSON data from the response
    data = response.json()

    # Load data to a data frame
    readings = pd.DataFrame(data["items"])

    return(readings)

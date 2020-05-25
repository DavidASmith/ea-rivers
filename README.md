# ea_rivers

## Summary

ea_rivers is a package to help you acquire information from England's [Environment Agency Real Time flood-monitoring API](https://environment.data.gov.uk/flood-monitoring/doc/reference).

There are three main concepts in the package and API.

* Stations - Monitoring stations which return information about the state of a river.
* Measures - Each station records one or more measures, for example: flow or level.
* Readings - Readings are the value of a particular measure at a given time.

## Getting started

Get details of all available monitoring stations.

    ea_rivers.get_stations()

Get details of all available measures.

    ea_rivers.get_measures().
    
Get details of all available readings for a given measure from today.

    ea_rivers.get_readings_for_measure('http://environment.data.gov.uk/flood-monitoring/id/measures/L0215-level-stage-i-15_min-m', 
                                       today = True)

All data is returned as Pandas DataFrame.

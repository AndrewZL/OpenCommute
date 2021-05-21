<h1>Open Commute</h1>

  <p>
    Compiling and analyzing Toronto's cycling volumes and accidents to create an accessible measure of cyclist safety  
    <br />
    
<!-- ![GNU License][license-shield] -->
![Version][version-shield]


## Table of Contents

* [Requirements](#requirements)
* [Data](#data)

### Requirements
* Python
* Numpy
* Pandas
* sklearn
#### Visualization Requirements
* Streamlit 
* Pydeck

### Data
* Data for cyclist volumes was compiled from <a href = https://open.toronto.ca/dataset/bicycle-counts/> City of Toronto Transportation Services </a>
    * Raw Data is found in /Data/raw
    * Data was manually compiled and geocoded
    * Temperature and precipitation data were excluded
        * In theory, the sampling should represent the average weather patterns in Toronto and thus the average volumes took into account cyclist counts on all days, including those with harsher weather
    * The second CSV which excludes data from trails and parks is used, as this project is concerned with commuting accidents rather than recreational ones 
    * A third CSV which averages data into a general weekday and weekend volume is in progress
* Data for commuter accidents is from the <a href= https://data.torontopolice.on.ca/pages/ksi>Toronto Police Service Public Safety Data Portal </a>
* Data includes: intersection name, longitude, latitude, average cyclist volume per hour for each day in a week
* Open Data License: <a href=https://open.toronto.ca/open-data-license/> Open Government License - Toronto </a>

### KDE
Since data for volume is sparse (only collected at certain intersections), hotspots were extrapolated using kernel density estimation from the sklearn library.
Based on https://doi.org/10.1016/j.aap.2008.12.014.

[license-shield]: https://img.shields.io/badge/license-GPLv3-green
[version-shield]: https://img.shields.io/badge/version-2.0.0-important

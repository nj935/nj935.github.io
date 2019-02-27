Annual average predicted surface for NO2, PM2.5, and NO; summer average for ozone and winter average for SO2. Prediction surface generated from LUR modeling of December 2008- December 2016 (years 1-8) New York Community Air Survey monitoring data.As these are estimated annual average levels produced by a statistical model, they are not comparable to short term localized monitoring or monitoring done for regulatory purposes. 

Data values: 
PM2.5: predicted fine particulte matter <2.5 microns, ug/m3
NO2: predicted ppb
NO: predicted ppb
Ozone: predicted ppb
SO2: ppb predicted
file: ESRI grid raster file at 300 meter resolution
file naming convention: season plus prediction year (e.g. aa1= annual average year 1 (Dec 2008-Dec 2009); s5= summer average year 5 (June-August 2013); w2= winter average year 2 (Dec 2009-February 2010))
projection: NAD 83, New YOrk Long Island State PLane FIPS, feet
output by: Sarah Johnson, DOHMH, March, 2018

Data collection:
The New York City Community Air Survey monitors fine particles (PM2.5), Nitrogen Oxides (NOX), Sulfur Dioxide (SO2), Ozone (O3) and elemental carbon (EC) at 155 locations throughout New York City during each season of the year.  Data is collected over 2 week intervals at each of 150 distributed locations once per season. Data is collected at five reference sites in is two week period year round for temporally adjusting distributed site data. For more information on NYCCAS methods see http://www.nyc.gov/health/nyccas. Raw data is not directly representative of time and place where collected.  Sampling design requires that raw data be temporally adjusted based on reference site values and modeled to account for nearby emission sources and landscape factors in order to calculate the distribution of constituent across NYC. Placement of monitors was not done to describe a specific neighborhood's air quality or evaluate emissions from unique facilities but to capture variable influence of sources distributed across the city (for example, traffic or oil burning boilers). Geospatial data on traffic, buildings and other emissions indicators are available through other data stewards as described in NYCCAS technical appendix, available as described below.  NYCCAS data cannot be compared to monitoring done for regulatory purposes because of differences in sampling techniques. 

Land-use Regression development:
Using raw monitored values, land-use regression models were developed with an indictor for week of monitoring to adjust for the influence of weather and non-local emissions sources,  and ajusted for spatial autocorrelation, when appropriate.  See http://www1.nyc.gov/site/doh/data/data-publications/air-quality-nyc-community-air-survey.page for emissions covariates by pollutant.  Citywide predicted values were generated at 100m grid centroids, then smoothed using IDW incorporating the 100 nearest centroids.


Data Quality			
The NYCCAS data must pass several quality assurance tests throughout the sample collection, laboratory analysis, and data analysis process.  For details on the QA/QC procedure, reliability of co-located measures and agreement with regulatory federal reference monitoring methods, please see Technical Appendices at http://www.nyc.gov/health/nyccas.
 				
Dates Available for Analytic Purposes
December 2008 through December 2016
				
More Information About Source Data
Sampling design and analysis notes available by request from the Bureau of Environmental Surveillance and Policy
New York City Department of Health and Mental Hygiene
nyccas@health.nyc.gov
				
Suggested Citation		
The New York City Department of Health and Mental Hygiene, Queens College Center for the Biology of Natural Systems, and Zev Ross Spatial Analysis.

Additional files in this folder:
Matte et al 2013jes 2012 126.pdf- description of nyccas design











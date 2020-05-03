import pandas as pd 
#Save subsets of the original data into csv files for easy web visualization 

State_List = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

 
df_raw = pd.read_csv("Data/DSIRE_Program_data.csv")

df_dsire = df_raw[["ProgramId", "Name", "State", "ImplementingSectorName", "CategoryName", "TypeName", "FundingSource", "Budget", "StartDate", "EndDate", "Technologies", "Sectors"]]

#Filter out non U.S. states
df_states = df_dsire[(df_dsire["State"] != "American Samoa") & (df_dsire["State"] != "District of Columbia") & (df_dsire["State"] != "Federated States of Micronesia") & (df_dsire["State"] != "Guam") & (df_dsire["State"] != "Federal") & (df_dsire["State"] != "N. Mariana Islands") & (df_dsire["State"] != "Palau") & (df_dsire["State"] != "Puerto Rico") & (df_dsire["State"] != "Virgin Islands")]

df_stateCount = df_states["ProgramId"].groupby(df_states["State"]).count()

stateCount_csv = df_stateCount.sort_values(ascending = False)
#Save file as csv for visualization
#stateCount_csv.to_csv("Data/stateCount.csv")

df_FICount = df_states[(df_states["CategoryName"] == "Financial Incentive")].groupby(["State"]).count()
df_RPCount = df_states[(df_states["CategoryName"] == "Regulatory Policy")].groupby(["State"]).count()
df_TRCount = df_states[(df_states["CategoryName"] == "Technical Resource")].groupby(["State"]).count()
FICount_csv = df_FICount["ProgramId"].sort_values(ascending = False)
RPCount_csv = df_RPCount["ProgramId"].sort_values(ascending = False)
TRCount_csv = df_TRCount["ProgramId"].sort_values(ascending = False)

#save files as csv for visualization
#FICount_csv.to_csv("Data/FICount.csv")
#RPCount_csv.to_csv("Data/RPCount.csv")
#TRCount_csv.to_csv("Data/TRCount.csv")

df_programs = df_states.groupby(["TypeName"]).count()
programs_csv = df_programs["ProgramId"].sort_values(ascending = False)
#Save file as csv for visualization
#programs_csv.to_csv("Data/programs.csv")

#df_technologies = df_states["ProgramId"].groupby(df_states["Technologies"]).count()
#df_technologies = df_technologies.to_string()
#df_sectors.to_csv("Data/sectorCount.csv")
#file = open('Data/technologies.json', 'w')
#file.write(df_technologies)
#file.close()

df_hvacr = df_states[(df_states['Technologies'].str.contains('HVAC') == True) | (df_states['Technologies'].str.contains('Water Heaters') == True) | (df_states['Technologies'].str.contains('Thermostat') == True) | (df_states['Technologies'].str.contains('Air conditioners') == True) | (df_states['Technologies'].str.contains('Heat pumps') == True) | (df_states['Technologies'].str.contains('Heat pumps') == True) | (df_states['Technologies'].str.contains('Boilers') == True) | (df_states['Technologies'].str.contains('Geothermal Heat Pumps') == True) | (df_states['Technologies'].str.contains('Combined Heat') == True) | (df_states['Technologies'].str.contains('Chillers') == True) | (df_states['Technologies'].str.contains('Furnaces') == True)]
df_hvacrCount = df_hvacr["ProgramId"].groupby(df_hvacr["CategoryName"]).count()

df_appliances = df_states[(df_states['Technologies'].str.contains('Clothes Washers') == True) | (df_states['Technologies'].str.contains('Dishwasher') == True) | (df_states['Technologies'].str.contains('Refrigerator') == True) | (df_states['Technologies'].str.contains('Ceiling Fan') == True) | (df_states['Technologies'].str.contains('Lighting') == True) | (df_states['Technologies'].str.contains('Motor') == True) | (df_states['Technologies'].str.contains('Cooking') == True) | (df_states['Technologies'].str.contains('Lighting') == True)]
df_appliancesCount = df_appliances["ProgramId"].groupby(df_appliances["CategoryName"]).count()

df_buildings = df_states[(df_states['Technologies'].str.contains('Combined Heat') == True) | (df_states['Technologies'].str.contains('Insulation') == True) | (df_states['Technologies'].str.contains('Steam-system') == True) | (df_states['Technologies'].str.contains('Compressed air') == True) | (df_states['Technologies'].str.contains('Building') == True) | (df_states['Technologies'].str.contains('Caulking') == True)  | (df_states['Technologies'].str.contains('sealing') == True)  | (df_states['Technologies'].str.contains('Windows') == True) | (df_states['Technologies'].str.contains('Doors') == True) | (df_states['Technologies'].str.contains('Siding') == True) | (df_states['Technologies'].str.contains('Roof') == True)  | (df_states['Technologies'].str.contains('Data Center') == True)  | (df_states['Technologies'].str.contains('Industrial') == True)  | (df_states['Technologies'].str.contains('Load Management') == True)]
df_buildingsCount = df_buildings["ProgramId"].groupby(df_buildings["CategoryName"]).count()

df_fuel = df_states[(df_states['Technologies'].str.contains('Biomass') == True) | (df_states['Technologies'].str.contains('Hydrogen') == True) | (df_states['Technologies'].str.contains('Solid Waste') == True) | (df_states['Technologies'].str.contains('Fuel') == True) | (df_states['Technologies'].str.contains('Landfill') == True)  | (df_states['Technologies'].str.contains('Renewable Energy') == True)  | (df_states['Technologies'].str.contains('Anaerobic') == True) | (df_states['Technologies'].str.contains('Generation Technologies') == True)  | (df_states['Technologies'].str.contains('Energy Sources') == True) | (df_states['Technologies'].str.contains('Lithium') == True)]
df_fuelCount = df_fuel["ProgramId"].groupby(df_fuel["CategoryName"]).count()

df_geo = df_states[(df_states['Technologies'].str.contains('Geothermal Electric') == True) | (df_states['Technologies'].str.contains('Geothermal Direct') == True)]
df_geoCount = df_geo["ProgramId"].groupby(df_geo["CategoryName"]).count()

df_hydro = df_states[(df_states['Technologies'].str.contains('Hydro') == True) | (df_states['Technologies'].str.contains('Tidal') == True) | (df_states['Technologies'].str.contains('Wave') == True) | (df_states['Technologies'].str.contains('Ocean') == True) | (df_states['Technologies'].str.contains('turbines') == True)]
df_hydroCount = df_hydro["ProgramId"].groupby(df_hydro["CategoryName"]).count()

df_other = df_states[(df_states['Technologies'].str.contains('Personal com') == True) | (df_states['Technologies'].str.contains('Processing and') == True) | (df_states['Technologies'].str.contains('Agricultural') == True) | (df_states['Technologies'].str.contains('Custom/Others') == True)  | (df_states['Technologies'].str.contains('Other EE') == True)  | (df_states['Technologies'].str.contains('not identified') == True)  | (df_states['Technologies'].str.contains('Food Service') == True)  | (df_states['Technologies'].str.contains('Vending') == True)  | (df_states['Technologies'].str.contains('Pool Pumps') == True)]
df_otherCount = df_other["ProgramId"].groupby(df_other["CategoryName"]).count()

df_solar = df_states[(df_states['Technologies'].str.contains('Solar') == True) | (df_states['Technologies'].str.contains('Daylighting') == True)]
df_solarCount = df_solar["ProgramId"].groupby(df_solar["CategoryName"]).count()

df_wind = df_states[(df_states['Technologies'].str.contains('Wind') == True)]
df_windCount = df_wind["ProgramId"].groupby(df_wind["CategoryName"]).count()

"""
print("HVACR",df_hvacrCount)
print("Appliances",df_appliancesCount)
print("Buildings",df_buildingsCount)
print("Fuels",df_fuelCount)
print("Geothermal",df_geoCount)
print("Hydro",df_hydroCount)
print("Other",df_otherCount)
print("Solar",df_solarCount)
print("Wind",df_windCount)
"""
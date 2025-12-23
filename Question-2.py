# Group Name: DAN/EXT 01
# Group Members: 4
# Member 1: Md Hasibul Raihan - S397592
# Member 2: Tanisa Sanam Vabna - S397593
# Member 3: JESHIKA SAPKOTA - S399269
# Member 4: LADDAPORN DAWSON - S382273

# -----------------------------
# Python Program: Temperature Data Analysis
# Description: This program reads temperature data from multiple CSV files
# (each representing one year) from the "temperatures" folder, then:
# 1. Calculates seasonal average temperatures across all stations and years
# 2. Identifies station(s) with the largest temperature range
# 3. Finds stations with the most stable and most variable temperatures
# -----------------------------

import pandas as pd
import glob
import os

# -----------------------------
# 1. Set path to CSV folder and find all CSV files
# -----------------------------
folder_path = "temperatures"  # Folder containing CSV files
all_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Check if any CSV files are found
if not all_files:
    print("No CSV files found in the folder:", folder_path)
else:
    print(f"Found {len(all_files)} CSV files:")
    for f in all_files:
        print("-", f)

# -----------------------------
# 2. Load all CSVs and combine into a single DataFrame
# -----------------------------
data_list = []

for file in all_files:
    df = pd.read_csv(file)
    
    # Transform months from columns to rows for easier processing
    df_melt = df.melt(
        id_vars=['STATION_NAME', 'STN_ID', 'LAT', 'LON'],  # Keep station info
        value_vars=['January','February','March','April','May','June','July','August',
                    'September','October','November','December'],  # Months to melt
        var_name='Month', 
        value_name='Temperature'
    )
    data_list.append(df_melt)

# Combine all years
all_data = pd.concat(data_list, ignore_index=True)

# Remove rows with missing temperature values
all_data = all_data.dropna(subset=['Temperature'])

# Display sample data for verification
print("\nSample of combined data:")
print(all_data.head())
print("Total rows after combining:", len(all_data))

# -----------------------------
# 3. Map months to Australian seasons
# -----------------------------
month_to_season = {
    'December':'Summer', 'January':'Summer', 'February':'Summer',
    'March':'Autumn', 'April':'Autumn', 'May':'Autumn',
    'June':'Winter', 'July':'Winter', 'August':'Winter',
    'September':'Spring', 'October':'Spring', 'November':'Spring'
}
all_data['Season'] = all_data['Month'].map(month_to_season)

# -----------------------------
# 4. Seasonal Average Temperature
# -----------------------------
seasonal_avg = all_data.groupby('Season')['Temperature'].mean()

# Save seasonal averages to file (UTF-8 to prevent Â issues)
with open("average_temp.txt", "w", encoding="utf-8") as f:
    for season in ['Summer', 'Autumn', 'Winter', 'Spring']:
        f.write(f"{season}: {seasonal_avg[season]:.1f}°C\n")

print("\nSeasonal averages saved to average_temp.txt")

# -----------------------------
# 5. Station with Largest Temperature Range
# -----------------------------
# Calculate max, min, and range per station
station_stats = all_data.groupby('STATION_NAME')['Temperature'].agg(['max','min'])
station_stats['range'] = station_stats['max'] - station_stats['min']

# Find station(s) with the largest range
max_range = station_stats['range'].max()
largest_range_stations = station_stats[station_stats['range'] == max_range]

# Save results to file (UTF-8)
with open("largest_temp_range_station.txt", "w", encoding="utf-8") as f:
    for station, row in largest_range_stations.iterrows():
        f.write(f"Station {station}: Range {row['range']:.1f}°C (Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C)\n")

print("Largest temperature range station(s) saved to largest_temp_range_station.txt")

# -----------------------------
# 6. Temperature Stability per Station
# -----------------------------
# Calculate standard deviation per station
station_std = all_data.groupby('STATION_NAME')['Temperature'].std()

# Most stable and most variable stations
min_std = station_std.min()
max_std = station_std.max()

most_stable = station_std[station_std == min_std]
most_variable = station_std[station_std == max_std]

# Save results to file (UTF-8)
with open("temperature_stability_stations.txt", "w", encoding="utf-8") as f:
    for station, std in most_stable.items():
        f.write(f"Most Stable: Station {station}: StdDev {std:.1f}°C\n")
    for station, std in most_variable.items():
        f.write(f"Most Variable: Station {station}: StdDev {std:.1f}°C\n")

print("Temperature stability station(s) saved to temperature_stability_stations.txt")

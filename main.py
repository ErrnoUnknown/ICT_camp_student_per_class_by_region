# Import
import os
import shutil
import json
import pandas as pd
import folium
import yaml

# Load config
with open('config/config.yml', encoding='utf-8') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

    AGES_TO_VISUALIZE = config['ages_to_visualize']
    MAP_STYLE = config['map_style']
    FILL_COLOR = config['fill_color']
    FILL_OPACITY = config['fill_opacity']

# Define functions
def remove_html_files_in_dir(dir_path):
    for root, _, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".html"): os.remove(os.path.join(root, file))

# Load data
data = pd.read_excel('data/avg_students_per_class_by_age.xlsx')

# Load geojson data
with open('data/korea.geojson', 'r', encoding='utf-8') as file:
    geo_data = json.load(file)

# Init regions
regions = data.columns[1:].tolist()

# Init students_per_class_by_age
students_per_class_by_age = {}

for age in range(8, 20):
    students_per_class_by_age[str(age)] = [round(value, 2) for value in data.iloc[age - 9].tolist()[1:]]

# Clear previous outputs
remove_html_files_in_dir('map/')

# Visualize
for age in range(8, 20):
    # Skip age if not used
    if age not in AGES_TO_VISUALIZE:
        continue
    
    # Init data_df
    data_df = pd.DataFrame({'region': regions,
                            'student': students_per_class_by_age[str(age)]})

    # Init map
    result_map = folium.Map(location=[36.5, 127.5],
                            zoom_start=7,
                            tiles=MAP_STYLE)

    # Init choropleth
    folium.Choropleth(
        geo_data=geo_data,
        data=data_df,
        columns=('region', 'student'),
        key_on='feature.properties.CTP_KOR_NM',
        fill_color=FILL_COLOR,
        fill_opacity=FILL_OPACITY,
        legend_name=f'학급별 평균 학생 수 ({age}세)'
    ).add_to(result_map)

    # Add tooltip
    folium.features.GeoJson(
        geo_data,
        name='geojson',
        tooltip=folium.features.GeoJsonTooltip(fields=['CTP_KOR_NM'], labels=False)
    ).add_to(result_map)

    # Save map
    result_map.save(f'map/map_{age}.html')

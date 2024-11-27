import folium
import pandas  as pd 

map = folium.Map(location=(40.6350,-73.9921))
data_file = pd.read_csv("Data.csv")
borough_park = data_file.groupby("NTA").get_group("Borough Park")
# borough_park.to_csv('borough.csv')

print(len(borough_park))

for i in borough_park.index:
   folium.Marker([borough_park["Latitude"][i], borough_park["Longitude"][i]]).add_to(map)
    


map.save("index.html")

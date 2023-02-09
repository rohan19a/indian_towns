import geopandas as gpd
import matplotlib.pyplot as plt

#show a map of india
plt.rcParams['figure.figsize'] = (20, 10)
df_places = gpd.read_file('india.geojson')

df_admin = gpd.read_file('algiers_algeria_expanded_admin.geojson')
ax = df_admin.plot(color='blue')



for idx, row in df_places.iterrows():
    if row['population'] > 10000:
        coordinates = row['geometry'].coords.xy
        x, y = coordinates[0][0], coordinates[1][0]
        ax.annotate(row['name'], xy=(x, y), xytext=(x, y))


df_places.plot(ax=ax, column='population', scheme='quantiles', cmap='OrRd')


#save the map
plt.savefig("india.png")

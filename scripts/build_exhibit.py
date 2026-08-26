import geopandas as gpd
from shapely.geometry import Point, Polygon
import os

# Output Location
output_dir = "C:/Users/Beast/Documents/SJWRWP_Investigaiton/output"
os.makedirs(output_dir, exist_ok=True)
output_gpkg = os.path.join(output_dir, "San_Jacinto_USACE_AOI.gpkg")

# Points Layer
points_data = {
    "Name": ["Site Center (EPA-verified)", "Reference Point (2010 field photos)"],
    "Description": [
        "Coordinates: 29.7944 N, -95.0625 W. Source: EPA OSC Response site profile, site_id 6534.",
        "Coordinates: approx. 29.7958 N, -95.068 W. Source: EPA site_id 6534 photo metadata, Dec. 2010."
    ],
    "geometry": [
        Point(-95.0625, 29.7944),
        Point(-95.0680, 29.7958)
    ]
}
points_gdf = gpd.GeoDataFrame(points_data, crs="EPSG:4326")

# Polygon Layer (AOI Boundary)
poly_data = {
    "Name": ["Requested Search Area (Area of Interest)"],
    "Description": ["Estimated bounding area for FOIA search purposes, extending to the Houston Ship Channel confluence."],
    "geometry": [Polygon([
        (-95.0825, 29.8050),
        (-95.0425, 29.8050),
        (-95.0425, 29.7580),
        (-95.0825, 29.7580),
        (-95.0825, 29.8050),   # closes back to the starting point
    ])]
}
poly_gdf = gpd.GeoDataFrame(poly_data, crs="EPSG:4326")

# Write both layers into one GeoPackage
points_gdf.to_file(output_gpkg, layer="AOI_Points", driver="GPKG")
poly_gdf.to_file(output_gpkg, layer="AOI_Boundary", driver="GPKG")

print("Saved GeoPackage to:", output_gpkg)

#commentagaain
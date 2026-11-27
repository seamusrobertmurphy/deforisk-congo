# Input data

Every third-party dataset the manuscript reads is listed here with its publisher, the link it was retrieved from, its licence and the date it was retrieved. The same name and link sit in a comment directly above the manuscript line that reads the file, so the next reader can fetch it without opening this page.

Raw downloads stay out of git under `02.inputs/<source>/raw/`, and the manuscript fetches each one inside a guarded chunk that downloads only when the file is missing. Derived tables the manuscript writes go to `03.outputs/TBL/` and are committed.

## Sources

Each source takes one entry in this form.

| Field | Entry |
|---|---|
| Dataset | Full name as the publisher gives it |
| Publisher | Agency or data centre |
| Link | Landing page, and the DOI as an https link where one exists |
| Licence | Licence name |
| Retrieved | ISO date |
| Local path | `02.inputs/<source>/raw/<file>` |
| Read by | Manuscript chunk label |

### GADM boundaries

| Field | Entry |
|---|---|
| Dataset | GADM version 4.1, level 1 boundaries of the Democratic Republic of the Congo |
| Publisher | GADM, University of California, Davis |
| Link | https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_COD_1.json.zip |
| Licence | Free for academic and other non-commercial use, redistribution not allowed without permission, maps for academic articles allowed, https://gadm.org/license.html |
| Retrieved | 2026-11-19 |
| Local path | `02.inputs/gadm/raw/gadm41_COD_1.json.zip` |
| Read by | `study-area`, `pressure-sources`, `travel-time` |

### GLanCE training data

| Field | Entry |
|---|---|
| Dataset | GLanCE training dataset, version 1 |
| Publisher | Boston University, on Source Cooperative |
| Link | https://data.source.coop/boston-university/bu-glance/bu_glance_training_dataV1.parquet, https://doi.org/10.34911/rdnt.x4xfh3 |
| Licence | CC BY 4.0 |
| Retrieved | 2026-11-19 |
| Local path | `02.inputs/glance/raw/bu_glance_training_dataV1.parquet` |
| Read by | `glance-samples` |

### Sentinel-2 images

| Field | Entry |
|---|---|
| Dataset | Harmonized Sentinel-2 MSI, MultiSpectral Instrument, Level-1C (TOA), `COPERNICUS/S2_HARMONIZED` |
| Publisher | European Space Agency, Copernicus programme, served by Earth Engine |
| Link | https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_HARMONIZED |
| Licence | As stated under the catalog page's terms of use |
| Retrieved | 2026-11-19, read in Earth Engine |
| Local path | none, read in Earth Engine |
| Read by | `forest-maps` |

### Cloud Score+

| Field | Entry |
|---|---|
| Dataset | Cloud Score+ S2_HARMONIZED V1, `GOOGLE/CLOUD_SCORE_PLUS/V1/S2_HARMONIZED` |
| Publisher | Google, served by Earth Engine |
| Link | https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED, https://doi.org/10.1109/CVPRW59228.2023.00206 |
| Licence | As stated under the catalog page's terms of use |
| Retrieved | 2026-11-19, read in Earth Engine |
| Local path | none, read in Earth Engine |
| Read by | `forest-maps` |

### SRTM elevation

| Field | Entry |
|---|---|
| Dataset | NASA SRTM Digital Elevation 30m, `USGS/SRTMGL1_003` |
| Publisher | NASA and USGS, served by Earth Engine |
| Link | https://developers.google.com/earth-engine/datasets/catalog/USGS_SRTMGL1_003, https://doi.org/10.5067/MEaSUREs/SRTM/SRTMGL1_NC.003 |
| Licence | As stated under the catalog page's terms of use |
| Retrieved | 2026-11-19, read in Earth Engine, and 2026-11-27 at 500 m for the map relief |
| Local path | none for `forest-maps`, and `02.inputs/srtm/raw/srtm_500m.tif` for the map relief |
| Read by | `forest-maps`, `map-backdrop` |

### GADM territories

| Field | Entry |
|---|---|
| Dataset | GADM version 4.1, level 2 boundaries of the Democratic Republic of the Congo |
| Publisher | GADM, University of California, Davis |
| Link | https://geodata.ucdavis.edu/gadm/gadm4.1/json/gadm41_COD_2.json.zip |
| Licence | Free for academic and other non-commercial use, redistribution not allowed without permission, maps for academic articles allowed, https://gadm.org/license.html |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/gadm/raw/gadm41_COD_2.json.zip` |
| Read by | `pressure-sources` |

### WorldPop 2018

| Field | Entry |
|---|---|
| Dataset | Modelled gridded population estimates for the Kinshasa, Kongo-Central, Kwango, Kwilu, and Mai-Ndombe provinces in the Democratic Republic of the Congo, version 2.0 |
| Publisher | WorldPop, University of Southampton |
| Link | https://data.worldpop.org/repo/wopr/COD/population/v2.0/, https://doi.org/10.5258/SOTON/WP00669 |
| Licence | CC BY-SA 4.0 |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/worldpop/raw/COD_population_v2_0_gridded.zip` |
| Read by | `pressure-sources`, `pressure-layers` |

### WorldPop 2024

| Field | Entry |
|---|---|
| Dataset | Bottom-up gridded population estimates for Maï-Ndombe Province in the Democratic Republic of Congo, version 4.4 |
| Publisher | WorldPop, University of Southampton |
| Link | https://data.worldpop.org/repo/wopr/COD/population/v4.4/Province/Mai_Ndombe/, https://doi.org/10.5258/SOTON/WP00867 |
| Licence | CC BY 4.0 |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/worldpop/raw/COD_Mai_Ndombe_province_population_v4.4_gridded.zip` |
| Read by | `pressure-sources`, `pressure-layers` |

### GRID3 settlement names

| Field | Entry |
|---|---|
| Dataset | GRID3 COD - Settlement Names v9.0 |
| Publisher | GRID3 and the Center for International Earth Science Information Network, Columbia University |
| Link | https://data.grid3.org/datasets/f4a459a34e43476a9a9671c4095bddd9/about, https://doi.org/10.7916/77t0-h465, read through https://services3.arcgis.com/BU6Aadhn6tbBEdyk/arcgis/rest/services/GRID3_COD_settlement_names_v9_0/FeatureServer |
| Licence | CC BY 4.0 |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/grid3/raw/settlement_names_v9_0.gpkg`, merged from the pages in `02.inputs/grid3/raw/settlement_names_v9_0/` |
| Read by | `pressure-sources`, `pressure-layers` |

### GRID3 roads

| Field | Entry |
|---|---|
| Dataset | GRID3 COD - Roads v1.0 |
| Publisher | GRID3 and the Center for International Earth Science Information Network, Columbia University |
| Link | https://data.grid3.org/datasets/b489c28df02247e3b227dc1adee1dad4/about, https://doi.org/10.7916/00gb-e164, read through https://services3.arcgis.com/BU6Aadhn6tbBEdyk/arcgis/rest/services/GRID3_COD_roads_v1_0/FeatureServer |
| Licence | CC BY-SA 4.0 |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/grid3/raw/roads_v1_0.gpkg`, merged from the pages in `02.inputs/grid3/raw/roads_v1_0/` |
| Read by | `pressure-sources`, `travel-time` |

### Forest roads

| Field | Entry |
|---|---|
| Dataset | Congo Basin Forest Roads, January 2019 to December 2024, `projects/wurnrt-loggingroads/assets/distribution/forestroads_afr_2019-01_2024-12` |
| Publisher | Slagter et al. (2024), served by Earth Engine through the community catalog |
| Link | https://gee-community-catalog.org/projects/forest_roads/, https://doi.org/10.1016/j.rse.2024.114380 |
| Licence | CC BY 4.0 |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/forestroads/raw/forest_roads_2019_2024.geojson` |
| Read by | `pressure-sources`, `pressure-layers`, `travel-time` |

### Charcoal shares

| Field | Entry |
|---|---|
| Dataset | Rapport d'étude sur l'organisation de la filière bois-énergie de la ville de Kinshasa, Figure 9, page 23 |
| Publisher | CIRAD, Programme de consommation durable et substitution partielle au bois-énergie |
| Link | http://agritrop.cirad.fr/600203/1/20220106_Rapport_Filie%CC%80re_bois_e%CC%81nergie_Kinshasa_CIRAD_Vf.pdf |
| Licence | Report, cited as `dubiez2021rapport` |
| Retrieved | 2026-11-22, four values entered from the figure |
| Local path | none, the values sit in `pressure-sources` |
| Read by | `pressure-sources` |

### Walking friction

| Field | Entry |
|---|---|
| Dataset | Global friction surface, walking only, 2019, version 5.1, `projects/malariaatlasproject/assets/accessibility/friction_surface/2019_v5_1_walking_only` |
| Publisher | Malaria Atlas Project, from Weiss et al. (2020), served by Earth Engine |
| Link | https://developers.google.com/earth-engine/datasets/catalog/projects_malariaatlasproject_assets_accessibility_friction_surface_2019_v5_1_walking_only, https://doi.org/10.1038/s41591-020-1059-1 |
| Licence | CC BY 4.0 |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/map/raw/friction_walking_2019.tif` |
| Read by | `travel-time` |

### GHSL settlement model

| Field | Entry |
|---|---|
| Dataset | GHS-SMOD R2023A, degree of urbanisation settlement model, 2020, `JRC/GHSL/P2023A/GHS_SMOD_V2-0` |
| Publisher | European Commission Joint Research Centre, served by Earth Engine |
| Link | https://developers.google.com/earth-engine/datasets/catalog/JRC_GHSL_P2023A_GHS_SMOD_V2-0, https://doi.org/10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA |
| Licence | Open and free data, reuse authorised provided the source is acknowledged |
| Retrieved | 2026-11-22 |
| Local path | `02.inputs/ghsl/raw/smod_2020.tif` |
| Read by | `travel-time` |

### GRIP4 roads

| Field | Entry |
|---|---|
| Dataset | GRIP4 Global Roads Inventory Project, Africa, `projects/sat-io/open-datasets/GRIP4/Africa` |
| Publisher | GLOBIO, PBL Netherlands Environmental Assessment Agency, from Meijer et al. (2018), served by the Earth Engine community catalog |
| Link | https://gee-community-catalog.org/projects/grip/, https://doi.org/10.1088/1748-9326/aabd42 |
| Licence | CC BY 4.0, as listed by the community catalog |
| Retrieved | 2026-11-27 |
| Local path | `02.inputs/grip4/raw/grip4_africa.geojson` |
| Read by | `pressure-sources`, `travel-time` |

### Microsoft roads

| Field | Entry |
|---|---|
| Dataset | Bing Maps mined roads, Middle Africa, release of 28 April 2025 |
| Publisher | Microsoft |
| Link | https://github.com/microsoft/RoadDetections, https://usaminedroads.z19.web.core.windows.net/drops/2025.04.28/Middle_Africa.zip |
| Licence | Open Data Commons Open Database License |
| Retrieved | 2026-11-27 |
| Local path | `02.inputs/msroads/raw/Middle_Africa.zip`, with the roads of the Democratic Republic of the Congo in `msroads_cod.gpkg` |
| Read by | `pressure-sources`, `travel-time` |

### HRSL population

| Field | Entry |
|---|---|
| Dataset | High Resolution Settlement Layer, overall population, `projects/sat-io/open-datasets/hrsl/hrslpop` |
| Publisher | Facebook Connectivity Lab and the Center for International Earth Science Information Network, served by the Earth Engine community catalog |
| Link | https://gee-community-catalog.org/projects/hrsl/, https://dataforgood.fb.com/tools/population-density-maps/ |
| Licence | CC BY 4.0, as listed by the community catalog |
| Retrieved | 2026-11-27, summed to 1 km in 16 tiles |
| Local path | `02.inputs/hrsl/raw/hrsl_1km.tif` |
| Read by | `market-access` |

### HydroSHEDS rivers

| Field | Entry |
|---|---|
| Dataset | Free Flowing Rivers, HydroSHEDS, `WWF/HydroSHEDS/v1/FreeFlowingRivers`, reaches with a mean discharge of 100 m³/s or more |
| Publisher | World Wildlife Fund, served by Earth Engine |
| Link | https://developers.google.com/earth-engine/datasets/catalog/WWF_HydroSHEDS_v1_FreeFlowingRivers |
| Licence | As stated under the catalog page's terms of use |
| Retrieved | 2026-11-27 |
| Local path | `02.inputs/hydrosheds/raw/rivers.geojson` |
| Read by | `map-backdrop` |

### HydroLAKES lakes

| Field | Entry |
|---|---|
| Dataset | HydroLAKES version 1.0, `projects/sat-io/open-datasets/HydroLakes/lake_poly_v10`, lakes of 10 km² or more |
| Publisher | HydroSHEDS, served by the Earth Engine community catalog |
| Link | https://gee-community-catalog.org/projects/hydrolakes/ |
| Licence | As listed by the community catalog |
| Retrieved | 2026-11-27 |
| Local path | `02.inputs/hydrolakes/raw/lakes.geojson` |
| Read by | `map-backdrop` |

### Natural Earth

| Field | Entry |
|---|---|
| Dataset | Natural Earth 1:10 million populated places and admin 0 countries, version 5.1.2 |
| Publisher | Natural Earth |
| Link | https://www.naturalearthdata.com/downloads/10m-cultural-vectors/, https://naciscdn.org/naturalearth/10m/cultural/ne_10m_populated_places.zip, https://naciscdn.org/naturalearth/10m/cultural/ne_10m_admin_0_countries.zip |
| Licence | Public domain |
| Retrieved | 2026-11-27 |
| Local path | `02.inputs/naturalearth/raw/` |
| Read by | `map-backdrop` |

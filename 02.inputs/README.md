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
| Retrieved | 2026-11-19, read in Earth Engine |
| Local path | none, read in Earth Engine |
| Read by | `forest-maps` |

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

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
| Read by | `study-area` |

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

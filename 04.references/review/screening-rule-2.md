# Screening rule 2

Written 12 November 2026 for the full screen, under the second deviation in `protocol.md`. It replaces `screening-rule.md`, which is kept as frozen. Both readers apply this rule to the title and abstract of each record, and to nothing else.

## Decision

Each record takes one decision.

1. `include` when the record bears on at least one of the eight questions below, and deforestation or forest change is a central subject of it. For question 8, forest or land use change need only enter the record's model as a predictor or an outcome.
2. `exclude` when it does not, with one reason code.
3. `undecided` when the abstract is missing or too short to decide. No claim is made about such a record, and its full text decides it later.

A record with no abstract is `undecided` whatever its title suggests. The one exception is a title showing that a search term matched something else, such as the dye Congo red, and that record is `off-topic`.

When a record could bear on a question but the abstract leaves it unclear, it is included. The full text reading removes it later if it fails. Exclusion is kept for records that plainly fail.

## Place

The Congo Basin means all land in Cameroon, the Central African Republic, the Democratic Republic of the Congo, Equatorial Guinea, Gabon and the Republic of the Congo. Savanna, woodland and dry forest count the same as humid forest. A record is in place when its study area lies wholly or partly in one of these countries. A regional, pantropical or global record is in place when its abstract names the Congo Basin or Central Africa as a study area or a reported result. Naming Africa's humid forest or one of the six countries counts the same way. Questions 4 and 6 need a place in the tropics but not in the six countries, and question 5 needs none.

## Period

Forest change of the distant past, rebuilt from pollen or lake sediment rather than from maps, records or images, bears on no question. Such a record is `wrong-concept`.

## Questions

1. The record maps, models, predicts, projects or simulates the risk, location or rate of deforestation or forest cover change in the Congo Basin.
2. The record measures or tests the drivers, causes or spatial predictors of deforestation or forest loss in the Congo Basin, from data. Logging, agriculture, roads, settlements, population, mining, charcoal, fire, conflict, tenure and protected areas all count as drivers.
3. The record produces, assesses, compares or validates a forest cover, forest change or land cover map, or its training or reference data, in the Congo Basin.
4. The record evaluates deforestation risk maps, projected deforestation baselines or forest reference levels anywhere in the tropics, for accuracy, bias, uncertainty or over-crediting. A record proposing a method for that evaluation counts too.
5. The record uses, assesses or describes the GLanCE training dataset or the GLanCE land cover products, anywhere, and its title or abstract names them. A record that cites a GLanCE paper without naming the data is `wrong-concept`.
6. The record builds, compares or validates a model or map that predicts the risk, location or rate of deforestation anywhere in the tropics. A record that maps past forest change and predicts nothing does not bear on question 6.
7. The record estimates, maps or accounts for greenhouse gas emissions or carbon losses from deforestation, forest degradation or land use change in the Congo Basin. A forest reference level or a REDD+ programme document that does so counts too.
8. The record maps or models a spatial risk other than deforestation in the Congo Basin, such as disease, landslides, flooding, fire or pests. Deforestation, forest loss, or land use or land cover change enters it as a predictor or an outcome.

## Exclusion codes

| Code | Use |
|---|---|
| `off-topic` | A search term matched something else, such as the dye Congo red or the ordinary word glance |
| `wrong-population` | The right concept in the wrong place, outside the Congo Basin for questions 1 to 3, 7 and 8, or outside the tropics for questions 4 and 6, and also when place and concept both fail |
| `wrong-concept` | The right place, with forest change absent or only background, such as forest carbon stocks, wildlife or timber yield with no change measured, and also a question 4 record that evaluates no baseline or risk map |
| `not-research` | An editorial, news item, correction, erratum, or data record with no method |
| `out-of-window` | No year |
| `not-english` | Neither English nor French |
| `duplicate` | The same work as another record, including its preprint |

## Output

Each reader returns one row per record with five fields.

1. `record_id`, as given.
2. `decision`, one of `include`, `exclude` or `undecided`.
3. `reason`, one code for an exclusion and blank otherwise.
4. `questions`, the question numbers an included or undecided record bears on, such as `q1 q7`.
5. `note`, fifteen words or fewer giving the deciding fact, in the reader's own words and never copied from the abstract.

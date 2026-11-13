# Charting rule

Written 13 November 2026 for the charting stage of `protocol.md`. It turns the seven charting columns into fields a reader fills from the title and abstract of one included record. Both readers apply it to the same ten records first, and the rule may be revised once from that pilot.

## Source

Each field is filled from the title and abstract alone. Nothing is taken from memory of the paper, from another record or from the web. Where the abstract does not say, the field reads `not stated`. A French abstract is charted in English, except for the copied passage, which stays in French.

## Fields

Each reader returns one row per record with these fields, in this order.

1. `record_id`, as given.
2. `questions`, the questions of `screening-rule-2.md` the abstract shows the record bears on, such as `q1 q7`. The screening entry is given with the record, and the reader corrects it where the abstract shows otherwise.
3. `place`, the countries, regions or sites studied, by name, such as `Democratic Republic of the Congo, Mai-Ndombe`. A record covering many countries names its scope, such as `pantropical` or `Central Africa`.
4. `area`, the size of the study area with its unit, as the abstract gives it.
5. `period`, the years the data cover, such as `2000 to 2020`, and the year projected to, if any, such as `projected to 2050`.
6. `data`, the forest change or land cover data used, by product name where given, such as `Hansen Global Forest Change` or `Landsat classification`.
7. `own_map`, whether the forest change or land cover map was made by the study itself. One of `yes`, `no`, `both` or `not stated`.
8. `method`, the model or mapping method by name, such as `random forest`, `logistic regression`, `Land Change Modeler` or `weighted sum of expert-scored factors`.
9. `predictors`, the predictors or drivers entered, separated by commas, as the abstract names them.
10. `validation`, how the map or model was checked, such as `independent reference sample`, `later years held out` or `cross-validation`.
11. `measures`, each accuracy or agreement measure with its value, as reported, such as `overall accuracy 89 per cent, AUC 0.82`.
12. `purpose`, one of `research`, `conservation planning`, `REDD+ reference level`, `carbon crediting`, `national monitoring`, `policy assessment` or `other`.
13. `finding`, the record's main result in the reader's own words, with its numbers where the abstract gives them. Thirty words or fewer.
14. `gap_quote`, one passage copied word for word from the abstract, where the record itself states a gap, limit, concern or need. It runs to 60 words at most, with nothing added, cut or changed inside it. The field is left blank when the abstract states none.

## Form

The `finding` field, and every field the reader writes in its own words, carries no dash, colon or semicolon used as punctuation. A hyphen inside a name, such as `CA-Markov`, is kept. Per cent is written out.

The `gap_quote` field is checked by script against the abstract after spaces are made single, and a passage that fails is returned to the reader. A passage is not taken from the title.

The `finding` field for a review or a commentary gives its main argument. For a dataset or a software record it gives what was released and where it applies.

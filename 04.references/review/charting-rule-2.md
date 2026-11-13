# Charting rule 2

Written 13 November 2026 for the full charting, under the fourth deviation in `protocol.md`. It revises `charting-rule.md` once, from the pilot of ten records charted by both readers. That file is kept as the rule the pilot used. The readers split on 22 of 130 fields, and 20 of the splits came from the rule rather than from the abstract. Each change below settles one of them.

## Source

Each field is filled from the title and abstract alone. Nothing is taken from memory of the paper, from another record or from the web. Where the abstract does not say, the field reads `not stated`. A French abstract is charted in English, except for the copied passage, which stays in French.

A record whose abstract shows it bears on no question keeps its screening entry, and the reader names it in its report for the full text reading to settle. A dataset, figure or supplement carrying its parent paper's abstract is charted from that abstract and named in the report, so that it can be merged with its paper.

## Fields

Each reader returns one row per record with these fields, in this order.

1. `record_id`, as given.
2. `questions`, the questions of `screening-rule-2.md` the abstract shows the record bears on, such as `q1 q7`. The screening entry is given with the record, and the reader corrects it where the abstract shows otherwise. Question 1 needs a risk map, a spatial model of forest change, or a prediction, projection or simulation of deforestation. A record that maps or measures past forest change and predicts nothing bears on question 3, not question 1. Question 7 needs an estimate, map or account of emissions or carbon losses, and emissions named only as the reason for the study do not count.
3. `place`, the countries, regions or sites studied, by name, such as `Democratic Republic of the Congo, Mai-Ndombe`. A record covering many countries names its scope, such as `pantropical` or `Central Africa`. Countries take their current names, so Zaire is written Democratic Republic of the Congo.
4. `area`, the size of the study area with its unit, as the abstract gives it. A buffer radius, a pixel size or a count of sites is not an area.
5. `period`, the years the data cover, such as `2000 to 2020`, and the year projected to, if any, such as `projected to 2050`.
6. `data`, the forest change or land cover data used, by product name where given, such as `Hansen Global Forest Change` or `Landsat classification`.
7. `own_map`, whether the study made its own forest, land cover or land use map. It reads `yes` when the study classified images into its own map, `no` when it used a map made by others, and `both` when it did both. It reads `not stated` when the abstract does not say, or when the study used no such map, such as a vegetation index alone.
8. `method`, the model or mapping method by name, such as `random forest`, `logistic regression`, `Land Change Modeler` or `weighted sum of expert-scored factors`. A sensitivity or uncertainty analysis is named here. A review, commentary or policy report with no method of its own reads `not stated`.
9. `predictors`, the variables a model or analysis entered to explain or predict forest change, separated by commas, as the abstract names them. For question 8 they are the variables entered to predict the risk modelled. Model parameters tested for sensitivity, the inputs of a cost and benefit comparison, and causes named but not measured are not predictors.
10. `validation`, how the record's own map or model output was checked, such as `independent reference sample`, `later years held out`, `cross-validation` or `compared with a rival model`. A sensitivity or uncertainty analysis is not validation, and neither is a comparison of two input datasets.
11. `measures`, each accuracy, agreement or error measure of that validation with its value, as reported, such as `overall accuracy 89 per cent, AUC 0.82`. A measure named without its value is entered as `root mean square error, value not stated`. A loss rate or an uncertainty range is a result, and it goes in `finding`.
12. `purpose`, the use the study was carried out for, as its stated aim gives it. The uses its closing sentences suggest do not count. When the aim names two, the first in this list after `research` is taken.
    - `research`, to measure, test or explain, with no named user.
    - `conservation planning`, to choose, design or manage areas for conservation.
    - `REDD+ reference level`, to set or assess a forest reference level or a REDD+ programme baseline.
    - `carbon crediting`, to set or assess a baseline or risk map for a crediting standard or project.
    - `national monitoring`, to build or assess a national system for monitoring or reporting forest change.
    - `policy assessment`, to assess or inform a policy, law or programme.
    - `other`, any other named user, such as urban or water planning.
13. `finding`, the record's main result in the reader's own words, with its numbers where the abstract gives them. Thirty words or fewer.
14. `gap_quote`, one passage copied word for word from the abstract, where the record itself states a gap, limit, concern or need. It runs to 60 words at most, with nothing added, cut or changed inside it. The passage may report the record's own result, such as a failure it found. When several passages qualify, the one naming the Congo Basin, Central Africa or one of the six countries is taken, and otherwise the first. The field is blank only when no passage of these kinds exists.

## Form

The `finding` field, and every field the reader writes in its own words, carries no dash, colon or semicolon used as punctuation. A hyphen inside a name, such as `CA-Markov`, is kept. Per cent is written out.

The `gap_quote` field is checked by script against the abstract after spaces are made single, and a passage that fails is returned to the reader. A passage is not taken from the title.

The `finding` field for a review or a commentary gives its main argument. For a dataset or a software record it gives what was released and where it applies.

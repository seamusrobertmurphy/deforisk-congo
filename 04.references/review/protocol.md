# Review protocol

Written 11 November 2026 for `deforisk-congo`, before any recorded query ran. It follows `library-science/protocols/literature-review.md`, escalated to the full method of the `scoping-review` skill. The escalation is made because the review is meant to find the gaps a new study could fill, so its findings rest on absences. The review follows Arksey and O'Malley (2005), Levac et al. (2010) and Peters et al. (2020), and it reports against PRISMA-ScR (Tricco et al. 2018).

The protocol is frozen by the commit that adds it. Until that commit, the SHA-256 digest of this file, `search-terms.csv` and `screening-rule.md` is written into every row of the search log. A row whose digest differs from the committed files ran under another protocol. Nothing above "Deviations" is edited after the commit.

## Purpose

The manuscript has no title, objectives or keywords yet. The review comes first, to find them. Seamus set its purpose on 11 November 2026 in these words.

> "I would like to apply here a scoping review. Of deforestation risk. Mapping in the Congo."

> "what we'll probably do in this study is we will map land use change with glance dataset, training datasets, and then we will begin to build a deforestation risk modeling. However, I want to do scoping review. I want to see what kind of literature there is out there, and I want to grab those kind of questions, like what's missing, what's needed, where is the technical gaps, what's been done so far, what's the current state of the literature on that specific question."

> "that'll give me an idea of what are the debates, what is the discussion, what are the concerns at the moment in the scientific literature."

After the pilot on the same day, Seamus widened the place and the methods searched. He was answering whether the review covered rainforest only, after the Verra tool VT0007 had been read.

> "No, not just rainforest. Like, I think deforestation is more important."

> "we also want to look beyond that to you know, the scientific literature for the best methodology and what are the risks and how to develop risk tools"

The result is used to set the manuscript's objectives and to design its land use change map and its deforestation risk model.

## Questions

The Congo Basin means all land in six countries, with savanna, woodland and dry forest counted the same as humid forest. These are Cameroon, the Central African Republic, the Democratic Republic of the Congo, Equatorial Guinea, Gabon and the Republic of the Congo. Each question is searched by one or more routes, named in `search-terms.csv`.

1. What methods have mapped, modelled or projected the risk, location or rate of deforestation in the Congo Basin, and how were they validated? Population Congo Basin forests, concept deforestation risk maps and spatial models of forest change, context research and REDD+ reference levels. Route `q1`.
2. Which drivers and spatial predictors of deforestation have been measured in the Congo Basin, and in which direction did each act? Population Congo Basin forests, concept the causes and spatial predictors of forest loss, context any. Route `q2`.
3. Which forest change and land cover maps, and which training and reference datasets, have measured deforestation in the Congo Basin, and how accurate and consistent were they there? Population Congo Basin forests, concept map accuracy, agreement and reference data, context remote sensing. Route `q3`.
4. How have deforestation risk maps and projected deforestation baselines been evaluated, and what concerns about their accuracy, bias and crediting have been raised? Population tropical forests anywhere, concept the evaluation of risk maps and baselines, context research, REDD+ and carbon crediting. Route `q4`.
5. Novelty. Has any study mapped land use change in the Congo Basin with the GLanCE training data or land cover products, or built a deforestation risk model from them? Population studies using GLanCE anywhere, concept land use change mapping and deforestation risk, context any. Routes `q5a` to `q5d`.
6. Which methods have built, compared and validated deforestation risk models across the tropics, and which predicted best? Population tropical forests anywhere, concept models that predict where deforestation will happen, context research, REDD+ and carbon crediting. Route `q6`.

Questions 4 and 6 are not limited to the Congo Basin, because risk models are built, compared and evaluated mostly in other tropical regions. A debate held elsewhere still governs how a Congo Basin model is judged.

## Adjudication

1. If a published model already maps deforestation risk across the whole Congo Basin and was validated against independent data, the new model is framed as a comparison with it. If models exist only for single countries or sites, a basin-wide model is new work.
2. If prior studies agree on the direction of a driver, that driver enters the attribute table with its expected direction. If they disagree, its direction is a hypothesis to be tested and is reported as contested.
3. If prior work shows that the forest change maps disagree in the Congo Basin, the choice of training data and map becomes a result the study must report. If the GLanCE training data was already assessed in Central Africa, that assessment is cited rather than repeated.
4. If prior work or a crediting standard sets how a risk map is to be validated, the study adopts it. If the question is still argued, the study's validation is designed to answer a named concern.
5. If any study has used GLanCE data to map land use change or to model deforestation risk in the Congo Basin, the manuscript is an extension of it. Otherwise the absence is checked against the full text of every candidate before it is stated.
6. If published comparisons agree that one kind of model predicts deforestation better than the others, the study builds that kind and tests it against the VT0007 benchmark. If they disagree, the study fits the contending kinds and reports which predicted best in the Congo Basin.

## Criteria

1. Document types admitted are peer-reviewed articles, reviews, chapters and conference papers. Preprints are admitted and marked as preprints. Agency reports, crediting standards and national reference level submissions are admitted where they are the primary source of a method, rule or data product.
2. No opening year, and records up to the date each search ran, because spatial models of deforestation predate the global forest change maps.
3. English and French, because French is an official language in all six countries.
4. A record bears on at least one question, and deforestation or forest change is a central subject of it rather than background to another subject.

Exclusions use the codes of the store protocol. The code `not-english` is read as outside the two languages admitted. No code is added.

## Sources

1. `library-science`, searched by `scripts/review_search.py store` on the titles in its manifest and the text of its source notes.
2. OpenAlex, searched by `scripts/review_search.py openalex` on titles and abstracts. The unkeyed service allowed about 100 requests a day on 11 November 2026, and it pages by number without a key. Routes `q5c` and `q5d` list every work OpenAlex records as citing the two GLanCE data papers.
3. Semantic Scholar bulk search, by `scripts/review_search.py s2`. It refused an unkeyed request with HTTP 429 during the pilot on 11 November 2026, so a refusal at search time is logged and reported.
4. Grey literature sought by hand, with route `grey`, its URL and the date retrieved. The places searched are the forest reference level submissions of the six countries on the UNFCCC REDD+ Web Platform, and the Verra unplanned deforestation methods and tools. The ART TREES standard and the emission reduction programme documents of the Forest Carbon Partnership Facility for the six countries are also searched.
5. One round of backward and forward citation chasing, from no more than five central records per question, chosen after screening.

No request carries an email address. Scopus and Web of Science need institutional keys, and Google Scholar allows no automated access, so none is searched.

The queries are built by the script from `search-terms.csv`. Terms sharing a concept within a route are joined by OR, and different concepts are joined by AND. The manuscript has no title or keywords yet. Each term is therefore marked `statement` where it is Seamus's own word of 11 November 2026, or `synonym` where the review added it. When the manuscript's keywords are set, every synonym the search used enters them.

## Pilot

The routes were piloted on OpenAlex on 11 November 2026 by counting matches only. The counts were 437 for `q1`, 543 for `q2`, 188 for `q4`, 2 for `q5a` and 11 for `q5b`. Route `q3` returned 387 before Zaire and Cameroun were added to the place terms. The two GLanCE papers had 73 and 95 citing works. A search on the bare acronym GLanCE without a second term returned works on the ordinary word glance, so `q5b` pairs it with Landsat or land cover. No record from the pilot was kept.

Route `q6` was added after the pilot screen on 11 November 2026, at Seamus's request, and four versions were counted on OpenAlex that day. The first version approved returned 372 records, most of them studies classifying satellite images. Its terms random forest and machine learning name image classifiers as often as risk models. The version kept returned 563, and it found a known validation study (Sloan and Pelletier 2012) that a narrower version missed.

Routes `q1` to `q5d` and the pilot screen ran under a first draft of this protocol, whose digest begins 7116d52b. That draft lacked question 6, and it defined the Congo Basin as the forests of the six countries. Every route is searched again under this text after the commit, and only the records of that search are screened.

## Screening

Two readers, reader A and reader B, read every title and abstract under `screening-rule.md`. Each reads without sight of the other's decisions. Both readers are language models, run in separate sessions with the same rule and the same records. Their agreement is reported as Cohen's kappa over include and exclude.

The rule is first tried on a pilot of 60 records, 12 drawn at random from each of the five questions. Seamus settles the pilot disagreements, and the rule may be revised once from his decisions before the full screen, as a dated deviation. Question 6 was added after the pilot, so its records were not piloted. A reader of the full screen who was not a pilot reader screens the same 60 records first, and the agreement of the new pair is reported. In the full screen, a record the readers disagree on is read a third time and settled, and the settlement is recorded with who made it.

Abstracts are kept in `02.inputs/review/raw/review-abstracts.csv`, outside git, because they are the publishers' text. The decisions are kept in `02.inputs/derived/review-records.csv`.

## Reading and charting

Every candidate for question 5 is read in full. So is every record behind an attribute row, an adopted method, a prior effect size or a claim of absence. Included records are charted on these columns, piloted first on ten records by both readers.

1. The questions the record bears on.
2. The country or site, the area and the period studied.
3. The forest change or land cover data used, and whether it was the study's own map.
4. The model or mapping method, and the predictors it entered.
5. How the map or model was validated, and the measures reported.
6. The purpose, such as research, conservation planning or a REDD+ reference level.
7. The gap, limit or concern the record itself states, with a passage copied word for word.

Every copied passage is checked by script against its abstract or full text. No critical appraisal of study quality is made, and the write-up says so.

## Files

| File | Holds |
|---|---|
| `04.references/review/protocol.md` | This protocol |
| `04.references/review/search-terms.csv` | Every search term, its route, concept and source |
| `04.references/review/screening-rule.md` | The rule both readers screen by |
| `04.references/review/scripts/` | The search, merge and sampling scripts |
| `02.inputs/derived/review-search-log.csv` | One row per query per source, with date, string, count, cap and digest |
| `02.inputs/derived/review-hits-<source>.csv` | The records each source returned, without abstracts |
| `02.inputs/derived/review-records.csv` | The screening table, one row per unique record |
| `02.inputs/review/raw/review-abstracts.csv` | Abstracts, kept out of git |

The review code stays out of the manuscript, because the article reports nothing from it.

## Deviations

None yet.

## References

Arksey, H. and O'Malley, L. (2005) Scoping studies, towards a methodological framework. International Journal of Social Research Methodology 8(1), 19 to 32. https://doi.org/10.1080/1364557032000119616

Levac, D., Colquhoun, H. and O'Brien, K.K. (2010) Scoping studies, advancing the methodology. Implementation Science 5, 69. https://doi.org/10.1186/1748-5908-5-69

Peters, M.D. et al. (2020) Updated methodological guidance for the conduct of scoping reviews. JBI Evidence Synthesis 18(10), 2119 to 2126. https://doi.org/10.11124/JBIES-20-00167

Sloan, S. and Pelletier, J. (2012) How accurately may we project tropical forest-cover change? A validation of a forward-looking baseline for REDD. Global Environmental Change 22(2), 440 to 453. https://doi.org/10.1016/j.gloenvcha.2012.02.001

Tricco, A.C. et al. (2018) PRISMA Extension for Scoping Reviews (PRISMA-ScR), checklist and explanation. Annals of Internal Medicine 169(7), 467 to 473. https://doi.org/10.7326/M18-0850

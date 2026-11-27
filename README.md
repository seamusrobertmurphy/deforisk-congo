# Testing deforestation risk variables in rural demography, distance to local market, regional haulage constraints and travel time estimates, compared against forest edge effects across Mai Ndombe district, Democratic Republic of the Congo



## Abstract

The deforestation risk models of the Democratic Republic of the Congo measured access to markets as travel time to towns of 50,000 or more people. Little was known about whether those settings matched how far rural people travelled for wood, fields and trade. No study read had entered wood demand into a risk model. This study reviewed the distance and population settings of 89 published forest loss and pressure models, holding 376 variables, and 747 field measurements from 86 African studies. A second review screened 1,075 records on fuelwood, charcoal and timber supply and read 38 full texts. Of 44 models that measured access to markets, 11 stated the size of the town, 8 of them 50,000 or more people, and 9 capped travel time or distance. Only one study, of the villages supplying Bamako, fitted how wood flows to a town fell with travel time. In the field, households walked a median of 3 km to collect wood and farmed a median of 3 km from home. In the North Batéké chiefdom of Mai Ndombe, fields were normally absent beyond 8 km of a village. Of the charcoal producers surveyed in Mai Ndombe, 60% made charcoal from trees felled to open fields, and the province supplied 16.9% of Kinshasa's charcoal. A market access layer was therefore built at 1 km, treating every settlement of the High Resolution Settlement Layer as a market, whatever its size. Roads from four sources were merged, and each settlement was weighted by its population to the power 0.55 and its travel time to the power -1.25, as fitted for Bamako. The layer was built to predict the forest loss of 2016 to 2021 and to be tested against distance to the forest edge over 2021 to 2026. Risk models should therefore measure access to village markets as well as to large towns, because wood cutting and farming lay within a few kilometres of home.


*Table 1 Pressures entered in the model, with the effect on forest clearing that the literature expected of a higher value of each.*

df1 <- tibble::tribble(
  ~Pressure, ~`Expected effect`, ~Reasoning,
  "Population density", "Mixed", "Small-scale clearing doubled with population growth across the basin from 2000 to 2014 (Tyukavina et al., 2018). In a national model for 2000 to 2005, population distribution did not predict where forest changed (Kibambe Lubamba, 2013).",
  "Travel time to Kinshasa and the river landings, by road and river", "Lowers", "Across eight Congo Basin countries, from 2000 to 2012, forest clearing fell by 0.63% with each 1% rise in travel time to the nearest market centre (Wheeler & Damania, 2015).",
  "Distance to the forest edge", "Lowers", "In the Democratic Republic of the Congo, 81.53% of the forest cover changes of 2000 to 2005 lay less than 1 km from existing secondary forest (Kibambe Lubamba, 2013).",
  "Distance to new forest roads", "Mixed", "Each kilometre of first-cut road in the basin was followed by 186 ha of forest loss and degradation (Engert, Souza, Kleinschroth, Bignoli, et al., 2025). Engert, Souza, Kleinschroth, Bignoli, et al. (2025) wrote that industrial selective logging there could “degrade forests but lead to little outright deforestation”.",
  "Distance to settlements and camps", "Lowers", "About 80% of the deforestation of 2015 to 2020 in the six countries lay within 3 km of the nearest road or settlement (A. Shapiro et al., 2023).",
  "Territory’s share of Kinshasa’s charcoal", "Mixed", "In Mai Ndombe in 2021, 60% of producers made charcoal from trees felled to open fields (Dubiez et al., 2021). A review found “a mismatch” between wood energy use and forest degradation (Besisa Nguba et al., 2025).",
  "Household wealth and cooking fuel", "Mixed", "Ngouhouo-Poufoun et al. (2024) found, among 1,035 households of the Tridom landscape shared by three countries, that “a marginally higher income from cocoa production-based livelihood portfolios is associated with six to seven times higher deforestation”. In two pilot sites of Equateur province, Samndong et al. (2018) found that “shifting cultivation is driven by the poverty conditions of the study area”. Behrendt et al. (2013) judged that charcoal supply “could represent the single biggest threat to Congo Basin forests in the coming decades”."
)

ft1 <- flextable(df1) %>%
  set_caption("Table 1 Pressures entered in the model, with the effect on forest clearing that the literature expected of a higher value of each.") %>%
  align(align = "left", part = "all") %>%
  bold(part = "header") %>%
  autofit()

# Note: Because Table 1 has very long paragraphs in the 'Reasoning' column, 
# autofit() alone will make it wider than a standard page. 
# Uncomment the line below to constrain it to a 6.5-inch page width while wrapping text:
# ft1 <- ft1 %>% width(j = c(1, 2, 3), width = c(1.5, 1.0, 4.0))

ft1

*Table 2 Distance and population variables in 89 published risk models. Cap, a limit on travel time or distance. Decay, the form in which an effect fell with distance.*

df2 <- tibble::tribble(
  ~Variable, ~Studies, ~`Stated a town size`, ~`Stated a cap`, ~`Stated a decay`,
  "Distance to road", 54, 0, 11, 21,
  "Distance to river", 29, 2, 0, 10,
  "Population density", 26, 1, 3, 6,
  "Distance to settlement", 26, 2, 0, 9,
  "Distance to town", 24, 0, 4, 5,
  "Travel time", 18, 8, 5, 4,
  "Distance to forest edge", 14, 2, 4, 4,
  "Population count", 9, 0, 1, 4,
  "Distance to market", 5, 1, 0, 2,
  "Market potential", 5, 3, 0, 4
)

ft2 <- flextable(df2) %>%
  set_caption("Table 2 Distance and population variables in 89 published risk models. Cap, a limit on travel time or distance. Decay, the form in which an effect fell with distance.") %>%
  align(j = 1, align = "left", part = "all") %>%
  align(j = 2:5, align = "right", part = "all") %>%
  bold(part = "header") %>%
  autofit()

ft2

*Table 3 Distances travelled for wood, fields and trade in 86 African field studies. Values, measurements read from the studies.*

df3 <- tibble::tribble(
  ~Measure, ~Values, ~Studies, ~Range, ~Median,
  "Walk to collect wood, km", 16, 6, "1 to 5", "3",
  "Time per wood collection trip, h", 6, 2, "1.7 to 6", "3.5",
  "Home to field, km", 9, 4, "0.5 to 10", "3",
  "Daily carrying distance per adult, km", 6, 1, "1 to 7", "3.4",
  "Village to market, km", 6, 3, "10 to 400", "25",
  "Village to hunting ground, km", 12, 6, "2 to 60", "17.5",
  "Wood supply distance, Kinshasa, km", 23, 7, "50 to 1,000", "160",
  "Wood supply distance, cities of 1 to 5 million, km", 53, 9, "4.5 to 550", "60",
  "Wood supply distance, towns under 1 million, km", 9, 5, "5 to 500", "40",
  "Rural wood use, kg per person per day", 8, 5, "0.4 to 2.0", "1.4"
)

ft3 <- flextable(df3) %>%
  set_caption("Table 3 Distances travelled for wood, fields and trade in 86 African field studies. Values, measurements read from the studies.") %>%
  align(j = 1, align = "left", part = "all") %>%
  align(j = 2:5, align = "right", part = "all") %>%
  bold(part = "header") %>%
  autofit()

ft3


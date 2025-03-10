Fantasy-Premier-League
======================

A FPL library that gets all the basic stats for each player, gw-specific data for each player and season history of each player

## FAQ

### Data Structure

The data folder contains the data from past seasons as well as the current season. It is structured as follows:

+ season/cleaned_players.csv : The overview stats for the season
+ season/gws/gw_number.csv : GW-specific stats for the particular season
+ season/gws/merged_gws.csv : GW-by-GW stats for each player in a single file
+ season/players/player_name/gws.csv : GW-by-GW stats for that specific player
+ season/players/player_name/history.csv : Prior seasons history stats for that specific player.

### Player Position Data

In players_raw.csv, element_type is the field that corresponds to the position.
1 = GK
2 = DEF
3 = MID
4 = FWD

## Downloading Your Team Data

You can download the data for your team by executing the following steps:

```
python teams_scraper.py <team_id>
#Eg: python teams_scraper.py 4582
```

This will create a new folder called "team_<team_id>_data18-19" with individual files of all the important data

## Notable Usages of this Repository

+ [FPL.co.id Tailsman](http://fpl.co.id/tools/talismans/)

+ [Leicester City Brendan Rodgers Impact Analysis on twitter by @neilswmurrayFPL](https://twitter.com/neilswmurrayFPL/status/1147407501736009728)

+ [Stat Analysis on twitter by @StatOnScout](https://twitter.com/StatOnScout)

+ [Arsenal-Chelsea LinkedIn article by Velko Kamenov](https://www.linkedin.com/pulse/whoever-wins-2019-uefa-europe-league-final-still-ends-velko-kamenov/)

+ [Form vs Fixture Medium article by JinHyunCheong](https://towardsdatascience.com/mythbusting-fantasy-premier-league-form-over-fixtures-eecf9022e834)

+ [Visualization by u/dkattir](https://www.reddit.com/r/dataisbeautiful/comments/9zlx14/points_per_game_vs_predictability_after_12_weeks/)

+ [Visualization by u/Dray11](https://www.reddit.com/r/FantasyPL/comments/9bjwra/created_a_very_crude_and_basic_comparison_chart/)

+ [Visualization website by @antoniaelek](http://fantasy.elek.hr/)

+ [FPL Captain Classifier by Raghunandh GS](https://medium.com/datacomics/building-an-fpl-captain-classifier-cf4ee343ebcc)

+ [My Personal Blog](http://vaastavanand.com/blog/)

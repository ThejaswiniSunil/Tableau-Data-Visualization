# Citi Bike NYC Ridership During the 2020 Lockdown

![Dashboard walkthrough](Citi%20Bike%20NYC-Summary%20Report.gif)

**Interactive Tableau story:** [Citi Bike Ridership During the 2020 Lockdown](https://public.tableau.com/views/CitiBikeRidershipDuringthe2020Lockdown_/Story1)

**Data source:** [Citi Bike System Data](https://www.citibikenyc.com/system-data)

## Objective
Analyse about 7.5M Citi Bike trips from January to June 2020 to see how the
spring 2020 lockdown changed ridership, and how members and casual riders
behaved differently.

## Research questions
- How did monthly trips change, and did members and casual riders differ?
- How did hourly riding patterns change between February and April?
- Which start stations were busiest?
- How did the mix of classic and electric bikes change?

## ETL
- Downloaded the 2020 Citi Bike trip data (`get_data.py`).
- The current files are split into parts per month, so `merge_parts.py`
  merges them into one file per month.
- Combined January to June in the Jupyter notebook, kept only rides that
  started in 2020, and exported one clean CSV.
- Loaded the CSV into Tableau Public and built a five-page story.

## Key findings
- 7,528,391 trips in total; the median trip lasted 13 minutes.
- Member trips fell 43.5% from March to April (916,581 to 518,018);
  casual trips rose 7.6% (154,815 to 166,521).
- Members' 8 AM peak fell about 81% (97,191 trips in February to 18,866 in
  April); the 5 PM peak fell about 46% (103,739 to 55,646).
- Casual riders peaked at 5 PM overall and 4 PM in April, and grew from about
  8% of trips in January to about 30% in June.
- The busiest start station was West St & Chambers St (39,191 trips); the
  ten busiest are all in Manhattan.
- Electric bikes stayed a small share of trips: 2.5% in February, peaking at
  8.8% in April, and 5.3% in June.

These patterns are consistent with fewer commuting trips during the lockdown,
but the data alone cannot show the cause.

## How to run
1. `pip install -r requirements.txt`
2. `python get_data.py`
3. `python merge_parts.py`
4. Run the notebook to create `data/six-month-2020-citibike-tripdata.csv`
5. Open the CSV in Tableau Public Desktop

## Limitations
- The current Citi Bike files have no gender, age or trip-duration fields,
  so those analyses cannot be done with this data.
- Station rankings cover only rides with a recorded start station.
- The analysis shows patterns, not causes.


import pandas as pd
import datetime as datetime

# expects date in the dataframe
def add_dimension_date(df):
    # day of the week
    df['day_of_week'] = df.date
    df['day_of_week'] = df['day_of_week'].apply(lambda x: x.strftime("%A"))

    df['day_of_week_abrev'] = df.date
    df['day_of_week_abrev'] = df['day_of_week_abrev'].apply(lambda x: x.strftime("%a"))

    # Week Start
    def firstDayOfWeek(dt):
        from datetime import datetime, timedelta
        start = dt - timedelta(days = dt.weekday())
        end = start + timedelta(days = 6)
        return start.date()

    df['week_start'] = df.date
    df['week_start'] = df['week_start'].apply(lambda x: firstDayOfWeek(x))

    # month_year
    df['week_of_year'] = df.date
    df['week_of_year'] = df['week_of_year'].apply(lambda x: x.strftime("%W"))


    # month_year
    df['year_month'] = df.date
    df['year_month'] = df['year_month'].apply(lambda x: x.strftime("%y-%m"))

    # What month
    df['month'] = df.date
    df['month'] = df['month'].apply(lambda x: x.strftime("%m"))

    # days ago
    df['days_ago'] = df.date
    df['days_ago'] = df['days_ago'].apply(lambda x: (datetime.datetime.today() - x).days )

    return df

if __name__ == "__main__":
    #pd.date_range(weight_raw['date'].iget(0), datetime.datetime.today())
    print "Add test"

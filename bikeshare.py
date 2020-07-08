import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and a day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, Washington?').lower()
    if city in ['chicago', 'washington', 'new york city']:
        print("Thank You")
    else :
     print('Oops, that is not one of the cities. Try again')
     city = input('Would you like to see data for Chicago, New York City, Washington?')
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('What month would you like to see? January, February, March, April, May or June?').lower()
    print (month)
    if month in ['january', 'february', 'march', 'april', 'may', 'june']:
        print ('Thank You')
    else:
        print('Oops, that is not one of the choices. Try again')
        month = input('What month would you like to see? January, February, March, April, May or June?').lower()
        
    day = input('What day of the week? Enter Monday,..., Sunday.').title()
    print (day)
    if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'all']:
        print("Thank You")
    else:
        print('Oops, that is not between 1 and 7. Try again')
        day = input('What day of the week? Enter Monday,..., Sunday.').title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    print('-'*40)
    return city, month, day
  
   

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #print(df)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    #popular_hour =  df['hour'].mode()[0]
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
 

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df
   
def time_stats(df):
    #Displays statistics on the most frequent times of travel.

# display total travel time
     total_travel_time = df['Trip Duration'].sum()
     count_days = total_travel_time // 86400
     count_hours = (total_travel_time % 86400) // 3600
     count_minutes = (total_travel_time % 3600) // 60
     count_seconds = total_travel_time % 60
     print('The total travel time is {} days {} hours {} minutes {} seconds.\n'.format(count_days, count_hours,
                                                                                      count_minutes, count_seconds))

    # display mean travel time
     mean_travel_time = df['Trip Duration'].mean()
     count_minutes = (mean_travel_time) // 60
     count_seconds = mean_travel_time % 60
     print('The mean travel time is {} minutes {} seconds.\n'.format(count_minutes, count_seconds))

    #A lot of the following calculations I was able to find through research on Github and Google."""


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common start station is: {} ".format(
        df['Start Station'].mode().values[0])
    )

    # TO DO: display most commonly used end station
    print("The most common end station is: {}".format(
        df['End Station'].mode().values[0])
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['routes'] = df['Start Station']+ " " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['routes'].mode().values[0])
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    df['duration'] = df['End Time'] - df['Start Time']
    
    # TO DO: display total travel time
    print("The total travel time is: {}".format(
        str(df['duration'].sum()))
    )

    # TO DO: display mean travel time
    print("The mean travel time is: {}".format(
        str(df['duration'].mean()))
    )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of gender
    try:
        print("Here are the counts of various user types:")
        print(df['User Type'].value_counts())
    except KeyError:
        print('There is no available Gender data for washington')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest birth year is: {}".format(
                str(int(df['Birth Year'].min())))
            )
        print("The latest birth year is: {}".format(
                str(int(df['Birth Year'].max())))
            )
        print("The most common birth year is: {}".format(
                str(int(df['Birth Year'].mode().values[0])))
            )
    except KeyError:
        print("There is no available Birth Year data for Washington")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

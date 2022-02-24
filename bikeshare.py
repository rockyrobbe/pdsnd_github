import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday', 'all' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('For which city do you want to explore the bikeshare data: Chicago, New York or Washington? \n> ').lower()
       print(city, '\n')
       if city not in CITIES:
           print("Sorry that entry is not valid, please retry.")
           continue
       else:
           break

    # get user input for month (all, january, february, ... , june)
    while True:
       month = input('Interesting city you have selected! Do you want to explore a specific month or all months? '\
                    '[Either choose \'all\' to apply no month filter or choose a specific month \n(e.g. january, february, march, april, may, june)] \n> ').lower()
       print(month, '\n')
       if month not in MONTHS:
           print("Sorry that is not a valid month entry, please retry and double-check on typo\'s.")
           continue
       else:
           break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
         day = input('Are you interested to analyze bikeshare data for a certain weekday or do you want to consider all weekdays?'\
                   ' You can type \'all\' again to apply no day filter or choose from following days. \n(e.g. monday, tuesday, wednesday, thursday, friday, saturday or sunday) \n> ').lower()
         print(day, '\n')
         if day not in DAYS:
             print("Sorry that is not a valid entry, please re-enter your selection correctly.")
             continue
         else:
             break

    print('-'*80)

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
       # use the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1

       # filter by month to create the new dataframe
       df = df[df['month' ] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day' ] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    # returns a month number
    most_common_month = df['month'].mode()[0]
    print("The most common month is:", most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day'].mode()[0]
    print("The most common day of week is:", most_common_day_of_week)

    # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("The most common start hour is:", most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_combination = (df['Start Station']+ ' and ' +df['End Station']).mode()[0]
    print("The most common combination of start and end station is: ", most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel time in seconds: ", total_travel, " (This is ", int(total_travel/60/60/24), " whole days)")

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time in seconds: ", mean_travel, " (This is ", int(mean_travel/60), "whole minutes)")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    # check if gender is recorded in dataset (excluded for Washington)
    if 'Gender' in df:
        gender_types = df['Gender'].value_counts()
        print("\n",gender_types)

    # Display earliest, most recent, and most common year of birth
    # check if birth year is recorded in dataset (excluded for Washington)
    if 'Birth Year' in df:
        # find the earliest birth year
        earliest_year = min(df['Birth Year'])
        print("\nEarliest Birth Year: ", int(earliest_year))
        # find the most recent birth year
        recent_year = max(df['Birth Year'])
        print("Recent Birth Year: ", int(recent_year))
        # find the most common birth year
        common_birth_year = df['Birth Year'].mode()[0]
        print("Most Common Birth Year: ", int(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

def display_data(df):
    """Displays bikeshare data details."""

    print('\nDisplaying the first 10 rows of bikeshare data...\n')
    start_time = time.time()

    print(df.head(n=10))  # start by viewing the first ten rows of the dataset!
    print('\nAnd displaying the last 10 rows of bikeshare data...\n')
    print(df.tail(n=10))  # start by viewing the last ten rows of the dataset!

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)

    i = 20
    raw = input("\nWould you like to see the next 20 rows of bikeshare data; type 'yes' or 'no'?\n").lower()
    while True:
        if raw == 'no':
            break
        print('\nAnd displaying the next 20 rows of bikeshare data...\n')
        print(df[i:i+20])
        raw = input('\nWould you like to see next 20 rows of bikeshare data?\n').lower()
        i += 20

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        print('\nThank you for using this bikeshare progam. Thanks to Udacity for learning Python...\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

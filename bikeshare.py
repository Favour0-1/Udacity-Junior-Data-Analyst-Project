import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    valid_cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input('Please insert a city you want to work with\n ').lower()
        if city in valid_cities:
            break
        else:
            print('You inserted an invalid city\please in the valid city\n')

    # get user input for month (all, january, february, ... , june)
    month_choice = input('Would you like to work with all months or a specific month?\nEnter yes for all and no for a specific month\n').lower()
    if month_choice == 'yes':
        month = 'all'
    else:
        valid_month = ['january', 'february', 'march', 'april', 'may', 'june']
        while True:
            month = input('please insert the month you want to work with\n').lower()
            if month in valid_month:
                break
            else:
                print('you inserted an invalid month\nplease type in the valid month\n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_choice = input('would you like to work with all days or a specific day?\nEnter yes for all and no for a specific day\n').lower()
    if day_choice == 'yes':
        day = 'all'
    else:
        day_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        while True:
            day = input('please insert the day you want to work with\n').lower()
            if day in day_of_week:
                break
            else:
                print('you inserted an invalid day\nplease type in the valid day\n')


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

   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    highest_month = df['month'].mode()[0]
    print(highest_month)

    # display the most common day of week
    highest_day = df['day'].mode()[0]
    print(highest_day)

    # display the most common start hour
    highest_hour = df['hour'].mode()[0]
    print(highest_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(common_start_station)


    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(common_start_station)


    # display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    df['combination']
    common_combination = df['combination'].mode()[0]
    print(common_combination)
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(total_travel_time)


    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print(average_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        user_types_count = df['User Type'].value_counts()
        print(user_types_count)
    else:
        print('There is no data for user types')


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    else:
        print('There is no data for gender')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        print(earliest_year)
        recent_year = df['Birth Year'].max()
        print(recent_year)
        common_year = df['Birth Year'].mode()[0]
        print(common_year)
    else:
        print('There is no data for birth year')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def display_data(df):
    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?\n').lower()
    start_loc = 0
    while True:
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input('Do you wish to continue?:\n').lower()
        if view_display == 'no':
            break
            
        display_data(df)
        
        
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
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    

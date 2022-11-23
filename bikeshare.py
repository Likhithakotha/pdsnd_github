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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("Please enter valid city\n")
            

    # TO DO: get user input for month (all, january, february, ... , june)
    
    months=['january', 'february', 'march', 'april', 'may', 'june','all']
    while True:
        month=input("Which month - January, February, March, April, May, June or all?\n").title()
        if month.lower() in months:
            break
        else:
            print("Please enter valid month\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
    while True:
        day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n").title()
        if day.lower() in days:
            break
        else:
            print("Please enter valid day of the week\n")


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
    
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'All':
        months=['January', 'February', 'March', 'April', 'May', 'June']
        month=months.index(month)+1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month: ",df['Start Time'].dt.month.mode()[0])

    # TO DO: display the most common day of week
    print("Most common day of week: ",df['Start Time'].dt.weekday_name.mode()[0])
    
    # TO DO: display the most common start hour
    print("Most common start hour: ",df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Commonly used start station: ", df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("Commonly used end station: ",df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    start_end_combined=("("+df['Start Station']+", "+df['End Station']+")").mode()[0]
    print("Most frequent combination of start station and end station trip: \n",start_end_combined)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time: ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean Travel Time: ",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Count of user types:\n",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("Count of gender:\n",df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print("Earliest Birth year: ",df['Birth Year'].min())
        print("Most Recent Birth year: ",df['Birth Year'].max())
        print("Most Common Birth year: ",df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    print("Welcome to Bikeshare System")	
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        count=0
        while True:
            
            data=input('would you like to view individual trip data? Type \'yes\' or \'no\'.\n')
            if data=='yes':
                datadict=df[count:count+5].rename(columns={'Unnamed: 0':''}).to_dict(orient='records')
                for d in datadict:
                    print('\n{')
                    for key,value in d.items():
                        print('{} : {}'.format(key,value))
                    print('}\n')
                count+=5
            else:
                break
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

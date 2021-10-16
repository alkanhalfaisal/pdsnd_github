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
    city =''
    ###
    countc =0
    #countc ==> count city
    while city not in ('chicago', 'new york city', 'washington'):
        while city not in('chicago', 'new york city', 'washington'):
            if countc != 0:
                print('invalid input please enter name city correct again')
            city = input('Would you like to see data for Chicago, New york city, or Washington? ')
            city = city.lower()
            countc+=1
        

    # TO DO: get user input for month (all, january, february, ... , june)
        countm=0
            #countc ==> count month
        month =''
        while month not in ('january', 'february', 'march','april','may','june','july','august','september','October','november','december','all'):
            if countm!=0:
                print('invalid input please enter name of the month correct again')
            month =input('Which month would you like to filter? ex: january, february, ...  ')
            month = month.lower()
            countm+=1
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        countd=0
            #countc ==> count day
        day = ''
        while day not in ('sunday', 'monday', 'tuesday','wednesday','thursday','friday','saturday','all'):
            if countd!=0:
                print('invalid input please enter name of the day correct again')
            day = input('Which day would you like to filter? ex: monday, tuesday, ... ')
            day = day.lower()
            countd+=1

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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
       
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

       
        df = df[df['month'] == month]

   
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    #mcm => most common month
    mcm = df['month'].mode()[0]
    print('The most common month is {}'.format(mcm))

    # TO DO: display the most common day of week
    mcd = df['day_of_week'].mode()[0]
    print('The most common day is {}'.format(mcd))
    # TO DO: display the most common start hour
    mcs=df['Start Time'].dt.hour.mode()[0]
    print('The most common start hour is {}'.format(mcs))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mcus=df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(mcus))
    
    # TO DO: display most commonly used end station
    mcues=df['End Station'].mode()[0]
    print('The most commonly used end Station is {}'.format(mcues))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station']+df['End Station']
    
    most_combination = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is {}'.format(most_combination))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('total travel time {}'.format(total_travel))

    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('mean travel time {}'.format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth

        df['Birth Year'] = pd.to_datetime(df['Birth Year'])
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
    #mcyofb =>>> most common year of birth
        mcyofb = df['Birth Year'].mode()[0]
        print('\nEarliest: {} most_recent {} most common year of birth {}'.format(earliest,most_recent,mcyofb))
    except:
        print('There is no Gender and Birth Year for washington')

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
        row = 0
        while True:
            
            viewData = input("Would you like to see the raw data? Type 'Yes' or 'No'.")
            if viewData.lower() == "yes":
                
                for i in range(5):
                    if df.size+5<=row:
                        break
                    print(df.iloc[row])
                    
                    row += 1
            else:
                restart = input('\nWould you like to restart? Enter yes or no.\n')
                if restart.lower() != 'yes':
                    break


if __name__ == "__main__":
	main()

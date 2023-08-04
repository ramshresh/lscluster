from datetime import datetime
import calendar

epochCategories = {
    'PreMonsoon': [1, 2, 3, 4, 5],
    'Monsoon': [6, 7, 8, 9],
    'PostMonsoon': [10, 11, 12],
    'PreGorkha':[1,2,3],
    'CoSeismic':[4,5],
}

epochCategoriesMidDate = {
    'PreMonsoon': {'month':3,'day':15},
    'Monsoon': {'month':7,'day':31},
    'PostMonsoon': {'month':11,'day':15},
    'PreGorkha':{'month':2,'day':15},
    'CoSeismic':{'month':4,'day':15},
}

epoc_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
epoch_names = [
    '01_PreMonsoon2014','02_PostMonsoon2014',
    '03_PreGorkha2015','04_Coseismic2015','05_PostMonsoon2015',
    '06_PreMonsoon2016','07_PostMonsoon2016',
    '08_PreMonsoon2017','09_PostMonsoon2017',
    '10_PreMonsoon2018','11_PostMonsoon2018',
    '12_PreMonsoon2019','13_PostMonsoon2019',
    '14_PostMonsoon2020']

epoch_duration = {
    "01_PreMonsoon2014": {
        'from': datetime.strptime('2014-01-01', "%Y-%m-%d"),
        'to': datetime.strptime('2014-05-31', "%Y-%m-%d"),
    },
    "02_PostMonsoon2014": {
        'from': datetime.strptime('2014-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2014-12-31', "%Y-%m-%d"),
    },
    "03_PreGorkha2015": {
        'from': datetime.strptime('2015-01-01', "%Y-%m-%d"),
        'to': datetime.strptime('2015-04-25', "%Y-%m-%d"),
    },
    "04_Coseismic2015": {
        'from': datetime.strptime('2015-04-25', "%Y-%m-%d"),
        'to': datetime.strptime('2015-05-31', "%Y-%m-%d"),
    },
    "05_PostMonsoon2015": {
        'from': datetime.strptime('2015-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2015-12-31', "%Y-%m-%d"),
    },
    "06_PreMonsoon2016": {
         'from': datetime.strptime('2016-01-01', "%Y-%m-%d"),
        'to': datetime.strptime('2016-05-31', "%Y-%m-%d"),
    },
    "07_PostMonsoon2016": {
        'from': datetime.strptime('2016-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2016-12-31', "%Y-%m-%d"),
    },
    "08_PreMonsoon2017": {
        'from': datetime.strptime('2017-01-01', "%Y-%m-%d"),
        'to': datetime.strptime('2017-05-31', "%Y-%m-%d"),
    },
    "09_PostMonsoon2017": {
        'from': datetime.strptime('2017-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2017-12-31', "%Y-%m-%d"),
    },
    "10_PreMonsoon2018": {
        'from': datetime.strptime('2018-01-01', "%Y-%m-%d"),
        'to': datetime.strptime('2018-05-31', "%Y-%m-%d"),
    },
    "11_PostMonsoon2018": {
        'from': datetime.strptime('2018-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2018-12-31', "%Y-%m-%d"),
    },
    "12_PreMonsoon2019": {
        'from': datetime.strptime('2019-01-01', "%Y-%m-%d"),
        'to': datetime.strptime('2019-05-31', "%Y-%m-%d"),
    },
    "13_PostMonsoon2019": {
        'from': datetime.strptime('2019-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2019-12-31', "%Y-%m-%d"),
    },
    "14_PostMonsoon2020": {
        'from': datetime.strptime('2020-10-01', "%Y-%m-%d"),
        'to': datetime.strptime('2020-12-31', "%Y-%m-%d"),
    },
}

def get_epoch_name_of_epoch_number(epoch_number):
    return epoch_names[epoc_numbers.index(epoch_number)]

def get_epoch_duration_of_epoch_number(epoch_number):
    epoch_name = get_epoch_name_of_epoch_number(epoch_number)
    return epoch_duration[epoch_name]

def get_epoch_duration_of_epoch_name(epoch_name):
    return epoch_duration[epoch_name]

def get_mid_date_of_epoch(epoch_number):
    
    d = get_epoch_duration_of_epoch_number(epoch_number)
    
    md = d['from'].date() + (d['to']-d['from']) / 2 
    return md

def get_to_date_of_epoch(epoch_number):
    
    d = get_epoch_duration_of_epoch_number(epoch_number)
    
    return d['to'].date() 

def get_dates_of_epoch(epoch_number):
    
    d = get_epoch_duration_of_epoch_number(epoch_number)
    
    return d['from'].date(),  d['from'].date() + (d['to']-d['from']) / 2 , d['to'].date() 


def get_month_code(n):
    codes = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    if n < 0 or n > 12:
        raise Exception('Month number out of range. Required value (1,12)')
    i = n - 1
    return codes[i]



def get_month_code(n):
    codes = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec' ]
    if n < 0 or n > 12:
        raise Exception('Month number out of range. Required value (1,12)')
    i = n - 1
    return codes[i]

def get_mid_date(year, month):
    # Calculate the number of days in the given month
    _, num_days = calendar.monthrange(year, month)
    
    # Calculate the mid-date (middle day) of the month
    mid_day = num_days // 2 + 1
    
    # Create a datetime object for the mid-date
    mid_date = datetime(year, month, mid_day)
    
    return mid_date

from datetime import datetime,timedelta

weekdays_dict={'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[]}

weakdays_list = ['Monday','Tuesday','Wednesday','Thursday','Friday']

current_datetime = datetime.now().date()
interval = current_datetime + timedelta(weeks=1)

def get_birthdays_per_week(users):
    for i in users:
        if i['birthday']>=current_datetime and i['birthday']<interval:
            weekdays_dict[get_day(i['birthday'])].append(i['name'])

    for i in weekdays_dict:
        print(f'{i}:',','.join(weekdays_dict[i]))

def get_day(date):
    if date.weekday()==5 or date.weekday()==6:
        return weakdays_list[0]
    else:
        return weakdays_list[date.weekday()]

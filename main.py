from datetime import datetime,timedelta

weekdays_dict={'Monday':[],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[]}

current_datetime = datetime.now().date()
interval = current_datetime + timedelta(weeks=1)

def get_birthdays_per_week(users):
    for user in users:
        user['birthday']=datetime(year=current_datetime.year,month=user['birthday'].month,day=user['birthday'].day).date()
        if user['birthday']>=current_datetime and user['birthday']<=interval:
            weekdays_dict[get_day(user['birthday'])].append(user['name'])

    for i in weekdays_dict:
        if weekdays_dict[i]:
            print(f'{i}:',','.join(weekdays_dict[i]))

def get_day(date):
    if date.weekday() in (5,6):
        return 'Monday'
    else:
        return date.strftime('%A')
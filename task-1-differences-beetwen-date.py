from datetime import datetime, timedelta

# this function is calculate differences
# between two date 
def  get_days_from_today(date):
    return datetime.today().date() - date.date()

from datetime import datetime, timedelta

# this function is calculate differences
# between two date 
def  get_days_from_today(date):
    
    try:
        datetime_date = datetime.strptime(date, "%Y-%m-%d")
        return (datetime.today().date() - datetime_date.date()).days
    
    except ValueError:
        print("Incorrect date")
        

from datetime import datetime
import locale

def get_datetime() -> str:
    user_lcale = locale.getlocale()
    
    try:
        locale.setlocale(locale.LC_TIME, user_lcale)
    except locale.Error:
        print(f'Locale {user_lcale} not found. Using default locale')
        locale.setlocale(locale.LC_TIME, 'c')
        
    today: datetime = datetime.now()
    
    return today.strftime('%c')


if __name__ == '__main__':
    print(get_datetime())
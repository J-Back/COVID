import datetime

def Time():
    return datetime.datetime.today().strftime('%Y-%m-%d')
    
if __name__ == '__main__':
    Time()
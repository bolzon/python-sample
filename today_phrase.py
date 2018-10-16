import datetime

def today_phrase(weekday):
    phrases = [
        'hello world',
        'today is a good day',
        "I'm not going out today",
        'hey you',
        'привет мир!',
        'здравствуйте товарищ',
        'всё хорошо, спасибо'
    ]
    return phrases[weekday]

weekday = datetime.date.today().weekday()
print(today_phrase(weekday))

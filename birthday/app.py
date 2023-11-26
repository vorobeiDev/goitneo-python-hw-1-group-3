import datetime
from collections import defaultdict

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_birthdays_per_week(users):
    today = datetime.date.today()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            weekday = birthday_this_year.weekday()
            if weekday in [5, 6]:
                weekday = 0

            weekday_name = WEEKDAYS[weekday]
            birthdays[weekday_name].append(name)

    for day in WEEKDAYS:
        if birthdays[day]:
            print(f"{day}: {', '.join((birthdays[day]))}")


if __name__ == "__main__":
    users = [
        {"name": "Taras Shevchenko", "birthday": datetime.datetime(1814, 3, 9)},
        {"name": "Lesia Ukrainka", "birthday": datetime.datetime(1871, 2, 25)},
        {"name": "Andrii Novak", "birthday": datetime.datetime(1993, 11, 30)}
    ]

    get_birthdays_per_week(users)

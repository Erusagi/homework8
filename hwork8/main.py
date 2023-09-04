from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    birthdays_per_week = {}
    today = date.today()
    for user in users:
        birthday = user["birthday"].replace(year = today.year)
        current_weekday = birthday.weekday()
        username = user["name"].split(" ")[0]
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today and (today-birthday_this_year).days < 359:
            continue

        if current_weekday == 5 or current_weekday == 6:
            if "Monday" in birthdays_per_week:
                birthdays_per_week["Monday"].append(username)
            else:
                birthdays_per_week["Monday"] = [username]
        else:
            if hasattr(birthdays_per_week, birthday.strftime("%A")):
                birthdays_per_week[birthday.strftime("%A")].append(username)
            else:
                birthdays_per_week[birthday.strftime("%A")] = [username]

    return birthdays_per_week


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 10, 5).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")

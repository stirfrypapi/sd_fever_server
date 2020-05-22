data = {
    "data": [
        {
            "Name": "Wheel of Fortune Tarot Match",
            "Date": "May 24, 2020",
            "Time": "2:30PM - 6:00PM"
        },
        {
            "Name": "A Dinner over HK Island",
            "Date": "May 26, 2020",
            "Time": "8:00PM - 10:30PM"
        },
        {
            "Name": "A Dinner over HK Island",
            "Date": "May 26, 2020",
            "Time": "8:00PM - 10:30PM"
        }
    ]
}

import json
if __name__ == "__main__":
    with open('event_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
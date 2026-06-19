#!/usr/bin/env python3
"""Generate data.json for the Olympic host-cities map (curated).

Summer and Winter Games host cities, chronological. Status is the season, which the
Periplum config maps to a ☀️ / ❄️ glyph. Edit the list and re-run when a new host is
awarded (at most once a year).

    python build.py > data.json
"""
import json
import sys

# (year, season, city, country, lat, lon, opening-date)
GAMES = [
    (1896, "Summer", "Athens", "Greece", 37.98, 23.73, "1896-04-06"),
    (1900, "Summer", "Paris", "France", 48.8566, 2.3522, "1900-05-14"),
    (1904, "Summer", "St. Louis", "United States", 38.63, -90.20, "1904-07-01"),
    (1908, "Summer", "London", "United Kingdom", 51.5074, -0.1278, "1908-04-27"),
    (1912, "Summer", "Stockholm", "Sweden", 59.33, 18.06, "1912-05-05"),
    (1920, "Summer", "Antwerp", "Belgium", 51.22, 4.40, "1920-04-20"),
    (1924, "Winter", "Chamonix", "France", 45.92, 6.87, "1924-01-25"),
    (1924, "Summer", "Paris", "France", 48.8566, 2.3522, "1924-05-04"),
    (1928, "Winter", "St. Moritz", "Switzerland", 46.50, 9.84, "1928-02-11"),
    (1928, "Summer", "Amsterdam", "Netherlands", 52.37, 4.90, "1928-05-17"),
    (1932, "Winter", "Lake Placid", "United States", 44.28, -73.98, "1932-02-04"),
    (1932, "Summer", "Los Angeles", "United States", 34.05, -118.24, "1932-07-30"),
    (1936, "Winter", "Garmisch-Partenkirchen", "Germany", 47.49, 11.10, "1936-02-06"),
    (1936, "Summer", "Berlin", "Germany", 52.52, 13.405, "1936-08-01"),
    (1948, "Winter", "St. Moritz", "Switzerland", 46.50, 9.84, "1948-01-30"),
    (1948, "Summer", "London", "United Kingdom", 51.5074, -0.1278, "1948-07-29"),
    (1952, "Winter", "Oslo", "Norway", 59.91, 10.75, "1952-02-14"),
    (1952, "Summer", "Helsinki", "Finland", 60.17, 24.94, "1952-07-19"),
    (1956, "Winter", "Cortina d'Ampezzo", "Italy", 46.54, 12.14, "1956-01-26"),
    (1956, "Summer", "Melbourne", "Australia", -37.81, 144.96, "1956-11-22"),
    (1960, "Winter", "Squaw Valley", "United States", 39.20, -120.24, "1960-02-18"),
    (1960, "Summer", "Rome", "Italy", 41.90, 12.50, "1960-08-25"),
    (1964, "Winter", "Innsbruck", "Austria", 47.27, 11.39, "1964-01-29"),
    (1964, "Summer", "Tokyo", "Japan", 35.68, 139.69, "1964-10-10"),
    (1968, "Winter", "Grenoble", "France", 45.19, 5.72, "1968-02-06"),
    (1968, "Summer", "Mexico City", "Mexico", 19.43, -99.13, "1968-10-12"),
    (1972, "Winter", "Sapporo", "Japan", 43.06, 141.35, "1972-02-03"),
    (1972, "Summer", "Munich", "West Germany", 48.14, 11.58, "1972-08-26"),
    (1976, "Winter", "Innsbruck", "Austria", 47.27, 11.39, "1976-02-04"),
    (1976, "Summer", "Montreal", "Canada", 45.50, -73.57, "1976-07-17"),
    (1980, "Winter", "Lake Placid", "United States", 44.28, -73.98, "1980-02-13"),
    (1980, "Summer", "Moscow", "Soviet Union", 55.76, 37.62, "1980-07-19"),
    (1984, "Winter", "Sarajevo", "Yugoslavia", 43.85, 18.36, "1984-02-08"),
    (1984, "Summer", "Los Angeles", "United States", 34.05, -118.24, "1984-07-28"),
    (1988, "Winter", "Calgary", "Canada", 51.05, -114.07, "1988-02-13"),
    (1988, "Summer", "Seoul", "South Korea", 37.57, 126.98, "1988-09-17"),
    (1992, "Winter", "Albertville", "France", 45.68, 6.39, "1992-02-08"),
    (1992, "Summer", "Barcelona", "Spain", 41.39, 2.17, "1992-07-25"),
    (1994, "Winter", "Lillehammer", "Norway", 61.12, 10.46, "1994-02-12"),
    (1996, "Summer", "Atlanta", "United States", 33.75, -84.39, "1996-07-19"),
    (1998, "Winter", "Nagano", "Japan", 36.65, 138.18, "1998-02-07"),
    (2000, "Summer", "Sydney", "Australia", -33.87, 151.21, "2000-09-15"),
    (2002, "Winter", "Salt Lake City", "United States", 40.76, -111.89, "2002-02-08"),
    (2004, "Summer", "Athens", "Greece", 37.98, 23.73, "2004-08-13"),
    (2006, "Winter", "Turin", "Italy", 45.07, 7.69, "2006-02-10"),
    (2008, "Summer", "Beijing", "China", 39.90, 116.40, "2008-08-08"),
    (2010, "Winter", "Vancouver", "Canada", 49.28, -123.12, "2010-02-12"),
    (2012, "Summer", "London", "United Kingdom", 51.5074, -0.1278, "2012-07-27"),
    (2014, "Winter", "Sochi", "Russia", 43.60, 39.73, "2014-02-07"),
    (2016, "Summer", "Rio de Janeiro", "Brazil", -22.91, -43.17, "2016-08-05"),
    (2018, "Winter", "Pyeongchang", "South Korea", 37.37, 128.39, "2018-02-09"),
    (2020, "Summer", "Tokyo", "Japan", 35.68, 139.69, "2021-07-23"),
    (2022, "Winter", "Beijing", "China", 39.90, 116.40, "2022-02-04"),
    (2024, "Summer", "Paris", "France", 48.8566, 2.3522, "2024-07-26"),
    (2026, "Winter", "Milan-Cortina", "Italy", 45.46, 9.19, "2026-02-06"),
    (2028, "Summer", "Los Angeles", "United States", 34.05, -118.24, "2028-07-14"),
    (2032, "Summer", "Brisbane", "Australia", -27.47, 153.03, "2032-07-23"),
]


def main():
    games = sorted(GAMES, key=lambda g: g[6])
    items = []
    for year, season, city, country, lat, lon, date in games:
        items.append({
            "name": f"{city} {year}", "date": date, "status": season,
            "placements": [{"map": "earth", "lat": lat, "lon": lon, "label": f"{city} {year}",
                            "popup": {"Games": f"{season} Olympics {year}", "Host": country}}],
        })
    json.dump({"items": items}, sys.stdout, indent=1, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()

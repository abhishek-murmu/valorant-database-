import mysql.connector
from datetime import timedelta


DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "1234",
    "database": "val_db",
    "port": "3306",
}


EVENT_DATA = [
    {
        "event_name": "Champions Tour 2023: LOCK//IN Sao Paulo",
        "event_prize": "$500,000 USD",
        "event_location": "Sao Paulo, Brazil",
        "event_dates": "Feb 13, 2023 - Mar 5, 2023",
        "matches": [
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-13", "22:40:00", "KOI", 0, "NRG", 2, "NRG", "0-2", "Completed", "Icebox, Haven"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-14", "01:35:00", "DetonatioN FocusMe", 0, "Giants Gaming", 2, "Giants Gaming", "0-2", "Completed", "Haven, Icebox"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-14", "22:40:00", "FunPlus Phoenix", 1, "Karmine Corp", 2, "Karmine Corp", "1-2", "Completed"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-15", "02:15:00", "BBL Esports", 1, "DRX", 2, "DRX", "1-2", "Completed"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-15", "05:35:00", "Cloud9", 2, "Paper Rex", 0, "Cloud9", "2-0", "Completed"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-15", "22:30:00", "Team Heretics", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-16", "01:05:00", "MIBR", 0, "TALON", 2, "TALON", "0-2", "Completed"),
            ("Bracket Stage", "Alpha - Round of 16", "2023-02-16", "03:50:00", "Gen.G", 0, "LOUD", 2, "LOUD", "0-2", "Completed"),
            ("Bracket Stage", "Alpha - Quarterfinals", "2023-02-17", "22:35:00", "NRG", 2, "Giants Gaming", 1, "NRG", "2-1", "Completed"),
            ("Bracket Stage", "Alpha - Quarterfinals", "2023-02-18", "02:05:00", "LOUD", 2, "Karmine Corp", 0, "LOUD", "2-0", "Completed"),
            ("Bracket Stage", "Alpha - Quarterfinals", "2023-02-18", "22:35:00", "DRX", 2, "Cloud9", 1, "DRX", "2-1", "Completed"),
            ("Bracket Stage", "Alpha - Quarterfinals", "2023-02-19", "01:30:00", "Evil Geniuses", 0, "TALON", 2, "TALON", "0-2", "Completed"),
            ("Bracket Stage", "Alpha - Semifinals", "2023-02-19", "22:35:00", "NRG", 1, "LOUD", 2, "LOUD", "1-2", "Completed"),
            ("Bracket Stage", "Alpha - Semifinals", "2023-02-20", "02:30:00", "DRX", 2, "TALON", 1, "DRX", "2-1", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-22", "22:30:00", "Team Liquid", 0, "Team Secret", 2, "Team Secret", "0-2", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-23", "01:00:00", "Natus Vincere", 2, "KRÜ Esports", 0, "Natus Vincere", "2-0", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-23", "03:30:00", "ZETA DIVISION", 0, "LEVIATÁN", 2, "LEVIATÁN", "0-2", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-23", "22:35:00", "Team Vitality", 2, "Global Esports", 1, "Team Vitality", "2-1", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-24", "01:40:00", "FUT Esports", 2, "Rex Regum Qeon", 0, "FUT Esports", "2-0", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-24", "04:00:00", "100 Thieves", 2, "EDward Gaming", 1, "100 Thieves", "2-1", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-24", "22:35:00", "Sentinels", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Bracket Stage", "Omega - Round of 16", "2023-02-25", "01:20:00", "T1", 0, "FURIA", 2, "FURIA", "0-2", "Completed"),
            ("Bracket Stage", "Omega - Quarterfinals", "2023-02-25", "22:30:00", "Team Secret", 0, "Natus Vincere", 2, "Natus Vincere", "0-2", "Completed"),
            ("Bracket Stage", "Omega - Quarterfinals", "2023-02-26", "01:00:00", "LEVIATÁN", 2, "Team Vitality", 0, "LEVIATÁN", "2-0", "Completed"),
            ("Bracket Stage", "Omega - Quarterfinals", "2023-02-26", "22:30:00", "FUT Esports", 1, "100 Thieves", 2, "100 Thieves", "1-2", "Completed"),
            ("Bracket Stage", "Omega - Quarterfinals", "2023-02-27", "02:05:00", "FNATIC", 2, "FURIA", 0, "FNATIC", "2-0", "Completed"),
            ("Bracket Stage", "Omega - Semifinals", "2023-02-27", "22:30:00", "Natus Vincere", 2, "LEVIATÁN", 0, "Natus Vincere", "2-0", "Completed"),
            ("Bracket Stage", "Omega - Semifinals", "2023-02-28", "00:55:00", "100 Thieves", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Playoffs", "Semifinals", "2023-03-02", "22:30:00", "LOUD", 3, "DRX", 2, "LOUD", "3-2", "Completed"),
            ("Playoffs", "Semifinals", "2023-03-03", "22:30:00", "Natus Vincere", 0, "FNATIC", 3, "FNATIC", "0-3", "Completed"),
            ("Showmatch", "Showmatch", "2023-03-04", "22:30:00", "Team tarik", 10, "Team FRTTT", 13, "Team FRTTT", "10-13", "Completed"),
            ("Playoffs", "Grand Final", "2023-03-05", "00:00:00", "LOUD", 2, "FNATIC", 3, "FNATIC", "2-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: Pacific League",
        "event_prize": "$250,000 USD",
        "event_location": "Seoul, South Korea",
        "event_dates": "Mar 25, 2023 - May 28, 2023",
        "matches": [
            ("League Play", "Week 1", "2023-03-25", "14:30:00", "ZETA DIVISION", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("League Play", "Week 1", "2023-03-25", "17:30:00", "T1", 2, "Global Esports", 1, "T1", "2-1", "Completed"),
            ("League Play", "Week 1", "2023-03-26", "14:30:00", "Paper Rex", 2, "DetonatioN FocusMe", 0, "Paper Rex", "2-0", "Completed"),
            ("League Play", "Week 1", "2023-03-26", "17:30:00", "Team Secret", 2, "TALON", 1, "Team Secret", "2-1", "Completed"),
            ("League Play", "Week 1", "2023-03-27", "14:30:00", "Rex Regum Qeon", 0, "Gen.G", 2, "Gen.G", "0-2", "Completed"),
            ("League Play", "Week 2", "2023-04-01", "14:30:00", "ZETA DIVISION", 2, "Rex Regum Qeon", 1, "ZETA DIVISION", "2-1", "Completed"),
            ("League Play", "Week 2", "2023-04-01", "18:00:00", "TALON", 0, "T1", 2, "T1", "0-2", "Completed"),
            ("League Play", "Week 2", "2023-04-02", "14:30:00", "Team Secret", 2, "Paper Rex", 1, "Team Secret", "2-1", "Completed"),
            ("League Play", "Week 2", "2023-04-02", "18:00:00", "Gen.G", 2, "DetonatioN FocusMe", 1, "Gen.G", "2-1", "Completed"),
            ("League Play", "Week 2", "2023-04-03", "14:30:00", "Global Esports", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("League Play", "Week 3", "2023-04-08", "14:30:00", "Rex Regum Qeon", 2, "DetonatioN FocusMe", 0, "Rex Regum Qeon", "2-0", "Completed"),
            ("League Play", "Week 3", "2023-04-08", "16:40:00", "T1", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("League Play", "Week 3", "2023-04-09", "14:30:00", "ZETA DIVISION", 2, "Global Esports", 1, "ZETA DIVISION", "2-1", "Completed"),
            ("League Play", "Week 3", "2023-04-09", "18:15:00", "TALON", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("League Play", "Week 3", "2023-04-10", "14:30:00", "Team Secret", 0, "Gen.G", 2, "Gen.G", "0-2", "Completed"),
            ("League Play", "Week 4", "2023-04-15", "14:30:00", "Paper Rex", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("League Play", "Week 4", "2023-04-15", "17:10:00", "Team Secret", 0, "Rex Regum Qeon", 2, "Rex Regum Qeon", "0-2", "Completed"),
            ("League Play", "Week 4", "2023-04-16", "14:30:00", "T1", 0, "Gen.G", 2, "Gen.G", "0-2", "Completed"),
            ("League Play", "Week 4", "2023-04-16", "16:45:00", "ZETA DIVISION", 2, "DetonatioN FocusMe", 0, "ZETA DIVISION", "2-0", "Completed"),
            ("League Play", "Week 4", "2023-04-17", "14:30:00", "TALON", 0, "Global Esports", 2, "Global Esports", "0-2", "Completed"),
            ("League Play", "Week 5", "2023-04-22", "13:30:00", "Paper Rex", 2, "Global Esports", 1, "Paper Rex", "2-1", "Completed"),
            ("League Play", "Week 5", "2023-04-22", "17:00:00", "Gen.G", 1, "DRX", 2, "DRX", "1-2", "Completed"),
            ("League Play", "Week 5", "2023-04-23", "13:30:00", "T1", 2, "Rex Regum Qeon", 0, "T1", "2-0", "Completed"),
            ("League Play", "Week 5", "2023-04-23", "15:50:00", "Team Secret", 2, "DetonatioN FocusMe", 0, "Team Secret", "2-0", "Completed"),
            ("League Play", "Week 5", "2023-04-24", "15:30:00", "ZETA DIVISION", 0, "TALON", 2, "TALON", "0-2", "Completed"),
            ("League Play", "Week 6", "2023-04-29", "13:30:00", "T1", 2, "DetonatioN FocusMe", 1, "T1", "2-1", "Completed"),
            ("League Play", "Week 6", "2023-04-29", "17:30:00", "ZETA DIVISION", 2, "Team Secret", 1, "ZETA DIVISION", "2-1", "Completed"),
            ("League Play", "Week 6", "2023-04-30", "13:30:00", "Global Esports", 2, "Gen.G", 0, "Global Esports", "2-0", "Completed"),
            ("League Play", "Week 6", "2023-04-30", "15:50:00", "Rex Regum Qeon", 1, "DRX", 2, "DRX", "1-2", "Completed"),
            ("League Play", "Week 6", "2023-05-01", "15:30:00", "TALON", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("League Play", "Week 7", "2023-05-06", "13:30:00", "TALON", 2, "Gen.G", 0, "TALON", "2-0", "Completed"),
            ("League Play", "Week 7", "2023-05-06", "16:00:00", "ZETA DIVISION", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("League Play", "Week 7", "2023-05-07", "13:30:00", "Rex Regum Qeon", 2, "Global Esports", 0, "Rex Regum Qeon", "2-0", "Completed"),
            ("League Play", "Week 7", "2023-05-07", "16:30:00", "Team Secret", 0, "T1", 2, "T1", "0-2", "Completed"),
            ("League Play", "Week 7", "2023-05-08", "15:30:00", "DRX", 2, "DetonatioN FocusMe", 0, "DRX", "2-0", "Completed"),
            ("League Play", "Week 8", "2023-05-12", "13:30:00", "Paper Rex", 2, "Gen.G", 0, "Paper Rex", "2-0", "Completed"),
            ("League Play", "Week 8", "2023-05-12", "17:15:00", "ZETA DIVISION", 1, "T1", 2, "T1", "1-2", "Completed"),
            ("League Play", "Week 8", "2023-05-13", "13:30:00", "Team Secret", 2, "DRX", 0, "Team Secret", "2-0", "Completed"),
            ("League Play", "Week 8", "2023-05-13", "16:00:00", "Global Esports", 2, "DetonatioN FocusMe", 0, "Global Esports", "2-0", "Completed"),
            ("League Play", "Week 8", "2023-05-14", "13:30:00", "TALON", 1, "Rex Regum Qeon", 2, "Rex Regum Qeon", "1-2", "Completed"),
            ("League Play", "Week 8", "2023-05-14", "16:30:00", "ZETA DIVISION", 2, "Gen.G", 1, "ZETA DIVISION", "2-1", "Completed"),
            ("League Play", "Week 8", "2023-05-15", "13:30:00", "T1", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("League Play", "Week 8", "2023-05-15", "16:30:00", "Team Secret", 2, "Global Esports", 0, "Team Secret", "2-0", "Completed"),
            ("League Play", "Week 8", "2023-05-16", "13:30:00", "TALON", 2, "DetonatioN FocusMe", 0, "TALON", "2-0", "Completed"),
            ("League Play", "Week 8", "2023-05-16", "16:00:00", "Rex Regum Qeon", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Playoffs", "Upper Round 1", "2023-05-19", "13:30:00", "ZETA DIVISION", 0, "Team Secret", 2, "Team Secret", "0-2", "Completed"),
            ("Playoffs", "Upper Round 1", "2023-05-19", "16:45:00", "T1", 2, "Gen.G", 1, "T1", "2-1", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-05-20", "13:30:00", "DRX", 2, "Team Secret", 1, "DRX", "2-1", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-05-20", "16:45:00", "Paper Rex", 2, "T1", 0, "Paper Rex", "2-0", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-05-21", "13:30:00", "Team Secret", 1, "Gen.G", 2, "Gen.G", "1-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-05-21", "17:15:00", "T1", 2, "ZETA DIVISION", 1, "T1", "2-1", "Completed"),
            ("Playoffs", "Upper Final", "2023-05-22", "13:30:00", "DRX", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-05-22", "16:00:00", "T1", 2, "Gen.G", 0, "T1", "2-0", "Completed"),
            ("Showmatch", "Showmatch", "2023-05-27", "11:00:00", "Team Bunny", 13, "Team SuperBusS", 6, "Team Bunny", "13-6", "Completed"),
            ("Playoffs", "Lower Final", "2023-05-27", "12:30:00", "DRX", 3, "T1", 2, "DRX", "3-2", "Completed"),
            ("Playoffs", "Grand Final", "2023-05-28", "12:30:00", "Paper Rex", 3, "DRX", 2, "Paper Rex", "3-2", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: EMEA League",
        "event_prize": "$250,000 USD",
        "event_location": "Berlin, Germany",
        "event_dates": "Mar 27, 2023 - May 28, 2023",
        "matches": [
            ("Regular Season", "Week 1", "2023-03-27", "22:00:00", "KOI", 2, "Natus Vincere", 0, "KOI", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2023-03-28", "01:00:00", "FNATIC", 2, "Giants Gaming", 0, "FNATIC", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2023-03-28", "21:30:00", "Team Heretics", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2023-03-29", "00:00:00", "Team Liquid", 1, "Team Vitality", 2, "Team Vitality", "1-2", "Completed"),
            ("Regular Season", "Week 1", "2023-03-29", "21:30:00", "Natus Vincere", 2, "Giants Gaming", 1, "Natus Vincere", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2023-03-30", "02:00:00", "Karmine Corp", 2, "BBL Esports", 0, "Karmine Corp", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2023-03-30", "21:30:00", "Team Liquid", 2, "FUT Esports", 1, "Team Liquid", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2023-03-31", "00:45:00", "KOI", 0, "Team Vitality", 2, "Team Vitality", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2023-03-31", "21:30:00", "FNATIC", 2, "BBL Esports", 1, "FNATIC", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2023-04-01", "01:15:00", "Team Heretics", 2, "Karmine Corp", 0, "Team Heretics", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2023-04-05", "23:30:00", "Team Vitality", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Regular Season", "Week 2", "2023-04-06", "21:30:00", "Natus Vincere", 2, "BBL Esports", 0, "Natus Vincere", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2023-04-07", "00:30:00", "FNATIC", 2, "Team Heretics", 0, "FNATIC", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2023-04-07", "21:30:00", "Team Liquid", 2, "Karmine Corp", 0, "Team Liquid", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2023-04-08", "00:00:00", "KOI", 0, "Giants Gaming", 2, "Giants Gaming", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2023-04-12", "23:30:00", "Natus Vincere", 2, "Team Heretics", 1, "Natus Vincere", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2023-04-13", "22:10:00", "KOI", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2023-04-14", "00:30:00", "Team Liquid", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2023-04-14", "22:30:00", "Giants Gaming", 2, "BBL Esports", 0, "Giants Gaming", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2023-04-15", "00:45:00", "Team Vitality", 2, "Karmine Corp", 0, "Team Vitality", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2023-04-19", "23:30:00", "Team Heretics", 0, "Team Liquid", 2, "Team Liquid", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-20", "21:30:00", "FUT Esports", 0, "Giants Gaming", 2, "Giants Gaming", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-21", "21:30:00", "Karmine Corp", 0, "Natus Vincere", 2, "Natus Vincere", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-22", "00:30:00", "BBL Esports", 2, "Team Vitality", 0, "BBL Esports", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2023-04-26", "23:30:00", "Giants Gaming", 1, "Team Liquid", 2, "Team Liquid", "1-2", "Completed"),
            ("Regular Season", "Week 5", "2023-04-27", "21:30:00", "BBL Esports", 2, "Team Heretics", 1, "BBL Esports", "2-1", "Completed"),
            ("Regular Season", "Week 5", "2023-04-28", "01:45:00", "KOI", 1, "Karmine Corp", 2, "Karmine Corp", "1-2", "Completed"),
            ("Regular Season", "Week 5", "2023-04-28", "21:30:00", "FUT Esports", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2023-04-28", "23:50:00", "Team Vitality", 0, "Natus Vincere", 2, "Natus Vincere", "0-2", "Completed"),
            ("Regular Season", "Week 6", "2023-05-03", "23:30:00", "Team Vitality", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Regular Season", "Week 6", "2023-05-04", "21:30:00", "FUT Esports", 2, "Karmine Corp", 0, "FUT Esports", "2-0", "Completed"),
            ("Regular Season", "Week 6", "2023-05-04", "23:45:00", "KOI", 1, "BBL Esports", 2, "BBL Esports", "1-2", "Completed"),
            ("Regular Season", "Week 6", "2023-05-05", "21:30:00", "Natus Vincere", 2, "Team Liquid", 0, "Natus Vincere", "2-0", "Completed"),
            ("Regular Season", "Week 6", "2023-05-06", "00:45:00", "Giants Gaming", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2023-05-10", "21:30:00", "KOI", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Regular Season", "Week 7", "2023-05-11", "00:40:00", "Giants Gaming", 2, "Team Vitality", 1, "Giants Gaming", "2-1", "Completed"),
            ("Regular Season", "Week 7", "2023-05-11", "21:30:00", "FUT Esports", 0, "Natus Vincere", 2, "Natus Vincere", "0-2", "Completed"),
            ("Regular Season", "Week 7", "2023-05-12", "00:50:00", "Karmine Corp", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Regular Season", "Week 7", "2023-05-12", "21:30:00", "BBL Esports", 1, "Team Liquid", 2, "Team Liquid", "1-2", "Completed"),
            ("Regular Season", "Week 7", "2023-05-13", "01:45:00", "KOI", 2, "Team Heretics", 1, "KOI", "2-1", "Completed"),
            ("Regular Season", "Week 8", "2023-05-17", "23:30:00", "FNATIC", 2, "Natus Vincere", 0, "FNATIC", "2-0", "Completed"),
            ("Regular Season", "Week 8", "2023-05-18", "21:05:00", "Team Heretics", 0, "Team Vitality", 2, "Team Vitality", "0-2", "Completed"),
            ("Regular Season", "Week 8", "2023-05-19", "00:05:00", "Karmine Corp", 0, "Giants Gaming", 2, "Giants Gaming", "0-2", "Completed"),
            ("Regular Season", "Week 8", "2023-05-19", "21:30:00", "KOI", 1, "Team Liquid", 2, "Team Liquid", "1-2", "Completed"),
            ("Regular Season", "Week 8", "2023-05-20", "02:05:00", "BBL Esports", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Playoffs", "Upper Round 1", "2023-05-23", "20:30:00", "Giants Gaming", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Playoffs", "Upper Round 1", "2023-05-23", "22:45:00", "Team Liquid", 2, "Team Vitality", 1, "Team Liquid", "2-1", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-05-24", "20:30:00", "FNATIC", 2, "FUT Esports", 1, "FNATIC", "2-1", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-05-25", "00:15:00", "Natus Vincere", 0, "Team Liquid", 2, "Team Liquid", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-05-25", "22:50:00", "FUT Esports", 2, "Team Vitality", 1, "FUT Esports", "2-1", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-05-26", "02:15:00", "Natus Vincere", 2, "Giants Gaming", 0, "Natus Vincere", "2-0", "Completed"),
            ("Playoffs", "Upper Final", "2023-05-26", "20:30:00", "FNATIC", 2, "Team Liquid", 0, "FNATIC", "2-0", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-05-26", "23:10:00", "Natus Vincere", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Playoffs", "Lower Final", "2023-05-27", "20:30:00", "Team Liquid", 3, "FUT Esports", 0, "Team Liquid", "3-0", "Completed"),
            ("Playoffs", "Grand Final", "2023-05-28", "20:30:00", "FNATIC", 1, "Team Liquid", 3, "Team Liquid", "1-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: Americas League",
        "event_prize": "$250,000 USD",
        "event_location": "Los Angeles, USA",
        "event_dates": "Apr 2, 2023 - May 28, 2023",
        "matches": [
            ("Regular Season", "Week 1", "2023-04-02", "00:30:00", "Sentinels", 2, "100 Thieves", 1, "Sentinels", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2023-04-02", "04:45:00", "KRÜ Esports", 0, "FURIA", 2, "FURIA", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2023-04-03", "00:30:00", "LOUD", 2, "MIBR", 1, "LOUD", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2023-04-03", "04:15:00", "Evil Geniuses", 0, "Cloud9", 2, "Cloud9", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2023-04-04", "00:30:00", "LEVIATÁN", 2, "NRG", 0, "LEVIATÁN", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2023-04-09", "00:30:00", "Cloud9", 1, "LOUD", 2, "LOUD", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2023-04-09", "04:05:00", "LEVIATÁN", 1, "FURIA", 2, "FURIA", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2023-04-10", "00:30:00", "NRG", 2, "Sentinels", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2023-04-10", "03:05:00", "MIBR", 2, "KRÜ Esports", 1, "MIBR", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2023-04-11", "00:30:00", "Evil Geniuses", 0, "100 Thieves", 2, "100 Thieves", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2023-04-16", "00:30:00", "Cloud9", 2, "100 Thieves", 0, "Cloud9", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2023-04-16", "03:30:00", "NRG", 1, "MIBR", 2, "MIBR", "1-2", "Completed"),
            ("Regular Season", "Week 3", "2023-04-17", "00:30:00", "LEVIATÁN", 2, "Sentinels", 1, "LEVIATÁN", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2023-04-17", "04:30:00", "Evil Geniuses", 2, "KRÜ Esports", 1, "Evil Geniuses", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2023-04-18", "00:30:00", "LOUD", 2, "FURIA", 0, "LOUD", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2023-04-22", "00:30:00", "LOUD", 2, "Sentinels", 1, "LOUD", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2023-04-22", "04:30:00", "LEVIATÁN", 2, "MIBR", 0, "LEVIATÁN", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2023-04-23", "00:30:00", "KRÜ Esports", 1, "100 Thieves", 2, "100 Thieves", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-23", "03:50:00", "Evil Geniuses", 1, "FURIA", 2, "FURIA", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-24", "00:30:00", "NRG", 1, "Cloud9", 2, "Cloud9", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-24", "04:35:00", "MIBR", 0, "Sentinels", 2, "Sentinels", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-25", "00:30:00", "LEVIATÁN", 1, "100 Thieves", 2, "100 Thieves", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-25", "04:30:00", "Evil Geniuses", 1, "LOUD", 2, "LOUD", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2023-04-26", "00:30:00", "Cloud9", 2, "FURIA", 0, "Cloud9", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2023-04-26", "03:00:00", "NRG", 2, "KRÜ Esports", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2023-04-30", "00:30:00", "NRG", 2, "100 Thieves", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2023-04-30", "02:50:00", "MIBR", 0, "FURIA", 2, "FURIA", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2023-05-01", "00:30:00", "Cloud9", 2, "Sentinels", 0, "Cloud9", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2023-05-01", "02:55:00", "LEVIATÁN", 1, "Evil Geniuses", 2, "Evil Geniuses", "1-2", "Completed"),
            ("Regular Season", "Week 5", "2023-05-02", "00:30:00", "LOUD", 2, "KRÜ Esports", 1, "LOUD", "2-1", "Completed"),
            ("Regular Season", "Week 6", "2023-05-07", "00:30:00", "Evil Geniuses", 2, "Sentinels", 0, "Evil Geniuses", "2-0", "Completed"),
            ("Regular Season", "Week 6", "2023-05-07", "02:40:00", "Cloud9", 2, "MIBR", 0, "Cloud9", "2-0", "Completed"),
            ("Regular Season", "Week 6", "2023-05-08", "00:30:00", "LOUD", 2, "100 Thieves", 0, "LOUD", "2-0", "Completed"),
            ("Regular Season", "Week 6", "2023-05-08", "03:00:00", "LEVIATÁN", 2, "KRÜ Esports", 0, "LEVIATÁN", "2-0", "Completed"),
            ("Regular Season", "Week 6", "2023-05-09", "00:30:00", "NRG", 2, "FURIA", 1, "NRG", "2-1", "Completed"),
            ("Regular Season", "Week 7", "2023-05-14", "00:30:00", "FURIA", 1, "100 Thieves", 2, "100 Thieves", "1-2", "Completed"),
            ("Regular Season", "Week 7", "2023-05-14", "04:00:00", "Evil Geniuses", 2, "MIBR", 0, "Evil Geniuses", "2-0", "Completed"),
            ("Regular Season", "Week 7", "2023-05-15", "00:30:00", "KRÜ Esports", 0, "Sentinels", 2, "Sentinels", "0-2", "Completed"),
            ("Regular Season", "Week 7", "2023-05-15", "03:15:00", "NRG", 2, "LOUD", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 7", "2023-05-16", "00:30:00", "LEVIATÁN", 0, "Cloud9", 2, "Cloud9", "0-2", "Completed"),
            ("Regular Season", "Week 8", "2023-05-19", "00:30:00", "Sentinels", 2, "FURIA", 1, "Sentinels", "2-1", "Completed"),
            ("Regular Season", "Week 8", "2023-05-19", "04:15:00", "NRG", 2, "Evil Geniuses", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 8", "2023-05-20", "00:30:00", "Cloud9", 2, "KRÜ Esports", 1, "Cloud9", "2-1", "Completed"),
            ("Regular Season", "Week 8", "2023-05-20", "04:10:00", "LEVIATÁN", 0, "LOUD", 2, "LOUD", "0-2", "Completed"),
            ("Regular Season", "Week 8", "2023-05-21", "00:30:00", "MIBR", 2, "100 Thieves", 1, "MIBR", "2-1", "Completed"),
            ("Playoffs", "Upper Round 1", "2023-05-24", "01:25:00", "LEVIATÁN", 1, "FURIA", 2, "FURIA", "1-2", "Completed"),
            ("Playoffs", "Upper Round 1", "2023-05-24", "05:15:00", "NRG", 1, "Evil Geniuses", 2, "Evil Geniuses", "1-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-05-25", "01:20:00", "LOUD", 2, "FURIA", 0, "LOUD", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-05-25", "03:40:00", "Cloud9", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-05-26", "01:30:00", "FURIA", 0, "NRG", 2, "NRG", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-05-26", "04:00:00", "Cloud9", 2, "LEVIATÁN", 1, "Cloud9", "2-1", "Completed"),
            ("Playoffs", "Upper Final", "2023-05-27", "01:30:00", "LOUD", 2, "Evil Geniuses", 1, "LOUD", "2-1", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-05-27", "04:50:00", "Cloud9", 1, "NRG", 2, "NRG", "1-2", "Completed"),
            ("Playoffs", "Lower Final", "2023-05-28", "01:30:00", "Evil Geniuses", 1, "NRG", 3, "NRG", "1-3", "Completed"),
            ("Playoffs", "Grand Final", "2023-05-29", "01:30:00", "LOUD", 3, "NRG", 0, "LOUD", "3-0", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: Masters Tokyo",
        "event_prize": "$1,000,000 USD",
        "event_location": "Tokyo, Japan",
        "event_dates": "Jun 11 - 25, 2023",
        "matches": [
            ("Group Stage", "Opening (B)", "2023-06-11", "08:30:00", "FUT Esports", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Group Stage", "Opening (B)", "2023-06-11", "11:15:00", "DRX", 2, "Attacking Soul Esports", 0, "DRX", "2-0", "Completed"),
            ("Group Stage", "Opening (A)", "2023-06-11", "13:45:00", "EDward Gaming", 1, "T1", 2, "T1", "1-2", "Completed"),
            ("Group Stage", "Opening (A)", "2023-06-12", "08:30:00", "NRG", 2, "Natus Vincere", 1, "NRG", "2-1", "Completed"),
            ("Group Stage", "Winner's (B)", "2023-06-12", "12:00:00", "DRX", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Group Stage", "Winner's (A)", "2023-06-13", "08:30:00", "NRG", 2, "T1", 1, "NRG", "2-1", "Completed"),
            ("Group Stage", "Elimination (B)", "2023-06-13", "12:15:00", "Attacking Soul Esports", 1, "FUT Esports", 2, "FUT Esports", "1-2", "Completed"),
            ("Group Stage", "Elimination (A)", "2023-06-13", "15:15:00", "Natus Vincere", 0, "EDward Gaming", 2, "EDward Gaming", "0-2", "Completed"),
            ("Group Stage", "Decider (B)", "2023-06-14", "08:30:00", "DRX", 2, "FUT Esports", 1, "DRX", "2-1", "Completed"),
            ("Group Stage", "Decider (A)", "2023-06-14", "11:45:00", "T1", 0, "EDward Gaming", 2, "EDward Gaming", "0-2", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-06-16", "08:30:00", "LOUD", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-06-16", "11:00:00", "Team Liquid", 2, "EDward Gaming", 1, "Team Liquid", "2-1", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-06-17", "08:30:00", "FNATIC", 2, "NRG", 0, "FNATIC", "2-0", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-06-17", "11:00:00", "Paper Rex", 2, "DRX", 0, "Paper Rex", "2-0", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-06-18", "08:30:00", "EDward Gaming", 2, "LOUD", 0, "EDward Gaming", "2-0", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-06-18", "11:05:00", "DRX", 0, "NRG", 2, "NRG", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-06-19", "08:30:00", "Team Liquid", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-06-19", "10:45:00", "Paper Rex", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-06-20", "08:30:00", "Team Liquid", 1, "NRG", 2, "NRG", "1-2", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-06-20", "12:15:00", "Paper Rex", 2, "EDward Gaming", 1, "Paper Rex", "2-1", "Completed"),
            ("Playoffs", "Upper Final", "2023-06-21", "08:30:00", "FNATIC", 2, "Evil Geniuses", 1, "FNATIC", "2-1", "Completed"),
            ("Playoffs", "Lower Round 3", "2023-06-21", "11:55:00", "NRG", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("Playoffs", "Lower Final", "2023-06-24", "08:30:00", "Evil Geniuses", 3, "Paper Rex", 2, "Evil Geniuses", "3-2", "Completed"),
            ("Playoffs", "Grand Final", "2023-06-25", "10:00:00", "FNATIC", 3, "Evil Geniuses", 0, "FNATIC", "3-0", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: Champions China Qualifier",
        "event_prize": "$0 USD",
        "event_location": "China",
        "event_dates": "Jun 1, 2023 - Jul 16, 2023",
        "matches": [
            ("Preliminary Stage", "Round 1", "2023-06-01", "14:30:00", "Weibo Gaming", 0, "Totoro Gaming", 2, "Totoro Gaming", "0-2", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-01", "14:30:00", "Number One Player", 0, "Douyu Gaming", 2, "Douyu Gaming", "0-2", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-01", "17:30:00", "Gank Gaming", 1, "Royal Never Give Up", 2, "Royal Never Give Up", "1-2", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-01", "17:30:00", "Four Angry Men", 1, "Night Wings Gaming", 2, "Night Wings Gaming", "1-2", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-02", "14:30:00", "Invincible Gaming", 0, "Nova Esports", 2, "Nova Esports", "0-2", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-02", "14:30:00", "TYLOO", 2, "Monarch Effect", 1, "TYLOO", "2-1", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-02", "17:30:00", "Shenzhen NTER", 2, "Kingzone", 0, "Shenzhen NTER", "2-0", "Completed"),
            ("Preliminary Stage", "Round 1", "2023-06-02", "18:30:00", "Dragon Ranger Gaming", 2, "Rare Atom", 1, "Dragon Ranger Gaming", "2-1", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-03", "14:30:00", "Totoro Gaming", 2, "Shenzhen NTER", 0, "Totoro Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-03", "14:30:00", "Dragon Ranger Gaming", 2, "Royal Never Give Up", 0, "Dragon Ranger Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-03", "17:30:00", "Nova Esports", 0, "TYLOO", 2, "TYLOO", "0-2", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-03", "17:30:00", "Night Wings Gaming", 0, "Douyu Gaming", 2, "Douyu Gaming", "0-2", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-04", "14:30:00", "Gank Gaming", 2, "Invincible Gaming", 0, "Gank Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-04", "14:30:00", "Number One Player", 2, "Kingzone", 0, "Number One Player", "2-0", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-04", "16:30:00", "Weibo Gaming", 2, "Four Angry Men", 1, "Weibo Gaming", "2-1", "Completed"),
            ("Preliminary Stage", "Round 2", "2023-06-04", "17:30:00", "Rare Atom", 1, "Monarch Effect", 2, "Monarch Effect", "1-2", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-05", "14:30:00", "Weibo Gaming", 2, "Shenzhen NTER", 0, "Weibo Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-05", "14:30:00", "Royal Never Give Up", 2, "Nova Esports", 1, "Royal Never Give Up", "2-1", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-05", "17:05:00", "Night Wings Gaming", 2, "Gank Gaming", 0, "Night Wings Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-05", "17:30:00", "Number One Player", 1, "Monarch Effect", 2, "Monarch Effect", "1-2", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-06", "14:30:00", "Totoro Gaming", 2, "Douyu Gaming", 0, "Totoro Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-06", "14:30:00", "Kingzone", 0, "Four Angry Men", 2, "Four Angry Men", "0-2", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-06", "16:45:00", "Invincible Gaming", 2, "Rare Atom", 0, "Invincible Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 3", "2023-06-06", "16:50:00", "Dragon Ranger Gaming", 0, "TYLOO", 2, "TYLOO", "0-2", "Completed"),
            ("Preliminary Stage", "Round 4", "2023-06-07", "11:30:00", "Weibo Gaming", 2, "Night Wings Gaming", 0, "Weibo Gaming", "2-0", "Completed"),
            ("Preliminary Stage", "Round 4", "2023-06-07", "11:30:00", "Four Angry Men", 2, "Invincible Gaming", 1, "Four Angry Men", "2-1", "Completed"),
            ("Preliminary Stage", "Round 4", "2023-06-07", "13:45:00", "Douyu Gaming", 0, "Royal Never Give Up", 2, "Royal Never Give Up", "0-2", "Completed"),
            ("Preliminary Stage", "Round 4", "2023-06-07", "13:45:00", "Nova Esports", 1, "Gank Gaming", 2, "Gank Gaming", "1-2", "Completed"),
            ("Preliminary Stage", "Round 4", "2023-06-07", "16:20:00", "Dragon Ranger Gaming", 1, "Monarch Effect", 2, "Monarch Effect", "1-2", "Completed"),
            ("Preliminary Stage", "Round 4", "2023-06-07", "16:45:00", "Shenzhen NTER", 2, "Number One Player", 0, "Shenzhen NTER", "2-0", "Completed"),
            ("Preliminary Stage", "Round 5", "2023-06-08", "11:30:00", "Night Wings Gaming", 1, "Shenzhen NTER", 2, "Shenzhen NTER", "1-2", "Completed"),
            ("Preliminary Stage", "Round 5", "2023-06-08", "14:30:00", "Gank Gaming", 1, "Four Angry Men", 2, "Four Angry Men", "1-2", "Completed"),
            ("Preliminary Stage", "Round 5", "2023-06-08", "18:30:00", "Dragon Ranger Gaming", 2, "Douyu Gaming", 0, "Dragon Ranger Gaming", "2-0", "Completed"),
            ("Playoffs", "Knockout Round", "2023-07-03", "14:30:00", "Trace Esports", 2, "Four Angry Men", 0, "Trace Esports", "2-0", "Completed"),
            ("Playoffs", "Knockout Round", "2023-07-03", "17:00:00", "Monarch Effect", 2, "Royal Never Give Up", 1, "Monarch Effect", "2-1", "Completed"),
            ("Playoffs", "Knockout Round", "2023-07-04", "14:30:00", "TYLOO", 2, "Shenzhen NTER", 0, "TYLOO", "2-0", "Completed"),
            ("Playoffs", "Knockout Round", "2023-07-04", "16:45:00", "Weibo Gaming", 2, "Dragon Ranger Gaming", 1, "Weibo Gaming", "2-1", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-07-05", "14:30:00", "Attacking Soul Esports", 1, "Trace Esports", 2, "Trace Esports", "1-2", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-07-05", "17:30:00", "Bilibili Gaming", 2, "Monarch Effect", 0, "Bilibili Gaming", "2-0", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-07-06", "14:30:00", "FunPlus Phoenix", 0, "TYLOO", 2, "TYLOO", "0-2", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2023-07-06", "16:45:00", "EDward Gaming", 2, "Weibo Gaming", 0, "EDward Gaming", "2-0", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-07-07", "14:30:00", "Attacking Soul Esports", 2, "Monarch Effect", 0, "Attacking Soul Esports", "2-0", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-07-07", "17:30:00", "FunPlus Phoenix", 2, "Weibo Gaming", 0, "FunPlus Phoenix", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-07-08", "14:30:00", "Trace Esports", 0, "Bilibili Gaming", 3, "Bilibili Gaming", "0-3", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-07-09", "14:30:00", "TYLOO", 0, "EDward Gaming", 3, "EDward Gaming", "0-3", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-07-10", "14:30:00", "Trace Esports", 1, "FunPlus Phoenix", 2, "FunPlus Phoenix", "1-2", "Completed"),
            ("Playoffs", "Lower Round 2", "2023-07-10", "17:30:00", "TYLOO", 2, "Attacking Soul Esports", 1, "TYLOO", "2-1", "Completed"),
            ("Playoffs", "Upper Final", "2023-07-13", "14:30:00", "Bilibili Gaming", 0, "EDward Gaming", 3, "EDward Gaming", "0-3", "Completed"),
            ("Playoffs", "Lower Round 3", "2023-07-14", "14:30:00", "TYLOO", 1, "FunPlus Phoenix", 3, "FunPlus Phoenix", "1-3", "Completed"),
            ("Playoffs", "Lower Final", "2023-07-15", "14:30:00", "Bilibili Gaming", 3, "FunPlus Phoenix", 2, "Bilibili Gaming", "3-2", "Completed"),
            ("Playoffs", "Grand Final", "2023-07-16", "14:30:00", "EDward Gaming", 3, "Bilibili Gaming", 1, "EDward Gaming", "3-1", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: Pacific Last Chance Qualifier",
        "event_prize": "TBD",
        "event_location": "Seoul, South Korea",
        "event_dates": "Jul 18 - 23, 2023",
        "matches": [
            ("Main Event", "Upper Round 1", "2023-07-18", "13:30:00", "TALON", 2, "DetonatioN FocusMe", 0, "TALON", "2-0", "Completed"),
            ("Main Event", "Upper Quarterfinals", "2023-07-19", "13:30:00", "Rex Regum Qeon", 2, "Global Esports", 0, "Rex Regum Qeon", "2-0", "Completed"),
            ("Main Event", "Upper Quarterfinals", "2023-07-19", "16:45:00", "Gen.G", 2, "TALON", 1, "Gen.G", "2-1", "Completed"),
            ("Main Event", "Upper Semifinals", "2023-07-20", "13:30:00", "ZETA DIVISION", 2, "Rex Regum Qeon", 1, "ZETA DIVISION", "2-1", "Completed"),
            ("Main Event", "Upper Semifinals", "2023-07-20", "17:40:00", "Team Secret", 2, "Gen.G", 0, "Team Secret", "2-0", "Completed"),
            ("Main Event", "Upper Final", "2023-07-21", "13:30:00", "ZETA DIVISION", 2, "Team Secret", 0, "ZETA DIVISION", "2-0", "Completed"),
            ("Main Event", "Lower Round 1", "2023-07-21", "15:55:00", "Rex Regum Qeon", 1, "Gen.G", 2, "Gen.G", "1-2", "Completed"),
            ("Main Event", "Lower Final", "2023-07-22", "13:30:00", "Team Secret", 3, "Gen.G", 1, "Team Secret", "3-1", "Completed"),
            ("Main Event", "Grand Final", "2023-07-23", "13:30:00", "ZETA DIVISION", 3, "Team Secret", 1, "ZETA DIVISION", "3-1", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: EMEA Last Chance Qualifier",
        "event_prize": "TBD",
        "event_location": "EMEA",
        "event_dates": "Jul 19 - 24, 2023",
        "matches": [
            ("Playoffs", "Knockout Round", "2023-07-19", "15:00:00", "Team Heretics", 1, "KOI", 2, "KOI", "1-2", "Completed"),
            ("Playoffs", "Knockout Round", "2023-07-19", "19:10:00", "BBL Esports", 1, "Karmine Corp", 2, "Karmine Corp", "1-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-07-20", "15:00:00", "Natus Vincere", 0, "KOI", 2, "KOI", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2023-07-20", "17:20:00", "Giants Gaming", 2, "Karmine Corp", 0, "Giants Gaming", "2-0", "Completed"),
            ("Playoffs", "Upper Final", "2023-07-21", "14:40:00", "KOI", 0, "Giants Gaming", 2, "Giants Gaming", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2023-07-21", "17:35:00", "Natus Vincere", 2, "Karmine Corp", 1, "Natus Vincere", "2-1", "Completed"),
            ("Playoffs", "Lower Final", "2023-07-22", "15:00:00", "KOI", 0, "Natus Vincere", 3, "Natus Vincere", "0-3", "Completed"),
            ("Playoffs", "Grand Final", "2023-07-23", "15:00:00", "Giants Gaming", 3, "Natus Vincere", 0, "Giants Gaming", "3-0", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2023: Americas Last Chance Qualifier",
        "event_prize": "TBD",
        "event_location": "Americas",
        "event_dates": "Jul 15 - 24, 2023",
        "matches": [
            ("Main Event", "Upper Round 1", "2023-07-16", "01:30:00", "MIBR", 0, "KRÜ Esports", 2, "KRÜ Esports", "0-2", "Completed"),
            ("Main Event", "Upper Quarterfinals", "2023-07-17", "01:30:00", "FURIA", 1, "KRÜ Esports", 2, "KRÜ Esports", "1-2", "Completed"),
            ("Main Event", "Upper Quarterfinals", "2023-07-17", "05:15:00", "Sentinels", 2, "100 Thieves", 1, "Sentinels", "2-1", "Completed"),
            ("Main Event", "Upper Semifinals", "2023-07-18", "01:30:00", "Cloud9", 2, "Sentinels", 1, "Cloud9", "2-1", "Completed"),
            ("Main Event", "Upper Semifinals", "2023-07-18", "04:30:00", "LEVIATÁN", 0, "KRÜ Esports", 2, "KRÜ Esports", "0-2", "Completed"),
            ("Main Event", "Upper Final", "2023-07-19", "01:30:00", "Cloud9", 1, "KRÜ Esports", 2, "KRÜ Esports", "1-2", "Completed"),
            ("Main Event", "Lower Round 1", "2023-07-19", "04:35:00", "Sentinels", 0, "LEVIATÁN", 2, "LEVIATÁN", "0-2", "Completed"),
            ("Main Event", "Lower Final", "2023-07-23", "01:30:00", "Cloud9", 2, "LEVIATÁN", 3, "LEVIATÁN", "2-3", "Completed"),
            ("Main Event", "Grand Final", "2023-07-24", "01:30:00", "KRÜ Esports", 3, "LEVIATÁN", 1, "KRÜ Esports", "3-1", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: Pacific Kickoff",
        "event_prize": "$0 USD",
        "event_location": "S FACTORY Tower D, Seoul",
        "event_dates": "Feb 17 - 26, 2024",
        "matches": [
            ("Group Stage", "Opening (A)", "2024-02-17", "11:30:00", "T1", 2, "BLEED", 0, "T1", "2-0", "Completed"),
            ("Group Stage", "Opening (C)", "2024-02-17", "19:15:00", "Gen.G", 2, "Rex Regum Qeon", 1, "Gen.G", "2-1", "Completed"),
            ("Group Stage", "Opening (A)", "2024-02-18", "11:30:00", "ZETA DIVISION", 2, "Global Esports", 0, "ZETA DIVISION", "2-0", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-18", "14:00:00", "Team Secret", 0, "TALON", 2, "TALON", "2-0", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-18", "16:00:00", "DRX", 2, "DetonatioN FocusMe", 0, "DRX", "2-0", "Completed"),
            ("Group Stage", "Winner's (C)", "2024-02-19", "11:30:00", "Gen.G", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("Group Stage", "Elimination (A)", "2024-02-19", "14:45:00", "BLEED", 1, "Global Esports", 2, "Global Esports", "1-2", "Completed"),
            ("Group Stage", "Winner's (A)", "2024-02-19", "18:30:00", "T1", 2, "ZETA DIVISION", 1, "T1", "2-1", "Completed"),
            ("Group Stage", "Elimination (B)", "2024-02-20", "13:30:00", "DetonatioN FocusMe", 0, "Team Secret", 2, "Team Secret", "2-0", "Completed"),
            ("Group Stage", "Winner's (B)", "2024-02-20", "15:50:00", "DRX", 2, "TALON", 0, "DRX", "2-0", "Completed"),
            ("Group Stage", "Decider (C)", "2024-02-21", "11:30:00", "Gen.G", 2, "Rex Regum Qeon", 1, "Gen.G", "2-1", "Completed"),
            ("Group Stage", "Decider (B)", "2024-02-21", "15:00:00", "TALON", 0, "Team Secret", 2, "Team Secret", "0-2", "Completed"),
            ("Group Stage", "Decider (A)", "2024-02-21", "17:45:00", "ZETA DIVISION", 2, "Global Esports", 0, "ZETA DIVISION", "2-0", "Completed"),
            ("Play-Ins", "Play-ins", "2024-02-22", "11:30:00", "Team Secret", 1, "Gen.G", 2, "Gen.G", "1-2", "Completed"),
            ("Play-Ins", "Play-ins", "2024-02-22", "14:50:00", "ZETA DIVISION", 0, "Team Secret", 2, "Team Secret", "0-2", "Completed"),
            ("Play-Ins", "Play-ins", "2024-02-22", "17:00:00", "Gen.G", 2, "ZETA DIVISION", 0, "Gen.G", "2-0", "Completed"),
            ("Playoffs", "Semifinals", "2024-02-24", "13:30:00", "T1", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Playoffs", "Semifinals", "2024-02-24", "15:55:00", "DRX", 0, "Gen.G", 2, "Gen.G", "0-2", "Completed"),
            ("Playoffs", "Grand Final", "2024-02-25", "13:30:00", "Paper Rex", 1, "Gen.G", 3, "Gen.G", "1-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: EMEA Kickoff",
        "event_prize": "$0 USD",
        "event_location": "Riot Games Arena, Berlin",
        "event_dates": "Feb 20, 2024 - Mar 2, 2024",
        "matches": [
            ("Group Stage", "Opening (A)", "2024-02-20", "21:30:00", "FUT Esports", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Group Stage", "Opening (A)", "2024-02-21", "00:05:00", "GIANTX", 1, "Karmine Corp", 2, "Karmine Corp", "1-2", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-21", "18:30:00", "Natus Vincere", 2, "BBL Esports", 1, "Natus Vincere", "2-1", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-21", "21:30:00", "Team Liquid", 2, "KOI", 0, "Team Liquid", "2-0", "Completed"),
            ("Group Stage", "Opening (C)", "2024-02-22", "00:15:00", "Team Vitality", 2, "Gentle Mates", 0, "Team Vitality", "2-0", "Completed"),
            ("Group Stage", "Winner's (A)", "2024-02-22", "21:30:00", "Team Heretics", 2, "Karmine Corp", 0, "Team Heretics", "2-0", "Completed"),
            ("Group Stage", "Elimination (A)", "2024-02-22", "23:40:00", "FUT Esports", 2, "GIANTX", 1, "FUT Esports", "2-1", "Completed"),
            ("Group Stage", "Winner's (B)", "2024-02-23", "18:30:00", "Natus Vincere", 2, "Team Liquid", 0, "Natus Vincere", "2-0", "Completed"),
            ("Group Stage", "Elimination (B)", "2024-02-23", "20:40:00", "BBL Esports", 0, "KOI", 2, "KOI", "0-2", "Completed"),
            ("Group Stage", "Winner's (C)", "2024-02-23", "22:50:00", "Team Vitality", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Group Stage", "Decider (C)", "2024-02-25", "18:35:00", "Team Vitality", 2, "Gentle Mates", 1, "Team Vitality", "2-1", "Completed"),
            ("Group Stage", "Decider (A)", "2024-02-25", "21:45:00", "Karmine Corp", 2, "FUT Esports", 1, "Karmine Corp", "2-1", "Completed"),
            ("Group Stage", "Decider (B)", "2024-02-26", "01:15:00", "Team Liquid", 1, "KOI", 2, "KOI", "1-2", "Completed"),
            ("Play-In Stage", "Play-ins", "2024-02-26", "18:30:00", "Karmine Corp", 2, "Team Vitality", 0, "Karmine Corp", "2-0", "Completed"),
            ("Play-In Stage", "Play-ins", "2024-02-26", "21:15:00", "KOI", 0, "Team Vitality", 2, "Team Vitality", "0-2", "Completed"),
            ("Play-In Stage", "Play-ins", "2024-02-26", "23:15:00", "Karmine Corp", 2, "KOI", 0, "Karmine Corp", "2-0", "Completed"),
            ("Playoffs", "Semifinals", "2024-02-29", "21:30:00", "Team Heretics", 2, "Natus Vincere", 0, "Team Heretics", "2-0", "Completed"),
            ("Playoffs", "Semifinals", "2024-02-29", "23:50:00", "FNATIC", 0, "Karmine Corp", 2, "Karmine Corp", "0-2", "Completed"),
            ("Playoffs", "Grand Final", "2024-03-01", "21:30:00", "Team Heretics", 1, "Karmine Corp", 3, "Karmine Corp", "1-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: China Kickoff",
        "event_prize": "$0 USD",
        "event_location": "VCT CN Arena, Shanghai",
        "event_dates": "Feb 22, 2024 - Mar 3, 2024",
        "matches": [
            ("Group Stage", "Opening (A)", "2024-02-22", "14:30:00", "Trace Esports", 2, "TYLOO", 0, "Trace Esports", "2-0", "Completed"),
            ("Group Stage", "Opening (A)", "2024-02-22", "16:35:00", "FunPlus Phoenix", 2, "Nova Esports", 0, "FunPlus Phoenix", "2-0", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-23", "12:30:00", "JDG Esports", 0, "Titan Esports Club", 2, "Titan Esports Club", "0-2", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-23", "15:25:00", "Dragon Ranger Gaming", 2, "All Gamers", 0, "Dragon Ranger Gaming", "2-0", "Completed"),
            ("Group Stage", "Opening (C)", "2024-02-23", "17:35:00", "Bilibili Gaming", 0, "Wolves Esports", 2, "Wolves Esports", "0-2", "Completed"),
            ("Group Stage", "Elimination (A)", "2024-02-24", "14:30:00", "TYLOO", 0, "Nova Esports", 2, "Nova Esports", "0-2", "Completed"),
            ("Group Stage", "Elimination (B)", "2024-02-24", "16:55:00", "JDG Esports", 2, "All Gamers", 0, "JDG Esports", "2-0", "Completed"),
            ("Group Stage", "Winner's (A)", "2024-02-25", "12:30:00", "Trace Esports", 1, "FunPlus Phoenix", 2, "FunPlus Phoenix", "1-2", "Completed"),
            ("Group Stage", "Winner's (B)", "2024-02-25", "16:00:00", "Titan Esports Club", 1, "Dragon Ranger Gaming", 2, "Dragon Ranger Gaming", "1-2", "Completed"),
            ("Group Stage", "Winner's (C)", "2024-02-25", "19:30:00", "Wolves Esports", 1, "EDward Gaming", 2, "EDward Gaming", "1-2", "Completed"),
            ("Group Stage", "Decider (A)", "2024-02-26", "12:30:00", "Trace Esports", 2, "Nova Esports", 0, "Trace Esports", "2-0", "Completed"),
            ("Group Stage", "Decider (B)", "2024-02-26", "14:35:00", "Titan Esports Club", 2, "JDG Esports", 1, "Titan Esports Club", "2-1", "Completed"),
            ("Group Stage", "Decider (C)", "2024-02-26", "18:10:00", "Wolves Esports", 0, "Bilibili Gaming", 2, "Bilibili Gaming", "0-2", "Completed"),
            ("Play-Ins", "Round-Robin", "2024-02-27", "12:30:00", "Trace Esports", 2, "Titan Esports Club", 1, "Trace Esports", "2-1", "Completed"),
            ("Play-Ins", "Round-Robin", "2024-02-27", "16:05:00", "Bilibili Gaming", 2, "Titan Esports Club", 0, "Bilibili Gaming", "2-0", "Completed"),
            ("Play-Ins", "Round-Robin", "2024-02-27", "18:05:00", "Bilibili Gaming", 1, "Trace Esports", 2, "Trace Esports", "1-2", "Completed"),
            ("Playoffs", "Semifinals", "2024-03-01", "14:30:00", "FunPlus Phoenix", 2, "Dragon Ranger Gaming", 0, "FunPlus Phoenix", "2-0", "Completed"),
            ("Playoffs", "Semifinals", "2024-03-01", "16:45:00", "EDward Gaming", 2, "Trace Esports", 0, "EDward Gaming", "2-0", "Completed"),
            ("Playoffs", "Grand Final", "2024-03-02", "14:30:00", "FunPlus Phoenix", 1, "EDward Gaming", 3, "EDward Gaming", "1-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: Americas Kickoff",
        "event_prize": "$0 USD",
        "event_location": "Riot Games Arena, Los Angeles",
        "event_dates": "Feb 17, 2024 - Mar 4, 2024",
        "matches": [
            ("Group Stage", "Opening (A)", "2024-02-17", "03:30:00", "NRG", 2, "FURIA", 0, "NRG", "2-0", "Completed"),
            ("Group Stage", "Opening (A)", "2024-02-17", "06:30:00", "Cloud9", 2, "MIBR", 1, "Cloud9", "2-1", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-18", "03:30:00", "LOUD", 2, "Sentinels", 0, "LOUD", "2-0", "Completed"),
            ("Group Stage", "Opening (B)", "2024-02-18", "06:05:00", "LEVIATÁN", 2, "100 Thieves", 1, "LEVIATÁN", "2-1", "Completed"),
            ("Group Stage", "Opening (C)", "2024-02-19", "03:30:00", "KRÜ Esports", 1, "G2 Esports", 2, "G2 Esports", "1-2", "Completed"),
            ("Group Stage", "Elimination (A)", "2024-02-20", "03:30:00", "FURIA", 0, "MIBR", 2, "MIBR", "0-2", "Completed"),
            ("Group Stage", "Elimination (B)", "2024-02-20", "06:15:00", "Sentinels", 2, "100 Thieves", 1, "Sentinels", "2-1", "Completed"),
            ("Group Stage", "Winner's (A)", "2024-02-24", "03:30:00", "NRG", 2, "Cloud9", 0, "NRG", "2-0", "Completed"),
            ("Group Stage", "Winner's (B)", "2024-02-24", "05:55:00", "LOUD", 2, "LEVIATÁN", 1, "LOUD", "2-1", "Completed"),
            ("Group Stage", "Winner's (C)", "2024-02-25", "03:30:00", "G2 Esports", 0, "Evil Geniuses", 2, "Evil Geniuses", "0-2", "Completed"),
            ("Group Stage", "Decider (A)", "2024-02-26", "01:30:00", "Cloud9", 0, "MIBR", 2, "MIBR", "0-2", "Completed"),
            ("Group Stage", "Decider (B)", "2024-02-26", "04:10:00", "LEVIATÁN", 1, "Sentinels", 2, "Sentinels", "1-2", "Completed"),
            ("Group Stage", "Decider (C)", "2024-02-26", "07:25:00", "G2 Esports", 2, "KRÜ Esports", 0, "G2 Esports", "2-0", "Completed"),
            ("Play-Ins", "Play-ins", "2024-02-27", "01:30:00", "MIBR", 0, "Sentinels", 2, "Sentinels", "0-2", "Completed"),
            ("Play-Ins", "Play-ins", "2024-02-27", "03:40:00", "G2 Esports", 1, "MIBR", 2, "MIBR", "1-2", "Completed"),
            ("Play-Ins", "Play-ins", "2024-02-27", "07:25:00", "Sentinels", 1, "G2 Esports", 2, "G2 Esports", "1-2", "Completed"),
            ("Playoffs", "Semifinals", "2024-03-03", "03:30:00", "Evil Geniuses", 1, "LOUD", 2, "LOUD", "1-2", "Completed"),
            ("Playoffs", "Semifinals", "2024-03-03", "06:30:00", "NRG", 1, "Sentinels", 2, "Sentinels", "1-2", "Completed"),
            ("Playoffs", "Grand Final", "2024-03-04", "03:30:00", "LOUD", 2, "Sentinels", 3, "Sentinels", "2-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: Masters Madrid",
        "event_prize": "$500,000 USD",
        "event_location": "Madrid Arena, Madrid",
        "event_dates": "Mar 14 - 24, 2024",
        "matches": [
            ("Swiss Stage", "Round 1", "2024-03-14", "20:30:00", "Karmine Corp", 2, "FunPlus Phoenix", 0, "Karmine Corp", "2-0", "Completed"),
            ("Swiss Stage", "Round 1", "2024-03-14", "22:55:00", "Gen.G", 2, "LOUD", 1, "Gen.G", "2-1", "Completed"),
            ("Swiss Stage", "Round 1", "2024-03-15", "20:30:00", "EDward Gaming", 2, "Paper Rex", 1, "EDward Gaming", "2-1", "Completed"),
            ("Swiss Stage", "Round 1", "2024-03-15", "23:45:00", "Sentinels", 2, "Team Heretics", 1, "Sentinels", "2-1", "Completed"),
            ("Swiss Stage", "Round 2", "2024-03-16", "20:30:00", "Sentinels", 2, "Karmine Corp", 0, "Sentinels", "2-0", "Completed"),
            ("Swiss Stage", "Round 2", "2024-03-16", "22:55:00", "EDward Gaming", 1, "Gen.G", 2, "Gen.G", "1-2", "Completed"),
            ("Swiss Stage", "Round 2", "2024-03-17", "20:30:00", "FunPlus Phoenix", 0, "LOUD", 2, "LOUD", "0-2", "Completed"),
            ("Swiss Stage", "Round 2", "2024-03-17", "22:50:00", "Team Heretics", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("Swiss Stage", "Round 3", "2024-03-18", "20:30:00", "LOUD", 2, "EDward Gaming", 0, "LOUD", "2-0", "Completed"),
            ("Swiss Stage", "Round 3", "2024-03-18", "22:25:00", "Karmine Corp", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-03-21", "20:30:00", "Gen.G", 2, "Paper Rex", 0, "Gen.G", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-03-21", "22:40:00", "Sentinels", 2, "LOUD", 1, "Sentinels", "2-1", "Completed"),
            ("Playoffs", "Upper Final", "2024-03-22", "20:30:00", "Gen.G", 2, "Sentinels", 1, "Gen.G", "2-1", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-03-22", "23:25:00", "Paper Rex", 2, "LOUD", 0, "Paper Rex", "2-0", "Completed"),
            ("Playoffs", "Lower Final", "2024-03-23", "20:30:00", "Sentinels", 3, "Paper Rex", 1, "Sentinels", "3-1", "Completed"),
            ("Showmatch", "Showmatch", "2024-03-24", "20:30:00", "Team International", 8, "Team Spain", 13, "Team Spain", "8-13", "Completed"),
            ("Playoffs", "Grand Final", "2024-03-24", "21:45:00", "Gen.G", 2, "Sentinels", 3, "Sentinels", "2-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: Pacific Stage 1",
        "event_prize": "$0 USD",
        "event_location": "COEX Artium, Seoul",
        "event_dates": "Apr 6, 2024 - May 12, 2024",
        "matches": [
            ("Regular Season", "Week 1", "2024-04-06", "13:30:00", "Global Esports", 1, "ZETA DIVISION", 2, "ZETA DIVISION", "1-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-06", "16:30:00", "Team Secret", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-07", "13:30:00", "BLEED", 1, "TALON", 2, "TALON", "1-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-07", "16:45:00", "T1", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-08", "13:30:00", "Team Secret", 1, "Rex Regum Qeon", 2, "Rex Regum Qeon", "1-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-08", "16:50:00", "Global Esports", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-09", "13:30:00", "Gen.G", 2, "TALON", 0, "Gen.G", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2024-04-09", "15:40:00", "T1", 1, "DetonatioN FocusMe", 2, "DetonatioN FocusMe", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-13", "13:30:00", "Gen.G", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-13", "16:40:00", "T1", 1, "DRX", 2, "DRX", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-14", "13:30:00", "Team Secret", 2, "ZETA DIVISION", 1, "Team Secret", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-14", "16:30:00", "BLEED", 0, "Rex Regum Qeon", 2, "Rex Regum Qeon", "0-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-15", "13:30:00", "Gen.G", 2, "DetonatioN FocusMe", 0, "Gen.G", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2024-04-15", "15:40:00", "Global Esports", 1, "TALON", 2, "TALON", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-16", "13:30:00", "T1", 2, "Rex Regum Qeon", 0, "T1", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2024-04-16", "15:30:00", "BLEED", 1, "ZETA DIVISION", 2, "ZETA DIVISION", "1-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-20", "13:30:00", "Gen.G", 1, "DRX", 2, "DRX", "1-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-20", "16:45:00", "BLEED", 2, "DetonatioN FocusMe", 1, "BLEED", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-21", "13:30:00", "Global Esports", 2, "Rex Regum Qeon", 0, "Global Esports", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-21", "16:30:00", "Team Secret", 2, "Paper Rex", 0, "Team Secret", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-22", "13:30:00", "T1", 0, "TALON", 2, "TALON", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-22", "15:45:00", "Gen.G", 2, "ZETA DIVISION", 0, "Gen.G", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-23", "13:30:00", "Team Secret", 2, "DetonatioN FocusMe", 1, "Team Secret", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-23", "16:20:00", "Global Esports", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-27", "13:30:00", "BLEED", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-27", "15:30:00", "Global Esports", 2, "DetonatioN FocusMe", 1, "Global Esports", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-28", "13:30:00", "T1", 2, "ZETA DIVISION", 1, "T1", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-28", "16:40:00", "Team Secret", 1, "TALON", 2, "TALON", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-29", "13:30:00", "BLEED", 0, "DRX", 2, "DRX", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-29", "15:35:00", "Gen.G", 1, "Rex Regum Qeon", 2, "Rex Regum Qeon", "1-2", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-03", "13:30:00", "Team Secret", 0, "T1", 2, "T1", "0-2", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-03", "15:40:00", "Paper Rex", 2, "TALON", 1, "Paper Rex", "2-1", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-04", "13:30:00", "Gen.G", 1, "T1", 2, "T1", "1-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-04", "16:40:00", "DRX", 1, "Paper Rex", 2, "Paper Rex", "1-2", "Completed"),
            ("Playoffs", "Upper Final", "2024-05-05", "13:30:00", "T1", 0, "Paper Rex", 2, "Paper Rex", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-05-05", "15:30:00", "Gen.G", 2, "DRX", 1, "Gen.G", "2-1", "Completed"),
            ("Playoffs", "Lower Final", "2024-05-11", "13:30:00", "T1", 0, "Gen.G", 3, "Gen.G", "0-3", "Completed"),
            ("Playoffs", "Grand Final", "2024-05-12", "13:30:00", "Paper Rex", 3, "Gen.G", 2, "Paper Rex", "3-2", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: EMEA Stage 1",
        "event_prize": "$0 USD",
        "event_location": "Riot Games Arena, Berlin",
        "event_dates": "Apr 4, 2024 - May 13, 2024",
        "matches": [
            ("Regular Season", "Week 1", "2024-04-03", "20:30:00", "Karmine Corp", 2, "GIANTX", 0, "Karmine Corp", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2024-04-03", "22:35:00", "KOI", 0, "Team Liquid", 2, "Team Liquid", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-04", "20:30:00", "Team Vitality", 0, "Natus Vincere", 2, "Natus Vincere", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-04", "22:40:00", "FNATIC", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-05", "20:30:00", "Team Liquid", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-05", "22:30:00", "BBL Esports", 0, "Gentle Mates", 2, "Gentle Mates", "0-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-10", "20:30:00", "Karmine Corp", 1, "FUT Esports", 2, "FUT Esports", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-10", "23:40:00", "Team Vitality", 2, "Team Heretics", 1, "Team Vitality", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-11", "20:30:00", "Team Liquid", 1, "Natus Vincere", 2, "Natus Vincere", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-11", "23:50:00", "BBL Esports", 2, "KOI", 0, "BBL Esports", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2024-04-12", "20:30:00", "FNATIC", 2, "GIANTX", 1, "FNATIC", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-12", "23:15:00", "Karmine Corp", 2, "Gentle Mates", 0, "Karmine Corp", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-17", "20:30:00", "Gentle Mates", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-17", "22:30:00", "Karmine Corp", 1, "Natus Vincere", 2, "Natus Vincere", "1-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-18", "20:30:00", "BBL Esports", 2, "Team Heretics", 0, "BBL Esports", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-18", "22:45:00", "Team Vitality", 2, "FUT Esports", 1, "Team Vitality", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-19", "20:30:00", "Team Liquid", 2, "GIANTX", 1, "Team Liquid", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-20", "00:25:00", "FNATIC", 2, "KOI", 0, "FNATIC", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2024-04-24", "20:30:00", "Team Liquid", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-24", "22:30:00", "Team Vitality", 0, "Gentle Mates", 2, "Gentle Mates", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-25", "20:30:00", "FNATIC", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-25", "23:00:00", "BBL Esports", 2, "Natus Vincere", 1, "BBL Esports", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-26", "20:30:00", "Team Vitality", 2, "GIANTX", 1, "Team Vitality", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-26", "23:40:00", "Karmine Corp", 2, "KOI", 1, "Karmine Corp", "2-1", "Completed"),
            ("Regular Season", "Week 5", "2024-05-01", "20:30:00", "BBL Esports", 0, "GIANTX", 2, "GIANTX", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-01", "22:30:00", "Karmine Corp", 1, "Team Heretics", 2, "Team Heretics", "1-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-02", "20:30:00", "Team Vitality", 1, "KOI", 2, "KOI", "1-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-02", "23:25:00", "Natus Vincere", 2, "FNATIC", 1, "Natus Vincere", "2-1", "Completed"),
            ("Regular Season", "Week 5", "2024-05-03", "20:30:00", "Team Liquid", 2, "Gentle Mates", 0, "Team Liquid", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2024-05-03", "22:20:00", "BBL Esports", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-08", "20:30:00", "FNATIC", 2, "Team Liquid", 1, "FNATIC", "2-1", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-08", "23:50:00", "Natus Vincere", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-09", "20:30:00", "Karmine Corp", 0, "FNATIC", 2, "FNATIC", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-09", "23:00:00", "FUT Esports", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Playoffs", "Upper Final", "2024-05-10", "20:30:00", "FNATIC", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-05-10", "23:00:00", "Karmine Corp", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Playoffs", "Lower Final", "2024-05-11", "20:30:00", "FNATIC", 3, "FUT Esports", 1, "FNATIC", "3-1", "Completed"),
            ("Playoffs", "Grand Final", "2024-05-12", "20:30:00", "Team Heretics", 2, "FNATIC", 3, "FNATIC", "2-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: Americas Stage 1",
        "event_prize": "$0 USD",
        "event_location": "Riot Games Arena, Los Angeles",
        "event_dates": "Apr 7, 2024 - May 13, 2024",
        "matches": [
            ("Regular Season", "Week 1", "2024-04-07", "02:30:00", "Cloud9", 2, "LEVIATÁN", 1, "Cloud9", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2024-04-07", "06:30:00", "NRG", 2, "LOUD", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2024-04-08", "02:30:00", "G2 Esports", 2, "Evil Geniuses", 0, "G2 Esports", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2024-04-08", "04:40:00", "Sentinels", 2, "100 Thieves", 0, "Sentinels", "2-0", "Completed"),
            ("Regular Season", "Week 1", "2024-04-09", "02:30:00", "KRÜ Esports", 2, "FURIA", 1, "KRÜ Esports", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-14", "02:30:00", "G2 Esports", 0, "100 Thieves", 2, "100 Thieves", "0-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-14", "04:55:00", "Sentinels", 0, "LEVIATÁN", 2, "LEVIATÁN", "0-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-15", "02:30:00", "KRÜ Esports", 2, "MIBR", 0, "KRÜ Esports", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2024-04-15", "04:50:00", "NRG", 2, "FURIA", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2024-04-16", "02:30:00", "Cloud9", 2, "Evil Geniuses", 1, "Cloud9", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-21", "02:30:00", "Sentinels", 2, "MIBR", 0, "Sentinels", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-21", "05:00:00", "Cloud9", 2, "LOUD", 1, "Cloud9", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-22", "02:30:00", "KRÜ Esports", 2, "Evil Geniuses", 0, "KRÜ Esports", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-22", "04:45:00", "NRG", 0, "LEVIATÁN", 2, "LEVIATÁN", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-23", "02:30:00", "G2 Esports", 2, "FURIA", 0, "G2 Esports", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-23", "04:30:00", "Cloud9", 0, "100 Thieves", 2, "100 Thieves", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-24", "02:30:00", "Sentinels", 1, "Evil Geniuses", 2, "Evil Geniuses", "1-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-24", "06:00:00", "NRG", 2, "MIBR", 0, "NRG", "2-0", "Completed"),
            ("Regular Season", "Week 3", "2024-04-25", "02:30:00", "G2 Esports", 1, "LEVIATÁN", 2, "LEVIATÁN", "1-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-25", "05:45:00", "KRÜ Esports", 2, "LOUD", 0, "KRÜ Esports", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2024-04-28", "02:30:00", "G2 Esports", 2, "MIBR", 0, "G2 Esports", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2024-04-28", "04:35:00", "Sentinels", 0, "LOUD", 2, "LOUD", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-29", "02:30:00", "Cloud9", 2, "FURIA", 1, "Cloud9", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-29", "05:25:00", "NRG", 1, "Evil Geniuses", 2, "Evil Geniuses", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-30", "02:30:00", "KRÜ Esports", 2, "100 Thieves", 1, "KRÜ Esports", "2-1", "Completed"),
            ("Regular Season", "Week 5", "2024-05-04", "05:30:00", "Sentinels", 2, "FURIA", 0, "Sentinels", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2024-05-05", "02:30:00", "NRG", 0, "100 Thieves", 2, "100 Thieves", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-05", "04:50:00", "KRÜ Esports", 1, "LEVIATÁN", 2, "LEVIATÁN", "1-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-06", "02:30:00", "Cloud9", 2, "MIBR", 0, "Cloud9", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2024-05-06", "05:05:00", "G2 Esports", 0, "LOUD", 2, "LOUD", "0-2", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-09", "02:30:00", "Cloud9", 0, "G2 Esports", 2, "G2 Esports", "0-2", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-09", "04:55:00", "100 Thieves", 2, "LOUD", 0, "100 Thieves", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-10", "02:30:00", "KRÜ Esports", 0, "G2 Esports", 2, "G2 Esports", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-10", "04:35:00", "LEVIATÁN", 1, "100 Thieves", 2, "100 Thieves", "1-2", "Completed"),
            ("Playoffs", "Upper Final", "2024-05-11", "02:30:00", "G2 Esports", 1, "100 Thieves", 2, "100 Thieves", "1-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-05-11", "05:30:00", "KRÜ Esports", 1, "LEVIATÁN", 2, "LEVIATÁN", "1-2", "Completed"),
            ("Playoffs", "Lower Final", "2024-05-12", "02:30:00", "G2 Esports", 3, "LEVIATÁN", 2, "G2 Esports", "3-2", "Completed"),
            ("Playoffs", "Grand Final", "2024-05-13", "02:30:00", "100 Thieves", 3, "G2 Esports", 0, "100 Thieves", "3-0", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: China Stage 1",
        "event_prize": "$0 USD",
        "event_location": "VCT CN Arena, Shanghai",
        "event_dates": "Apr 5, 2024 - May 13, 2024",
        "matches": [
            ("Regular Season", "Week 1", "2024-04-05", "14:30:00", "Bilibili Gaming", 2, "TYLOO", 1, "Bilibili Gaming", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2024-04-05", "17:40:00", "Wolves Esports", 1, "Titan Esports Club", 2, "Titan Esports Club", "1-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-06", "14:30:00", "Dragon Ranger Gaming", 1, "All Gamers", 2, "All Gamers", "1-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-06", "18:15:00", "EDward Gaming", 2, "JDG Esports", 1, "EDward Gaming", "2-1", "Completed"),
            ("Regular Season", "Week 1", "2024-04-07", "14:30:00", "Nova Esports", 0, "Trace Esports", 2, "Trace Esports", "0-2", "Completed"),
            ("Regular Season", "Week 1", "2024-04-07", "16:45:00", "FunPlus Phoenix", 2, "Wolves Esports", 0, "FunPlus Phoenix", "2-0", "Completed"),
            ("Regular Season", "Week 2", "2024-04-12", "14:30:00", "JDG Esports", 1, "Nova Esports", 2, "Nova Esports", "1-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-12", "17:45:00", "FunPlus Phoenix", 2, "Dragon Ranger Gaming", 1, "FunPlus Phoenix", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-13", "14:30:00", "All Gamers", 0, "Wolves Esports", 2, "Wolves Esports", "0-2", "Completed"),
            ("Regular Season", "Week 2", "2024-04-13", "17:15:00", "Trace Esports", 2, "Bilibili Gaming", 1, "Trace Esports", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-14", "14:30:00", "Dragon Ranger Gaming", 2, "Titan Esports Club", 1, "Dragon Ranger Gaming", "2-1", "Completed"),
            ("Regular Season", "Week 2", "2024-04-14", "17:20:00", "TYLOO", 0, "EDward Gaming", 2, "EDward Gaming", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-19", "14:30:00", "Wolves Esports", 0, "Trace Esports", 2, "Trace Esports", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-19", "16:55:00", "Nova Esports", 0, "FunPlus Phoenix", 2, "FunPlus Phoenix", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-20", "14:30:00", "Bilibili Gaming", 0, "All Gamers", 2, "All Gamers", "0-2", "Completed"),
            ("Regular Season", "Week 3", "2024-04-20", "17:10:00", "Dragon Ranger Gaming", 2, "JDG Esports", 1, "Dragon Ranger Gaming", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-21", "14:30:00", "TYLOO", 2, "Nova Esports", 1, "TYLOO", "2-1", "Completed"),
            ("Regular Season", "Week 3", "2024-04-21", "18:30:00", "EDward Gaming", 2, "Titan Esports Club", 0, "EDward Gaming", "2-0", "Completed"),
            ("Regular Season", "Week 4", "2024-04-26", "14:30:00", "Titan Esports Club", 2, "Bilibili Gaming", 1, "Titan Esports Club", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-26", "17:35:00", "Trace Esports", 0, "Dragon Ranger Gaming", 2, "Dragon Ranger Gaming", "0-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-27", "14:30:00", "TYLOO", 1, "Wolves Esports", 2, "Wolves Esports", "1-2", "Completed"),
            ("Regular Season", "Week 4", "2024-04-27", "18:00:00", "FunPlus Phoenix", 2, "EDward Gaming", 1, "FunPlus Phoenix", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-28", "14:30:00", "All Gamers", 2, "Nova Esports", 1, "All Gamers", "2-1", "Completed"),
            ("Regular Season", "Week 4", "2024-04-28", "18:10:00", "Bilibili Gaming", 2, "JDG Esports", 0, "Bilibili Gaming", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2024-05-02", "16:30:00", "EDward Gaming", 2, "All Gamers", 0, "EDward Gaming", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2024-05-03", "16:30:00", "Wolves Esports", 0, "JDG Esports", 2, "JDG Esports", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-04", "14:30:00", "Dragon Ranger Gaming", 0, "TYLOO", 2, "TYLOO", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-04", "17:00:00", "Bilibili Gaming", 0, "FunPlus Phoenix", 2, "FunPlus Phoenix", "0-2", "Completed"),
            ("Regular Season", "Week 5", "2024-05-05", "14:30:00", "Nova Esports", 2, "Titan Esports Club", 0, "Nova Esports", "2-0", "Completed"),
            ("Regular Season", "Week 5", "2024-05-05", "16:35:00", "Trace Esports", 0, "EDward Gaming", 2, "EDward Gaming", "0-2", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-08", "14:30:00", "Trace Esports", 2, "All Gamers", 0, "Trace Esports", "2-0", "Completed"),
            ("Playoffs", "Knockout Round", "2024-05-08", "16:45:00", "Dragon Ranger Gaming", 2, "Nova Esports", 0, "Dragon Ranger Gaming", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-09", "14:30:00", "FunPlus Phoenix", 2, "Trace Esports", 0, "FunPlus Phoenix", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-05-09", "17:00:00", "EDward Gaming", 2, "Dragon Ranger Gaming", 0, "EDward Gaming", "2-0", "Completed"),
            ("Playoffs", "Upper Final", "2024-05-10", "14:30:00", "FunPlus Phoenix", 2, "EDward Gaming", 0, "FunPlus Phoenix", "2-0", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-05-10", "17:15:00", "Trace Esports", 1, "Dragon Ranger Gaming", 2, "Dragon Ranger Gaming", "1-2", "Completed"),
            ("Playoffs", "Lower Final", "2024-05-11", "14:30:00", "EDward Gaming", 3, "Dragon Ranger Gaming", 1, "EDward Gaming", "3-1", "Completed"),
            ("Playoffs", "Grand Final", "2024-05-12", "14:30:00", "FunPlus Phoenix", 1, "EDward Gaming", 3, "EDward Gaming", "1-3", "Completed"),
        ],
    },
    {
        "event_name": "Champions Tour 2024: Masters Shanghai",
        "event_prize": "$1,000,000 USD",
        "event_location": "VCT CN Arena & Mercedes-Benz Arena",
        "event_dates": "May 23, 2024 - Jun 9, 2024",
        "matches": [
            ("Swiss Stage", "Round 1", "2024-05-23", "13:30:00", "G2 Esports", 2, "T1", 1, "G2 Esports", "2-1", "Completed"),
            ("Swiss Stage", "Round 1", "2024-05-23", "16:40:00", "FunPlus Phoenix", 2, "FUT Esports", 1, "FunPlus Phoenix", "2-1", "Completed"),
            ("Swiss Stage", "Round 1", "2024-05-24", "13:30:00", "Gen.G", 2, "LEVIATÃN", 1, "Gen.G", "2-1", "Completed"),
            ("Swiss Stage", "Round 1", "2024-05-24", "16:30:00", "Team Heretics", 2, "Dragon Ranger Gaming", 0, "Team Heretics", "2-0", "Completed"),
            ("Swiss Stage", "Round 2", "2024-05-25", "13:30:00", "FunPlus Phoenix", 1, "Gen.G", 2, "Gen.G", "1-2", "Completed"),
            ("Swiss Stage", "Round 2", "2024-05-25", "17:10:00", "G2 Esports", 2, "Team Heretics", 1, "G2 Esports", "2-1", "Completed"),
            ("Swiss Stage", "Round 2", "2024-05-26", "13:30:00", "LEVIATÃN", 2, "T1", 0, "LEVIATÃN", "2-0", "Completed"),
            ("Swiss Stage", "Round 2", "2024-05-26", "15:40:00", "Dragon Ranger Gaming", 0, "FUT Esports", 2, "FUT Esports", "0-2", "Completed"),
            ("Swiss Stage", "Round 3", "2024-05-27", "13:30:00", "FunPlus Phoenix", 1, "Team Heretics", 2, "Team Heretics", "1-2", "Completed"),
            ("Swiss Stage", "Round 3", "2024-05-27", "17:05:00", "FUT Esports", 2, "LEVIATÃN", 1, "FUT Esports", "2-1", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2024-05-30", "13:30:00", "100 Thieves", 2, "FUT Esports", 0, "100 Thieves", "2-0", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2024-05-30", "15:30:00", "FNATIC", 1, "Gen.G", 2, "Gen.G", "1-2", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2024-05-31", "13:30:00", "Paper Rex", 1, "G2 Esports", 2, "G2 Esports", "1-2", "Completed"),
            ("Playoffs", "Upper Quarterfinals", "2024-05-31", "16:30:00", "EDward Gaming", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-06-01", "13:30:00", "FUT Esports", 2, "FNATIC", 1, "FUT Esports", "2-1", "Completed"),
            ("Playoffs", "Lower Round 1", "2024-06-01", "16:30:00", "Paper Rex", 2, "EDward Gaming", 0, "Paper Rex", "2-0", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-06-02", "13:30:00", "100 Thieves", 0, "Gen.G", 2, "Gen.G", "0-2", "Completed"),
            ("Playoffs", "Upper Semifinals", "2024-06-02", "15:45:00", "G2 Esports", 2, "Team Heretics", 1, "G2 Esports", "2-1", "Completed"),
            ("Playoffs", "Lower Round 2", "2024-06-03", "13:30:00", "100 Thieves", 2, "Paper Rex", 1, "100 Thieves", "2-1", "Completed"),
            ("Playoffs", "Lower Round 2", "2024-06-03", "16:40:00", "Team Heretics", 2, "FUT Esports", 0, "Team Heretics", "2-0", "Completed"),
            ("Playoffs", "Upper Final", "2024-06-07", "12:30:00", "G2 Esports", 0, "Gen.G", 2, "Gen.G", "0-2", "Completed"),
            ("Playoffs", "Lower Round 3", "2024-06-07", "14:55:00", "100 Thieves", 0, "Team Heretics", 2, "Team Heretics", "0-2", "Completed"),
            ("Playoffs", "Lower Final", "2024-06-08", "12:30:00", "G2 Esports", 0, "Team Heretics", 3, "Team Heretics", "0-3", "Completed"),
            ("Showmatch", "Showmatch", "2024-06-09", "12:30:00", "Team International", 11, "Team China", 13, "Team China", "11-13", "Completed"),
            ("Playoffs", "Grand Final", "2024-06-09", "13:45:00", "Gen.G", 3, "Team Heretics", 2, "Gen.G", "3-2", "Completed"),
        ],
    },
]


CREATE_MATCHES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS matches (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    event_stage VARCHAR(100) NOT NULL,
    match_series VARCHAR(100) NOT NULL,
    match_date DATE NOT NULL,
    match_time TIME NOT NULL,
    map_name VARCHAR(50),
    team1_id INT,
    team1_name VARCHAR(100) NOT NULL,
    team1_score INT NOT NULL,
    team2_id INT,
    team2_name VARCHAR(100) NOT NULL,
    team2_score INT NOT NULL,
    winner_team_id INT,
    winner_team_name VARCHAR(100) NOT NULL,
    winning_score VARCHAR(20) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (team1_id) REFERENCES teams(team_id),
    FOREIGN KEY (team2_id) REFERENCES teams(team_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
)
"""


CREATE_MAPS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS maps (
    map_id INT AUTO_INCREMENT PRIMARY KEY,
    map_name VARCHAR(50) NOT NULL UNIQUE
)
"""


CREATE_MATCH_MAPS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS match_maps (
    match_map_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT NOT NULL,
    map_number INT NOT NULL,
    map_id INT,
    map_name VARCHAR(50) NOT NULL,
    team1_score INT,
    team2_score INT,
    winner_team_id INT,
    winner_team_name VARCHAR(100),
    UNIQUE KEY uniq_match_map (match_id, map_number),
    FOREIGN KEY (match_id) REFERENCES matches(match_id),
    FOREIGN KEY (map_id) REFERENCES maps(map_id),
    FOREIGN KEY (winner_team_id) REFERENCES teams(team_id)
)
"""


CREATE_EVENTS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255) NOT NULL UNIQUE,
    event_prize VARCHAR(100) NOT NULL,
    event_location VARCHAR(150) NOT NULL,
    event_dates VARCHAR(100) NOT NULL
)
"""


INSERT_EVENT_SQL = """
INSERT INTO events (event_name, event_prize, event_location, event_dates)
VALUES (%s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    event_prize = VALUES(event_prize),
    event_location = VALUES(event_location),
    event_dates = VALUES(event_dates)
"""


INSERT_MATCH_SQL = """
INSERT INTO matches (
    event_id,
    event_stage,
    match_series,
    match_date,
    match_time,
    map_name,
    team1_id,
    team1_name,
    team1_score,
    team2_id,
    team2_name,
    team2_score,
    winner_team_id,
    winner_team_name,
    winning_score,
    status
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


INSERT_MAP_SQL = """
INSERT INTO maps (map_name)
VALUES (%s)
ON DUPLICATE KEY UPDATE
    map_name = VALUES(map_name)
"""


INSERT_MATCH_MAP_SQL = """
INSERT INTO match_maps (
    match_id,
    map_number,
    map_id,
    map_name,
    team1_score,
    team2_score,
    winner_team_id,
    winner_team_name
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    map_id = VALUES(map_id),
    map_name = VALUES(map_name),
    team1_score = VALUES(team1_score),
    team2_score = VALUES(team2_score),
    winner_team_id = VALUES(winner_team_id),
    winner_team_name = VALUES(winner_team_name)
"""


INSERT_TEAM_SQL = """
INSERT INTO teams (team_name, league, coach_name, founded_year)
VALUES (%s, %s, %s, %s)
"""


TEAM_NAME_ALIASES = {
    "FNATIC": "Fnatic",
    "KOI": "Movistar KOI",
    "LEVIATÁN": "Leviatán",
    "KRÜ Esports": "KRÜ Esports",
    "NRG": "NRG Esports",
    "TALON": "Talon Esports",
}


def get_team_id_maps(cursor):
    cursor.execute("SELECT team_id, team_name FROM teams")
    raw_rows = cursor.fetchall()
    exact_name_to_id = {team_name: team_id for team_id, team_name in raw_rows if team_name}
    normalized_name_to_id = {normalize_team_name(team_name): team_id for team_id, team_name in raw_rows if team_name}
    return exact_name_to_id, normalized_name_to_id


def get_map_id_map(cursor):
    cursor.execute("SELECT map_id, map_name FROM maps")
    return {map_name: map_id for map_id, map_name in cursor.fetchall() if map_name}


def normalize_team_name(team_name: str) -> str:
    return (
        team_name.strip()
        .lower()
        .replace("á", "a")
        .replace("ã", "a")
        .replace("ü", "u")
        .replace("û", "u")
    )


def resolve_team_id(team_name: str, exact_name_to_id: dict, normalized_name_to_id: dict):
    canonical_name = TEAM_NAME_ALIASES.get(team_name, team_name)
    if canonical_name in exact_name_to_id:
        return exact_name_to_id[canonical_name]
    return normalized_name_to_id.get(normalize_team_name(canonical_name))


def ensure_team_id(cursor, team_name: str, exact_name_to_id: dict, normalized_name_to_id: dict):
    team_id = resolve_team_id(team_name, exact_name_to_id, normalized_name_to_id)
    if team_id is not None:
        return team_id

    cursor.execute(INSERT_TEAM_SQL, (team_name, "Unknown", None, None))
    team_id = cursor.lastrowid

    exact_name_to_id[team_name] = team_id
    normalized_name_to_id[normalize_team_name(team_name)] = team_id
    return team_id


def ensure_map_id(cursor, map_name: str, map_name_to_id: dict):
    map_id = map_name_to_id.get(map_name)
    if map_id is not None:
        return map_id

    cursor.execute(INSERT_MAP_SQL, (map_name,))
    cursor.execute("SELECT map_id FROM maps WHERE map_name = %s", (map_name,))
    map_id = cursor.fetchone()[0]
    map_name_to_id[map_name] = map_id
    return map_id


def get_or_create_event_id(cursor, event_data: dict):
    cursor.execute(
        INSERT_EVENT_SQL,
        (
            event_data["event_name"],
            event_data["event_prize"],
            event_data["event_location"],
            event_data["event_dates"],
        ),
    )
    cursor.execute("SELECT event_id FROM events WHERE event_name = %s", (event_data["event_name"],))
    return cursor.fetchone()[0]


def get_existing_match_keys(cursor, event_id: int):
    cursor.execute(
        """
        SELECT event_stage, match_series, match_date, match_time, team1_name, team2_name
        FROM matches
        WHERE event_id = %s
        """,
        (event_id,),
    )
    return {
        (
            row[0],
            row[1],
            row[2].isoformat() if row[2] is not None else None,
            normalize_time_value(row[3]),
            row[4],
            row[5],
        )
        for row in cursor.fetchall()
    }


def normalize_time_value(value):
    if value is None:
        return None
    if hasattr(value, "strftime"):
        return value.strftime("%H:%M:%S")
    if isinstance(value, timedelta):
        total_seconds = int(value.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return str(value)


def build_insert_rows(cursor, event_id: int, matches: list[tuple]):
    exact_name_to_id, normalized_name_to_id = get_team_id_maps(cursor)
    existing_match_keys = get_existing_match_keys(cursor, event_id)
    rows = []

    for match in matches:
        match_key = (match[0], match[1], match[2], match[3], match[4], match[6])
        if match_key in existing_match_keys:
            continue

        team1_id = ensure_team_id(cursor, match[4], exact_name_to_id, normalized_name_to_id)
        team2_id = ensure_team_id(cursor, match[6], exact_name_to_id, normalized_name_to_id)
        winner_team_id = ensure_team_id(cursor, match[8], exact_name_to_id, normalized_name_to_id)

        rows.append(
            (
                event_id,
                match[0],
                match[1],
                match[2],
                match[3],
                None,
                team1_id,
                match[4],
                match[5],
                team2_id,
                match[6],
                match[7],
                winner_team_id,
                match[8],
                match[9],
                match[10],
            )
        )

    return rows


def get_match_id_by_key(cursor, event_id: int, match: tuple):
    cursor.execute(
        """
        SELECT match_id
        FROM matches
        WHERE event_id = %s
          AND event_stage = %s
          AND match_series = %s
          AND match_date = %s
          AND match_time = %s
          AND team1_name = %s
          AND team2_name = %s
        """,
        (event_id, match[0], match[1], match[2], match[3], match[4], match[6]),
    )
    row = cursor.fetchone()
    return row[0] if row else None


def insert_match_maps(cursor, event_id: int, matches: list[tuple]):
    exact_name_to_id, normalized_name_to_id = get_team_id_maps(cursor)
    map_name_to_id = get_map_id_map(cursor)

    for match in matches:
        match_maps_data = None
        if len(match) > 12 and isinstance(match[12], list):
            match_maps_data = match[12]
        elif len(match) > 11:
            if isinstance(match[11], list):
                match_maps_data = match[11]
            elif isinstance(match[11], str):
                match_maps_data = [
                    {"map_name": map_name.strip()}
                    for map_name in match[11].split(",")
                    if map_name.strip()
                ]

        if not match_maps_data:
            continue

        match_id = get_match_id_by_key(cursor, event_id, match)
        if match_id is None:
            continue

        for map_number, map_data in enumerate(match_maps_data, start=1):
            if isinstance(map_data, dict):
                map_name = map_data.get("map_name")
                team1_score = map_data.get("team1_score")
                team2_score = map_data.get("team2_score")
                winner_team_name = map_data.get("winner_team_name")
            else:
                map_name, team1_score, team2_score, winner_team_name = map_data

            if not map_name:
                continue

            map_id = ensure_map_id(cursor, map_name, map_name_to_id)
            winner_team_id = None
            if winner_team_name:
                winner_team_id = ensure_team_id(cursor, winner_team_name, exact_name_to_id, normalized_name_to_id)

            cursor.execute(
                INSERT_MATCH_MAP_SQL,
                (
                    match_id,
                    map_number,
                    map_id,
                    map_name,
                    team1_score,
                    team2_score,
                    winner_team_id,
                    winner_team_name,
                ),
            )


def backfill_match_maps_from_match_names(cursor):
    map_name_to_id = get_map_id_map(cursor)
    cursor.execute(
        """
        SELECT m.match_id, m.map_name
        FROM matches m
        WHERE m.map_name IS NOT NULL
          AND TRIM(m.map_name) <> ''
          AND NOT EXISTS (
              SELECT 1
              FROM match_maps mm
              WHERE mm.match_id = m.match_id
          )
        """
    )

    for match_id, map_name_blob in cursor.fetchall():
        map_names = [map_name.strip() for map_name in map_name_blob.split(",") if map_name.strip()]
        for map_number, map_name in enumerate(map_names, start=1):
            map_id = ensure_map_id(cursor, map_name, map_name_to_id)
            cursor.execute(
                INSERT_MATCH_MAP_SQL,
                (
                    match_id,
                    map_number,
                    map_id,
                    map_name,
                    None,
                    None,
                    None,
                    None,
                ),
            )


def backfill_match_team_links(cursor):
    exact_name_to_id, normalized_name_to_id = get_team_id_maps(cursor)
    cursor.execute(
        """
        SELECT match_id, team1_name, team2_name, winner_team_name
        FROM matches
        WHERE team1_id IS NULL OR team2_id IS NULL OR winner_team_id IS NULL
        """
    )

    for match_id, team1_name, team2_name, winner_team_name in cursor.fetchall():
        team1_id = ensure_team_id(cursor, team1_name, exact_name_to_id, normalized_name_to_id)
        team2_id = ensure_team_id(cursor, team2_name, exact_name_to_id, normalized_name_to_id)
        winner_team_id = ensure_team_id(cursor, winner_team_name, exact_name_to_id, normalized_name_to_id)

        cursor.execute(
            """
            UPDATE matches
            SET team1_id = %s,
                team2_id = %s,
                winner_team_id = %s
            WHERE match_id = %s
            """,
            (team1_id, team2_id, winner_team_id, match_id),
        )


def ensure_tables(cursor):
    cursor.execute(CREATE_MAPS_TABLE_SQL)
    cursor.execute(CREATE_EVENTS_TABLE_SQL)
    cursor.execute(CREATE_MATCHES_TABLE_SQL)
    cursor.execute(CREATE_MATCH_MAPS_TABLE_SQL)
    cursor.execute(
        """
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_schema = DATABASE()
          AND table_name = 'matches'
          AND column_name = 'map_name'
        """
    )
    if cursor.fetchone()[0] == 0:
        cursor.execute("ALTER TABLE matches ADD COLUMN map_name VARCHAR(50) NULL AFTER match_time")

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM information_schema.columns
        WHERE table_schema = DATABASE()
          AND table_name = 'matches'
          AND column_name = 'map_id'
        """
    )
    if cursor.fetchone()[0] > 0:
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM information_schema.referential_constraints
            WHERE constraint_schema = DATABASE()
              AND constraint_name = 'fk_matches_map_id'
              AND table_name = 'matches'
            """
        )
        if cursor.fetchone()[0] > 0:
            cursor.execute("ALTER TABLE matches DROP FOREIGN KEY fk_matches_map_id")
        cursor.execute(
            "ALTER TABLE matches DROP COLUMN map_id"
        )


def main():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    ensure_tables(cursor)

    total_inserted = 0

    for event_data in EVENT_DATA:
        event_id = get_or_create_event_id(cursor, event_data)
        insert_rows = build_insert_rows(cursor, event_id, event_data["matches"])
        if insert_rows:
            cursor.executemany(INSERT_MATCH_SQL, insert_rows)
            total_inserted += len(insert_rows)
        insert_match_maps(cursor, event_id, event_data["matches"])

    backfill_match_team_links(cursor)
    backfill_match_maps_from_match_names(cursor)

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM events")
    total_events = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM matches")
    total_matches = cursor.fetchone()[0]

    print("events table ready")
    print(f"events table now contains {total_events} rows")
    print(f"new match rows inserted in this run: {total_inserted}")
    print(f"matches table now contains {total_matches} rows")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()

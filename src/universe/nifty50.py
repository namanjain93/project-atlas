from pathlib import Path
import pandas as pd


class Nifty50Universe:

    def __init__(
        self,
        events_path,
        starting_members_path
    ):

        self.events_path = Path(events_path)
        self.starting_members_path = Path(starting_members_path)

        self.events = pd.read_csv(
            self.events_path,
            parse_dates=["effective_date"]
        )

        starting = pd.read_csv(
            self.starting_members_path
        )

        self.starting_members = set(
            starting["symbol"].astype(str)
        )

        if len(self.starting_members) != 50:
            raise ValueError(
                f"Starting universe must contain 50 unique members. "
                f"Found {len(self.starting_members)}."
            )

        self.events = self.events.sort_values(
            ["effective_date", "action", "normalized_symbol"]
        ).reset_index(drop=True)

    def members_on(self, date):

        date = pd.Timestamp(date)

        members = set(self.starting_members)

        applicable = self.events[
            self.events["effective_date"] <= date
        ]

        for _, row in applicable.iterrows():

            symbol = row["normalized_symbol"]

            if row["action"] == "ADD":
                members.add(symbol)

            elif row["action"] == "REMOVE":
                members.discard(symbol)

            else:
                raise ValueError(
                    f"Unknown action: {row['action']}"
                )

        return sorted(members)

    def membership_count(self, date):

        return len(self.members_on(date))

    def validate_dates(self, dates):

        results = []

        for date in dates:

            members = self.members_on(date)

            results.append({
                "date": pd.Timestamp(date),
                "member_count": len(members),
                "valid": len(members) == 50
            })

        return pd.DataFrame(results)

    def validate_events(self):

        members = set(self.starting_members)

        results = []

        for date, group in self.events.groupby(
            "effective_date",
            sort=True
        ):

            adds = set(
                group.loc[
                    group["action"] == "ADD",
                    "normalized_symbol"
                ]
            )

            removes = set(
                group.loc[
                    group["action"] == "REMOVE",
                    "normalized_symbol"
                ]
            )

            duplicate_symbols = (
                adds.intersection(removes)
            )

            invalid_adds = adds.intersection(members)
            invalid_removes = removes - members

            for symbol in removes:
                members.discard(symbol)

            for symbol in adds:
                members.add(symbol)

            results.append({
                "effective_date": date,
                "member_count": len(members),
                "duplicate_add_remove": len(
                    duplicate_symbols
                ),
                "invalid_adds": len(invalid_adds),
                "invalid_removes": len(invalid_removes),
                "valid": (
                    len(members) == 50
                    and len(duplicate_symbols) == 0
                    and len(invalid_adds) == 0
                    and len(invalid_removes) == 0
                )
            })

        return pd.DataFrame(results)

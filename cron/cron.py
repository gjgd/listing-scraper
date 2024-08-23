import json
from slack_client import post_message_to_slack
from scraper import get_listings
import pandas as pd

def get_cheapest(df):
    min_price_index = df['RawPrice'].idxmin()
    min_price_row = df.loc[min_price_index]
    # min_price_row_json = min_price_row.to_json()
    # print(json.dumps(json.loads(min_price_row_json)))

    pwf = min_price_row['PriceWithFees']
    pwf = pwf.replace("$", "")
    pwf = float(pwf)
    p = min_price_row['Price']
    pwfat = p.replace("$", "")
    pwfat = float(pwfat) * 1.42
    pwfat = round(pwfat, 2)
    display_json = {
        "Section": min_price_row['Section'],
        "PriceWithFeesAfterTax": f"${pwfat}",
        "RawPrice": min_price_row['RawPrice'],
        "Price": p,
        "PriceWithFees": pwf,
        "BuyUrl": f"https://stubhub.com{min_price_row['BuyUrl']}",
    }
    return display_json, pwfat

def main(event, context):
    f1_quali_2024 = 152042582
    events = [f1_quali_2024]
    quantity = 2

    for event in events:
        res = get_listings([event], quantity=quantity)
        df = pd.concat([pd.DataFrame(r) for r in res])
        # Print all possible "Section" values
        # print(df['Section'].unique())

        # only keep values where Section startswith T12 or T15
        dfSpecialTurns = df[df['Section'].str.startswith('T12') | df['Section'].str.startswith('T15')]

        cheapestOverall, pwfat = get_cheapest(df)
        cheapestAtT12OrT15, _ = get_cheapest(dfSpecialTurns)

        slack_message_json = {
            "cheapestOverall": cheapestOverall,
            "cheapestAtT12OrT15": cheapestAtT12OrT15,
        }
        slack_message = json.dumps(slack_message_json, indent=4)
        print(json.dumps(slack_message, indent=4))
        if pwfat < 400:
            post_message_to_slack(slack_message, 'stubhub-cron')

if __name__ == "__main__":
    main(None, None)

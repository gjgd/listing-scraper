import json
from slack_client import post_message_to_slack
from scraper import get_listings
import pandas as pd

# def filter_out_parking(df):
#   df = df[(df['Row'] != "PARKI")]
#   df = df[(df['Section'] !=  "PARKING")]
#   return df

# def filter_out_sections(df, sections):
#   df = df[~df['Section'].isin(sections)]
#   return df


def main(event, context):
    f1_quali_2024 = 152042582
    events = [f1_quali_2024]
    quantity = 2

    for event in events:
        res = get_listings([event], quantity=quantity)
        df = pd.concat([pd.DataFrame(r) for r in res])
        # Filters
        # df = filter_out_parking(df)
        # df = filter_out_sections(df, sections_blocklist)

        min_price_index = df['RawPrice'].idxmin()
        min_price_row = df.loc[min_price_index]
        min_price_row_json = min_price_row.to_json()
        # print(json.dumps(json.loads(min_price_row_json)))

        # Print all possible "Section" values
        # print(df['Section'].unique())

        pwf = min_price_row['PriceWithFees']
        pwf = pwf.replace("$", "")
        pwf = float(pwf)
        p = min_price_row['Price']
        pwfat = p.replace("$", "")
        pwfat = float(pwfat) * 1.42
        display_json = {
            "Section": min_price_row['Section'],
            "PriceWithFeesAfterTax": f"${pwfat}",
            "RawPrice": min_price_row['RawPrice'],
            "Price": p,
            "PriceWithFees": pwf,
            "BuyUrl": f"https://stubhub.com{min_price_row['BuyUrl']}",
        }
        print(json.dumps(display_json, indent=4))
        if pwfat < 400:
            post_message_to_slack(display_json, 'stubhub-cron')

if __name__ == "__main__":
    main(None, None)

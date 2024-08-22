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

        display_json = {
            "Section": min_price_row['Section'],
            "RawPrice": min_price_row['RawPrice'],
            "Price": min_price_row['Price'],
            "PriceWithFees": min_price_row['PriceWithFees'],
            "BuyUrl": f"https://stubhub.com{min_price_row['BuyUrl']}",
        }
        print(json.dumps(display_json, indent=4))
        pwf = display_json['PriceWithFees']
        pwf = pwf.replace("$", "")
        pwf = float(pwf)
        if pwf < 300:
            post_message_to_slack(display_json, 'stubhub-cron')

if __name__ == "__main__":
    main(None, None)

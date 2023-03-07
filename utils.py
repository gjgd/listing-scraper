from listing_scraper import st
import pandas as pd
import numpy as np
from opentelemetry.metrics import Observation

def filter_out_parking(df):
  df = df[(df['Row'] != "PARKI")]
  df = df[(df['Section'] !=  "PARKING")]
  return df

def get_concert_prices_callback_by_events(events, metadata):
    def get_concert_prices_callback(observer):
        res = st.get_listings(events)
        df = pd.concat([pd.DataFrame(r) for r in res])
        # df.to_json(save_loc, orient='records')
        # df = pd.read_json(save_loc,)

        # Filter out Parking tickets
        df = filter_out_parking(df)

        min_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.min)
        min_price_dict = min_price['RawPrice'].to_dict()
        for event_id, price in min_price_dict.items():
            labels = {
                "event_id": event_id,
                "event_date": metadata["event_dates"][event_id],
                "event_url": metadata["event_urls"][event_id],
                "event_image": metadata["event_image"],
                "event_artist": metadata["event_artist"],
                "price": "min_price"
            }
            print(labels, price)
            yield Observation(price, labels)

        # avg_price = pd.pivot_table(df, values='RawPrice', index=[
        #                         'EventId'], aggfunc=np.mean)
        # avg_price_dict = avg_price['RawPrice'].to_dict()
        # for event_id, price in avg_price_dict.items():
        #     labels = {
        #         "event_id": event_id,
        #         "event_date": event_dates[event_id],
        #         "price": "avg_price"
        #     }
        #     print(labels, price)
        #     yield Observation(price, labels)

        # max_price = pd.pivot_table(df, values='RawPrice', index=[
        #                         'EventId'], aggfunc=np.max)
        # max_price_dict = max_price['RawPrice'].to_dict()
        # for event_id, price in max_price_dict.items():
        #     labels = {
        #         "event_id": event_id,
        #         "event_date": event_dates[event_id],
        #         "price": "max_price"
        #     }
        #     print(labels, price)
        #     yield Observation(price, labels)
    return get_concert_prices_callback

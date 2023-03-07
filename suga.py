from metrics import meter
import numpy as np
import pandas as pd
from opentelemetry.metrics import Observation
from listing_scraper import st
from utils import filter_out_parking

suga = 151473277

events = [
  suga
]

event_dates = {
    suga: "Sat Apr 29, Newark, NJ",
}

def get_suga_prices_callback_by_events(events):
    def get_suga_prices_callback(observer):
        res = st.get_listings(events)
        df = pd.concat([pd.DataFrame(r) for r in res])
        # save_loc = "suga.json"
        # df.to_json(save_loc, orient='records')
        # df = pd.read_json(save_loc,)

        # Filter out Parking tickets
        df = filter_out_parking(df)

        min_price = pd.pivot_table(df, values='RawPrice', index=[
                                'EventId'], aggfunc=np.min)
        min_price_dict = min_price['RawPrice'].to_dict()
        for event_id, price in min_price_dict.items():
            labels = {
                "event_id": event_id,
                "event_date": event_dates[event_id],
                "price": "min_price"
            }
            print(labels, price)
            yield Observation(price, labels)

        avg_price = pd.pivot_table(df, values='RawPrice', index=[
                                'EventId'], aggfunc=np.mean)
        avg_price_dict = avg_price['RawPrice'].to_dict()
        for event_id, price in avg_price_dict.items():
            labels = {
                "event_id": event_id,
                "event_date": event_dates[event_id],
                "price": "avg_price"
            }
            print(labels, price)
            yield Observation(price, labels)

        max_price = pd.pivot_table(df, values='RawPrice', index=[
                                'EventId'], aggfunc=np.max)
        max_price_dict = max_price['RawPrice'].to_dict()
        for event_id, price in max_price_dict.items():
            labels = {
                "event_id": event_id,
                "event_date": event_dates[event_id],
                "price": "max_price"
            }
            print(labels, price)
            yield Observation(price, labels)
    return get_suga_prices_callback

meter.create_observable_counter(
    callbacks=[get_suga_prices_callback_by_events(events)],
    name="suga_prices",
    unit="",
)

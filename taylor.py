import numpy as np
import pandas as pd
from opentelemetry.metrics import Observation
from listing_scraper import st

# https://www.stubhub.com/taylor-swift-arlington-tickets-3-31-2023/event/151219647/
friday_event_id = 151219647
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-1-2023/event/150593502/
saturday_event_id = 150593502
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-2-2023/event/150593515/
sunday_event_id = 150593515

# https://www.stubhub.com/taylor-swift-houston-tickets-4-21-2023/event/151214693/
friday_houston_event_id = 151214693
# https://www.stubhub.com/taylor-swift-houston-tickets-4-22-2023/event/150593575/
saturday_houston_event_id = 150593575
# https://www.stubhub.com/taylor-swift-houston-tickets-4-23-2023/event/151214704/
sunday_houston_event_id = 151214704

save_loc = 'taylor.json'

event_dates = {
    friday_event_id: "Fri Mar 31, Arlington, Texas",
    saturday_event_id: "Sat Apr 01, Arlington, Texas",
    sunday_event_id: "Sun Apr 02, Arlington, Texas",
    friday_houston_event_id: "Fri Apr 21, Houston, Texas",
    saturday_houston_event_id: "Sat Apr 22, Houston, Texas",
    sunday_houston_event_id: "Sun Apr 23, Houston, Texas",
}

event_urls = {
    friday_event_id: "https://www.stubhub.com/taylor-swift-arlington-tickets-3-31-2023/event/151219647/",
    saturday_event_id: "https://www.stubhub.com/taylor-swift-arlington-tickets-4-1-2023/event/150593502/",
    sunday_event_id: "https://www.stubhub.com/taylor-swift-arlington-tickets-4-2-2023/event/150593515/",
    friday_houston_event_id: "https://www.stubhub.com/taylor-swift-houston-tickets-4-21-2023/event/151214693/",
    saturday_houston_event_id: "https://www.stubhub.com/taylor-swift-houston-tickets-4-22-2023/event/150593575/",
    sunday_houston_event_id: "https://www.stubhub.com/taylor-swift-houston-tickets-4-23-2023/event/151214704/",
}


def get_taylor_prices_callback_by_events(events):
    def get_taylor_prices_callback(observer):

        res = st.get_listings(events)
        df = pd.concat([pd.DataFrame(r) for r in res])
        # df.to_json(save_loc, orient='records')

        # df = pd.read_json(save_loc)

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
    return get_taylor_prices_callback

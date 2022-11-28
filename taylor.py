from dotenv import load_dotenv
load_dotenv()
import os
import time

from listing_scraper import st
from opentelemetry import metrics
from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry.metrics import Observation
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

import pandas as pd
import numpy as np

exporter = PrometheusRemoteWriteMetricsExporter(
    endpoint=os.getenv("PROM_REMOTE_WRITE_URL"),
    basic_auth={
        "username":os.getenv("PROM_REMOTE_WRITE_USER"),
        "password":os.getenv("PROM_REMOTE_WRITE_PASSWORD"),
    },
)
reader = PeriodicExportingMetricReader(exporter, 60 * 1000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

# https://www.stubhub.com/taylor-swift-arlington-tickets-3-31-2023/event/151219647/
friday_event_id = 151219647
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-1-2023/event/150593502/
saturday_event_id = 150593502
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-2-2023/event/150593515/
sunday_event_id = 150593515

save_loc = 'taylor.json'

def get_taylor_prices_callback(observer):

    events = [friday_event_id, saturday_event_id, sunday_event_id]

    res = st.get_listings(events)
    df = pd.concat([pd.DataFrame(r) for r in res])
    # df.to_json(save_loc, orient='records')

    # df = pd.read_json(save_loc)

    print(1)
    min_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.min)
    min_price_dict = min_price['RawPrice'].to_dict()
    for event_id, price in min_price_dict.items():
        labels = {"event_id": event_id, "price": "min_price"}
        print(labels, price)
        yield Observation(price, labels)

    print(2)
    avg_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.mean)
    avg_price_dict = avg_price['RawPrice'].to_dict()
    for event_id, price in avg_price_dict.items():
        labels = {"event_id": event_id, "price": "avg_price"}
        print(labels, price)
        yield Observation(price, labels)

    print(3)
    max_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.max)
    max_price_dict = max_price['RawPrice'].to_dict()
    for event_id, price in max_price_dict.items():
        labels = {"event_id": event_id, "price": "max_price"}
        print(labels, price)
        yield Observation(price, labels)


meter.create_observable_counter(
    callbacks=[get_taylor_prices_callback],
    name="taylor_prices",
    description="",
    unit="",
)

# while True:
#   print("hi")
#   time.sleep(10)

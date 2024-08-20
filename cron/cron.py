from scraper import get_listings
import pandas as pd
import numpy as np

def filter_out_parking(df):
  df = df[(df['Row'] != "PARKI")]
  df = df[(df['Section'] !=  "PARKING")]
  return df

def filter_out_sections(df, sections):
  df = df[~df['Section'].isin(sections)]
  return df

def get_concert_prices_callback_by_events(events, metadata, quantity=None, sections_blocklist=[], max_price=None):
    def get_concert_prices_callback(observer):
        res = get_listings(events, quantity=quantity, max_price=max_price)
        df = pd.concat([pd.DataFrame(r) for r in res])
        # save_loc = metadata.get("event_artist") + ".json"
        # df.to_json(save_loc, orient='records')
        # df = pd.read_json(save_loc,)

        # Filters
        df = filter_out_parking(df)
        df = filter_out_sections(df, sections_blocklist)

        min_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.min)
        min_price_dict = min_price['RawPrice'].to_dict()
        for event_id, price in min_price_dict.items():
            event_url = metadata["event_urls"][event_id]
            if quantity is not None:
                event_url += f"?quantity={quantity}"
            labels = {
                "event_id": event_id,
                "event_date": metadata["event_dates"][event_id],
                "event_url": event_url,
                "event_image": metadata["event_image"],
                "event_artist": metadata["event_artist"],
                "price": "min_price"
            }
            print(labels, price)
    return get_concert_prices_callback

def main(event, context):
  print("hi")

def lol():
  f1_quali_2024 = 152042582

  events = [
      f1_quali_2024
  ]

  metadata = {
      "event_artist": "COTA",
      "event_image":  "https://media.stubhubstatic.com/stubhub-v2-catalog/d_defaultLogo.jpg/q_auto:low,f_auto,c_fill,g_auto,w_280,h_180/categories/421995/6422685",
      "event_dates": {
          f1_quali_2024: "Oct 19 • Sat • 1:05PM • 2024",
      },
      "event_urls": {
          f1_quali_2024: "https://www.stubhub.com/formula-1-austin-tickets-10-19-2024/event/152042582/",
      }
  }

  quantity = 2

  get_concert_prices_callback_by_events(
      events,
      metadata=metadata,
      quantity=quantity,
      max_price=300
  )

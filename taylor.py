from listing_scraper import st

import pandas as pd
import numpy as np

# https://www.stubhub.com/taylor-swift-arlington-tickets-3-31-2023/event/151219647/
friday_event_id = 151219647
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-1-2023/event/150593502/
saturday_event_id = 150593502
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-2-2023/event/150593515/
sunday_event_id = 150593515

events = [friday_event_id, saturday_event_id, sunday_event_id]
# res = st.get_listings(events)
# df = pd.concat([pd.DataFrame(r) for r in res])

save_loc = 'taylor.json'
# df.to_json(save_loc, orient='records')
df = pd.read_json(save_loc)

min_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.min)
print(min_price)

avg_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.mean)
print(avg_price)

max_price = pd.pivot_table(df, values='RawPrice', index=['EventId'], aggfunc=np.max)
max_price_dict = max_price['RawPrice'].to_dict()
print(max_price)

print(max_price_dict[friday_event_id])
print(max_price_dict[saturday_event_id])
print(max_price_dict[sunday_event_id])

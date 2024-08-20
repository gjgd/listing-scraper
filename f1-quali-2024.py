from metrics import meter
from utils import get_concert_prices_callback_by_events

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

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(
        events,
        metadata=metadata,
        quantity=quantity,
        max_price=300
    )],
    name="f1_quali_2024",
    unit="",
)

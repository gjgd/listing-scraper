from metrics import meter
from utils import get_concert_prices_callback_by_events

austin_5pm = 151894031
austin_8pm = 151870859

events = [
    austin_5pm,
    austin_8pm
]

metadata = {
    "event_artist": "John Oliver",
    "event_image":  "https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_1687,w_3000,x_0,y_0/dpr_1.5/c_limit,w_1600/fl_lossy,q_auto/v1557998763/190507-stern-oliver-tease_1_fxn7b9",
    "event_dates": {
        austin_5pm: "Aug 20 • Sun • 5:00PM • 2023",
        austin_8pm: "Aug 20 • Sun • 8:00PM • 2023"
    },
    "event_urls": {
        austin_5pm: "https://www.stubhub.com/john-oliver-austin-tickets-8-20-2023/event/151894031/",
        austin_8pm: "https://www.stubhub.com/john-oliver-austin-tickets-8-20-2023/event/151870859/",
    }
}

quantity = 2

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(events, metadata=metadata, quantity=quantity)],
    name="john_prices",
    unit="",
)

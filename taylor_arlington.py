from metrics import meter
from utils import get_concert_prices_callback_by_events

# https://www.stubhub.com/taylor-swift-arlington-tickets-3-31-2023/event/151219647/
friday_arlington_event_id = 151219647
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-1-2023/event/150593502/
saturday_arlington_event_id = 150593502
# https://www.stubhub.com/taylor-swift-arlington-tickets-4-2-2023/event/150593515/
sunday_arlington_event_id = 150593515

events = [
    friday_arlington_event_id,
    saturday_arlington_event_id,
    sunday_arlington_event_id,
]

metadata = {
    "event_artist": "Taylor Swift",
    "event_image":  "https://media1.popsugar-assets.com/files/thumbor/0ebv7kCHr0T-_O3RfQuBoYmUg1k/475x60:1974x1559/fit-in/500x500/filters:format_auto-!!-:strip_icc-!!-/2019/09/09/023/n/1922398/9f849ffa5d76e13d154137.01128738_/i/Taylor-Swift.jpg",
    "event_dates": {
        friday_arlington_event_id: "Fri Mar 31, Arlington, Texas",
        saturday_arlington_event_id: "Sat Apr 01, Arlington, Texas",
        sunday_arlington_event_id: "Sun Apr 02, Arlington, Texas",
    },
    "event_urls": {
        friday_arlington_event_id: "https://www.stubhub.com/taylor-swift-arlington-tickets-3-31-2023/event/151219647/",
        saturday_arlington_event_id: "https://www.stubhub.com/taylor-swift-arlington-tickets-4-1-2023/event/150593502/",
        sunday_arlington_event_id: "https://www.stubhub.com/taylor-swift-arlington-tickets-4-2-2023/event/150593515/",
    }
}

quantity = 2

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(events, metadata=metadata, quantity=quantity)],
    name="taylor_prices",
    unit="",
)

from metrics import meter
from utils import get_concert_prices_callback_by_events

# https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-28-2023/event/151197002/
santa_clara_friday = 151197002
# https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-29-2023/event/150593663/
santa_clara_saturday = 150593663

events = [
    santa_clara_friday,
    santa_clara_saturday
]

metadata = {
    "event_artist": "Taylor Swift",
    "event_image":  "https://media1.popsugar-assets.com/files/thumbor/0ebv7kCHr0T-_O3RfQuBoYmUg1k/475x60:1974x1559/fit-in/500x500/filters:format_auto-!!-:strip_icc-!!-/2019/09/09/023/n/1922398/9f849ffa5d76e13d154137.01128738_/i/Taylor-Swift.jpg",
    "event_dates": {
        santa_clara_friday: "Fri Jul 28 Santa Clara",
        santa_clara_saturday: "Sat Jul 29 Santa Clara",
    },
    "event_urls": {
        santa_clara_friday: "https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-28-2023/event/151197002/",
        santa_clara_saturday: "https://www.stubhub.com/taylor-swift-santa-clara-tickets-7-29-2023/event/150593663/",
    }
}

quantity = None

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(events, metadata=metadata, quantity=quantity)],
    name="taylor_prices",
    unit="",
)

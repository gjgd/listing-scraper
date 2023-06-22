from metrics import meter
from utils import get_concert_prices_callback_by_events

# https://www.stubhub.com/taylor-swift-seattle-tickets-7-22-2023/event/150593667/
seattle = 150593667

events = [
    seattle,
]

metadata = {
    "event_artist": "Taylor Swift",
    "event_image":  "https://media1.popsugar-assets.com/files/thumbor/0ebv7kCHr0T-_O3RfQuBoYmUg1k/475x60:1974x1559/fit-in/500x500/filters:format_auto-!!-:strip_icc-!!-/2019/09/09/023/n/1922398/9f849ffa5d76e13d154137.01128738_/i/Taylor-Swift.jpg",
    "event_dates": {
        seattle: "Sat Jul 22, Seattle, Washington",
    },
    "event_urls": {
        seattle: "https://www.stubhub.com/taylor-swift-seattle-tickets-7-22-2023/event/150593667/",
    }
}

quantity = None

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(events, metadata=metadata, quantity=quantity)],
    name="taylor_prices",
    unit="",
)

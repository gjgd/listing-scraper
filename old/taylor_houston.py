from cron.metrics import meter
from utils import get_concert_prices_callback_by_events

# https://www.stubhub.com/taylor-swift-houston-tickets-4-21-2023/event/151214693/
friday_houston_event_id = 151214693
# https://www.stubhub.com/taylor-swift-houston-tickets-4-22-2023/event/150593575/
saturday_houston_event_id = 150593575
# https://www.stubhub.com/taylor-swift-houston-tickets-4-23-2023/event/151214704/
sunday_houston_event_id = 151214704

events = [
    friday_houston_event_id,
    saturday_houston_event_id,
    sunday_houston_event_id
]

metadata = {
    "event_artist": "Taylor Swift",
    "event_image":  "https://media1.popsugar-assets.com/files/thumbor/0ebv7kCHr0T-_O3RfQuBoYmUg1k/475x60:1974x1559/fit-in/500x500/filters:format_auto-!!-:strip_icc-!!-/2019/09/09/023/n/1922398/9f849ffa5d76e13d154137.01128738_/i/Taylor-Swift.jpg",
    "event_dates": {
        friday_houston_event_id: "Fri Apr 21, Houston, Texas",
        saturday_houston_event_id: "Sat Apr 22, Houston, Texas",
        sunday_houston_event_id: "Sun Apr 23, Houston, Texas",
    },
    "event_urls": {
        friday_houston_event_id: "https://www.stubhub.com/taylor-swift-houston-tickets-4-21-2023/event/151214693/",
        saturday_houston_event_id: "https://www.stubhub.com/taylor-swift-houston-tickets-4-22-2023/event/150593575/",
        sunday_houston_event_id: "https://www.stubhub.com/taylor-swift-houston-tickets-4-23-2023/event/151214704/",
    }
}

quantity = 2

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(events, metadata=metadata, quantity=quantity)],
    name="taylor_prices",
    unit="",
)

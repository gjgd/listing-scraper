from metrics import meter
from utils import get_concert_prices_callback_by_events

suga = 151473277

events = [
  suga
]

metadata = {
    "event_artist": "Suga",
    "event_image": "https://imageio.forbes.com/specials-images/imageserve/61d3b07749cc228e4b034eaa/BTS-s-Digital-Single--Butter--Release-Press-Conference/0x0.jpg?format=jpg&crop=2474,1854,x0,y80,safe&width=960",
    "event_dates": {
        suga: "Sat Apr 29, Newark, NJ",
    },
    "event_urls": {
        suga: "https://www.stubhub.com/suga-newark-tickets-4-29-2023/event/151473277/"
    }
}

quantity = None

meter.create_observable_counter(
    callbacks=[get_concert_prices_callback_by_events(events, metadata=metadata, quantity=quantity)],
    name="suga_prices",
    unit="",
)

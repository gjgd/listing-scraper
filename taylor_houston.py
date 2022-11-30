from metrics import meter
from taylor import get_taylor_prices_callback_by_events, friday_houston_event_id, saturday_houston_event_id, sunday_houston_event_id

events = [
    friday_houston_event_id,
    saturday_houston_event_id,
    sunday_houston_event_id
]

meter.create_observable_counter(
    callbacks=[get_taylor_prices_callback_by_events(events)],
    name="taylor_prices",
    description="houston",
    unit="",
)

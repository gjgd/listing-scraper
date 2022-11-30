from metrics import meter
from taylor import get_taylor_prices_callback_by_events, friday_event_id, saturday_event_id, sunday_event_id

events = [
    friday_event_id,
    saturday_event_id,
    sunday_event_id,
]

meter.create_observable_counter(
    callbacks=[get_taylor_prices_callback_by_events(events)],
    name="taylor_prices",
    description="arlington",
    unit="",
)

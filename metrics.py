from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.prometheus_remote_write import (
    PrometheusRemoteWriteMetricsExporter,
)
from opentelemetry import metrics
import os
from dotenv import load_dotenv
load_dotenv()

exporter = PrometheusRemoteWriteMetricsExporter(
    endpoint=os.getenv("PROM_REMOTE_WRITE_URL"),
    basic_auth={
        "username": os.getenv("PROM_REMOTE_WRITE_USER"),
        "password": os.getenv("PROM_REMOTE_WRITE_PASSWORD"),
    },
)
reader = PeriodicExportingMetricReader(exporter, 1000)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)

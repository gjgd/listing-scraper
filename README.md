# Taylor scrapper

```
python3 -m venv venv
./venv/bin/pip3 install requests tqdm pandas opentelemetry-exporter-prometheus-remote-write python-dotenv
```

Setup .env
```
PROM_REMOTE_WRITE_URL=
PROM_REMOTE_WRITE_USER=
PROM_REMOTE_WRITE_PASSWORD=
```

Add this to crontab
```

*/2 * * * * /home/gjgd/workspace/taylor-scraper/venv/bin/python /home/gjgd/workspace/taylor-scraper/taylor_arlington.py
*/2 * * * * /home/gjgd/workspace/taylor-scraper/venv/bin/python /home/gjgd/workspace/taylor-scraper/taylor_houston.py
```
./venv/bin/python taylor.py

## Links

- https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/exporter/opentelemetry-exporter-prometheus-remote-write/example/sampleapp.py#L55

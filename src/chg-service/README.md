# REST API service for Change Machine

### Usage:
```
$ make run-local
poetry run uvicorn change_machine_service.api:app --reload
INFO:     Will watch for changes in these directories: ['/Users/a.yushkovskiy/gh/atemate/case-change-machine']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [34193] using WatchFiles
INFO:     Started server process [34197]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
...
```

```
$ curl 'localhost:8000/api/v1/pay?eur_inserted=10&currywurst_price_eur=4.9' | jq
{
  "total_coins": 4,
  "total_eur": 5.1,
  "coins": [
    {
      "count": 2,
      "value": 2,
      "value_in_cents": 200,
      "name": "euro",
      "type": "coin"
    },
    {
      "count": 1,
      "value": 1,
      "value_in_cents": 100,
      "name": "euro",
      "type": "coin"
    },
    {
      "count": 1,
      "value": 10,
      "value_in_cents": 10,
      "name": "cent",
      "type": "coin"
    }
  ]
}
```


### Configuration
See [src/chg-service/change_machine_service/settings.py](src/chg-service/change_machine_service/settings.py), which can be overloaded using environment variables.
For example:
- specify the change-computation algorithm: `export CHG_ALGORITHM="greedy_search"`
- specify
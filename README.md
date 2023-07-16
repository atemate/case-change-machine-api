# case-change-machine
Test task: REST API for money change machine

# Development
- Requirements:
    - Python 3.10 (install via pyenv)
    - Poetry (`pip install -U poetry`)

- Install local dependencies:
```
make install
```

- Run unit tests:
```
make unit-tests
```

- Run in docker-compose:
```
make run-docker
```

In a separate terminal:
```
$ curl 'localhost:3003/pay?eur_inserted=5&currywurst_price_eur=4.9' | jq
[
  {
    "count": 1,
    "value": 10,
    "value_in_cents": 10,
    "name": "cent",
    "type": "coin"
  }
]
```

# nats-streaming-pubsub-py
Try to subscribe &amp; publish through nats-streaming

1. Run nats-streaming server. Use [here](https://hub.docker.com/_/nats-streaming)

```
docker pull nats-streaming:latest
```

```
docker run -p 4222:4222  nats-streaming -p 4222
```


2. Start Sub

```
python nats-sub.py
```

In starting subscribe, The server's logs is below.

```
[1] 2021/07/02 03:18:50.093259 [INF] STREAM: Channel "hoge.topic" has been created
```

3. Publish message.

```
python nats-pub.py
```



Received below.

```
Received message! seq: 1 data: b'hoge'
Received message! seq: 2 data: b'hoge'
Received message! seq: 3 data: b'hoge'
Received message! seq: 4 data: b'hoge'
Received message! seq: 5 data: b'hoge'
Received message! seq: 6 data: b'hoge'
Received message! seq: 7 data: b'hoge'
Received message! seq: 8 data: b'hoge'
Received message! seq: 9 data: b'hoge'
Received message! seq: 10 data: b'hoge'
```

4. Stop Sub

Press `Ctrl + C` .


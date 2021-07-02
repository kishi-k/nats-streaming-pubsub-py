import asyncio
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN

CLUSTER_ID = "test-cluster"
CLIENT_ID = "test_sub"
TPIC_NAME = "hoge.topic"

async def run(loop, feture):
    nc = NATS()
    sc = STAN()

    await nc.connect("nats://127.0.0.1:4222", loop=loop)
    await sc.connect(CLUSTER_ID, CLIENT_ID, nats=nc)
    print('connected nats.')

    async def cb(msg):
        print(f"Received message! seq: {msg.seq} data: {msg.data}")

    sub = await sc.subscribe(TPIC_NAME, start_at='new_only', cb=cb)
    
    await asyncio.wait([feture])
   
    await sub.unsubscribe()
    await sc.close()
    await nc.close()

    return

async def close(main_f):
    print('closing')
    await asyncio.sleep(1)
   
    # Run loop until tasks done:
    return asyncio.gather(main_f)
   

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    stop_feture = loop.create_future()
    
    try:
        main_f = asyncio.ensure_future(run(loop, stop_feture))
        loop.run_forever()

    except KeyboardInterrupt :
        pass

    finally:
        stop_feture.set_result(None)
        loop.run_until_complete(close(main_f))
    loop.close()
    print('closed')
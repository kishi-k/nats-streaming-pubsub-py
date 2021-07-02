import asyncio
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN


CLUSTER_ID = "test-cluster"
CLIENT_ID = "test_pub"
TPIC_NAME = "hoge.topic"



async def run(loop):
    nc = NATS()
    sc = STAN()

    await nc.connect("nats://127.0.0.1:4222", loop=loop)
    await sc.connect(CLUSTER_ID, CLIENT_ID, nats=nc)

    print('connected')


    ## publish
    async def ack_handler(msg):
        print(f'Received ack: {msg}')
        #something received ack meassage

    for i in range(10):
        await sc.publish(TPIC_NAME, b'hoge', ack_handler=ack_handler)

    await sc.close()
    await nc.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()


# pynacos-sdk

## Tutorial
``` python
from nacos import Nacos
from nacos.errors import RequestError
from nacos.params import ServiceRegisterParam, ServiceListParam


NACOS_HOST = "127.0.0.1"
NACOS_PORT = 8848
NAMESPACE_ID = "e26e7439-e161-4709-8778-ab5ecef5fec5"

nacos = Nacos(NACOS_HOST, NACOS_PORT, NAMESPACE_ID)

try:
    param = ServiceRegisterParam("hello")
    status = nacos.service_register(param)
    print("register status = ", status)
except RequestError as e:
    print(e)

try:
    param = ServiceListParam()
    services = nacos.service_list(param)
    print(services.json())
except RequestError as e:
    print(e)
```

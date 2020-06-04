# pynacos-sdk

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7578f591597d48349f116893af440a7e)](https://app.codacy.com/manual/olivetree123/pynacos-sdk?utm_source=github.com&utm_medium=referral&utm_content=olivetree123/pynacos-sdk&utm_campaign=Badge_Grade_Dashboard)

## Tutorial
``` python
from nacos import Nacos
from nacos.errors import RequestError, ParamError
from nacos.params import ServiceRegisterParam, ServiceListParam


NACOS_HOST = "127.0.0.1"
NACOS_PORT = 8848
NAMESPACE_ID = "e26e7439-e161-4709-8778-ab5ecef5fec5"

nacos = Nacos(NACOS_HOST, NACOS_PORT, NAMESPACE_ID)

try:
    param = ServiceRegisterParam("hello")
    status = nacos.service_register(param)
    print("register status = ", status)
except ParamError as e:
    print("param error")
    print(e)
except RequestError as e:
    print("nacos error")
    print(e)

try:
    param = ServiceListParam()
    services = nacos.service_list(param)
    print(services.json())
except ParamError as e:
    print("param error")
    print(e)
except RequestError as e:
    print("nacos error")
    print(e)
```


import json
import random
from typing import List

from openai import AzureOpenAI

API_VERSION = "2023-12-01-preview"


class Deployment:
    GPT35 = "gpt-35-turbo"
    GPT35_16K = "gpt-35-turbo-16k"
    GPT4_32K = "gpt-4-32k"
    GPT4V = "gpt-4-vision-preview"
    GPT4O = "gpt-4o"



class ModelName:
    GPT4P = "gpt-4-1106-preview"
    GPT4 = "gpt-4"
    GPT4_32K = "gpt-4-32k"
    GPT35 = "gpt-3.5-turbo"
    GPT35_16K = "gpt-3.5-turbo-16k"
    GPT4V = "gpt-4-vision-preview"
    GPT4O = "gpt-4o"


class ModelVersion:
    V1106P = "1106-Preview"
    V0613 = "0613"
    V1106 = "1106"
    GPT4V = "vision-preview"
    V0513 = "2024-05-13"


class Resource:
    def __init__(self, key, endpoint):
        self.key = key
        self.endpoint = endpoint

GPT02 = Resource(key="replace with respective openai api key", endpoint="https://gptforai02.openai.azure.com/")
GPT01 = Resource(key="replace with respective openai api key", endpoint="https://gptforai01.openai.azure.com/")
GPT03 = Resource(key="replace with respective openai api key", endpoint="https://gptforai03.openai.azure.com/")
GPT04 = Resource(key="replace with respective openai api key", endpoint="https://gptforai04.openai.azure.com/")
GPT05 = Resource(key="replace with respective openai api key", endpoint="https://gptforai05.openai.azure.com/")
GPT11 = Resource(key="replace with respective openai api key", endpoint="https://gptforai11.openai.azure.com/")


class ENVariable:
    def __init__(self, resource: Resource, model_name: str, deployment: str, model_version: str, match_name: str=None):
        self.resource = resource
        self.model_name = model_name  # model_name与采购时的设定有关，不一定完全与模型名一致
        self.deployment = deployment
        self.model_version = model_version
        self.match_name = match_name or self.model_name

    @property
    def key(self):
        return self.resource.key

    @property
    def endpoint(self):
        return self.resource.endpoint

    def __repr__(self):
        return self.dump()

    def __str__(self):
        return self.dump()

    def to_json(self):
        return {
            "endpoint": self.endpoint,
            "model_name": self.model_name,
            "model_version": self.model_version,
            "deployment": self.deployment
        }

    def dump(self):
        return json.dumps(self.to_json(), ensure_ascii=False)


variables: List[ENVariable] = [
    ENVariable(resource=GPT01, model_name=ModelName.GPT35, deployment=Deployment.GPT35,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT01, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT01, model_name=ModelName.GPT4O, deployment=Deployment.GPT4O,
               model_version=ModelVersion.V0513),
    ENVariable(resource=GPT02, model_name=ModelName.GPT35, deployment=Deployment.GPT35,
               model_version=ModelVersion.V1106),
    ENVariable(resource=GPT02, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT02, model_name=ModelName.GPT4_32K, deployment=Deployment.GPT4_32K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT03, model_name=ModelName.GPT35, deployment=Deployment.GPT35,
               model_version=ModelVersion.V1106),
    ENVariable(resource=GPT03, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT03, model_name=ModelName.GPT4_32K, deployment=Deployment.GPT4_32K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT04, model_name=ModelName.GPT35, deployment=Deployment.GPT35,
               model_version=ModelVersion.V1106),
    ENVariable(resource=GPT04, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT05, model_name=ModelName.GPT4_32K, deployment=Deployment.GPT4_32K,
               model_version=ModelVersion.V0613),
    ENVariable(resource=GPT11, model_name=ModelName.GPT4, deployment=Deployment.GPT4V, model_version=ModelVersion.GPT4V,
               match_name=ModelName.GPT4V)
]


class ENVManager:
    def __init__(self):
        self.variables: List[ENVariable] = [
            ENVariable(resource=GPT01, model_name=ModelName.GPT35, deployment=Deployment.GPT35, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT01, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT02, model_name=ModelName.GPT35, deployment=Deployment.GPT35, model_version=ModelVersion.V1106),
            ENVariable(resource=GPT02, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT02, model_name=ModelName.GPT4_32K, deployment=Deployment.GPT4_32K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT03, model_name=ModelName.GPT35, deployment=Deployment.GPT35, model_version=ModelVersion.V1106),
            ENVariable(resource=GPT03, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT03, model_name=ModelName.GPT4_32K, deployment=Deployment.GPT4_32K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT04, model_name=ModelName.GPT35, deployment=Deployment.GPT35, model_version=ModelVersion.V1106),
            ENVariable(resource=GPT04, model_name=ModelName.GPT35_16K, deployment=Deployment.GPT35_16K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT05, model_name=ModelName.GPT4_32K, deployment=Deployment.GPT4_32K, model_version=ModelVersion.V0613),
            ENVariable(resource=GPT11, model_name=ModelName.GPT4, deployment=Deployment.GPT4V, model_version=ModelVersion.GPT4V)
        ]

        self.default_model_map = {
            'gpt-3.5-turbo': 'gpt-3.5-turbo-0613',
            'gpt-3.5-turbo-16k': 'gpt-3.5-turbo-16k-0613',
            'gpt-4': 'gpt-4-1106-preview',
            'gpt-4-0314': 'gpt-4-1106-preview',
            'gpt-4-32k': 'gpt-4-32k-0613',
            'gpt-4-32k-0314': 'gpt-4-32k-0613'
        }

    def _get_model_type(self, model_name: str):
        return '-'.join(model_name.split('-')[:2])

    def _get_context(self, model_name: str):
        if '16k' in model_name:
            return '16k'
        elif '32k' in model_name:
            return '32k'
        else:
            return None

    def _get_version(self, model_name: str):
        if '1106-preview' in model_name:
            return '1106-preview'
        if '1106' in model_name:
            return '1106'
        if '0613' in model_name:
            return '0613'
        if '0301' in model_name:
            return '0613'
        if 'vision-preview' in model_name:
            return 'vision-preview'
        return None

    def _match(self, variable: ENVariable, model_name: str) -> bool:
        if variable.match_name == model_name:
            return True
        if self._get_model_type(variable.model_name) != self._get_model_type(model_name):
            return False
        if self._get_context(variable.model_name) != self._get_context(model_name):
            return False
        md_v = self._get_version(model_name)
        if md_v is not None:
            if md_v != variable.model_version.lower():
                return False
        return True

    def get_environment(self, model_name: str) -> ENVariable:

        model_name = self.default_model_map.get(model_name, model_name)
        ret = []
        for variable in self.variables:
            if self._match(variable, model_name):
                ret.append(variable)
        if ret:
            return random.choice(ret)
        raise Exception


env_manager = ENVManager()


def chat(messages: List, model: str, **kwargs):
    env = env_manager.get_environment(model)
    #logger.info(f'[chat]: {model} env: {env}')
    with AzureOpenAI(api_key=env.key, azure_endpoint=env.endpoint, api_version=API_VERSION) as openai_client:
        args_keys = list(kwargs.keys())
        for key in args_keys:
            if kwargs[key] is None:
                del kwargs[key]
        if 'api-key' in kwargs:
            del kwargs['api-key']

        response = openai_client.chat.completions.create(model=env.deployment, messages=messages, **kwargs)
        res_jd = json.loads(response.model_dump_json(indent=2))
        return res_jd


def chat_stream(messages: List, model: str, **kwargs):
    env = env_manager.get_environment(model)
    with AzureOpenAI(api_key=env.key, azure_endpoint=env.endpoint, api_version=API_VERSION) as openai_client:
        if 'model' in kwargs:
            del kwargs['model']
        for data in openai_client.chat.completions.create(messages=messages, stream=True, model=env.deployment, **kwargs):
            if data is not None:
                jd = data.model_dump()
                jd_wrap = {'status': '000000', 'desc': 'success', 'detail': jd, 'traceId': None}
                json_str = json.dumps(jd_wrap, ensure_ascii=False)
                data_wrap = f"data: {json_str}\n\n"
                data_wrap_bytes = data_wrap.encode('utf-8')
                yield data_wrap_bytes
        yield "data: [DONE]".encode('utf-8')
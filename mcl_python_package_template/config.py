import pydantic
import yaml


class Config(pydantic.BaseModel):
    foo: str
    bar: int

    @classmethod
    def from_yaml(cls, yaml_file):
        with open(yaml_file, "r") as f:
            return cls(**yaml.safe_load(f))


config = Config.from_yaml("config.yaml")

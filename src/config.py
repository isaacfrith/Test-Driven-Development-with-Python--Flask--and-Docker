class BaseConfig:
    TESTING = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TEST = True

class ProductionConfig(BaseConfig):
    pass


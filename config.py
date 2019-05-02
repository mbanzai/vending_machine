

class Config(object):
    """
    Common configurations
    """
    LOG_FILENAME = 'app.log'
    DEBUG = True
    bank = {}

    # Accepted values for coins,
    # 50 is 50 pence, 100 is one pound, 200 is two pounds
    coins = ("1", "2", "5", "10", "20", "50", "100", "200")

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    LOG_FILENAME = 'app.log'


class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True


app_config = {
    'production': ProductionConfig,
    'testing': TestingConfig
}
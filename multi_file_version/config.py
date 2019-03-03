# import os
#
# class Config(object):
#     """
#     Common configurations
#     """
#
#     # Put any configurations here that are common across all environments
#     SQLALCHEMY_DATABASE_URI = 'postgres://jxxblesrascyio:a447ed84172575a035b9fa57af3f819f0c1163fe46da6c3469f110293e0412f1@ec2-54-243-223-245.compute-1.amazonaws.com:5432/d37d890uhbs9gv'
#     #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     print("Database URL configured as:", SQLALCHEMY_DATABASE_URI)
#
#
# class DevelopmentConfig(Config):
#     """
#     Development configurations
#     """
#
#     DEBUG = True
#     SQLALCHEMY_ECHO = False
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
# class ProductionConfig(Config):
#     """
#     Production configurations
#     """
#
#     DEBUG = False
#
#
# app_config = {
#     'development': DevelopmentConfig,
#     'production': ProductionConfig
# }

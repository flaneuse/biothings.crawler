''' Biothings API Web Config '''

import os

from biothings.web.api.es.handlers import QueryHandler
from biothings.web.settings.default import *

from web.query_builder import MPQueryBuilder
from web.query_transformer import MPResultTransformer

# *****************************************************************************
# Elasticsearch
# *****************************************************************************
ES_DOC_TYPE = '_doc'
ES_HOST = os.getenv("ES_HOST", 'localhost:9200')
ES_INDEX = os.getenv('ES_INDEX', '_all')  # query endpoint

# *****************************************************************************
# Tornado URL Patterns
# *****************************************************************************
APP_LIST = [
    (r"/api/query/?", QueryHandler),
]

# *****************************************************************************
# Biothings SDK Settings
# *****************************************************************************
ES_QUERY_BUILDER = MPQueryBuilder
ES_RESULT_TRANSFORMER = MPResultTransformer
ALLOW_RANDOM_QUERY = True

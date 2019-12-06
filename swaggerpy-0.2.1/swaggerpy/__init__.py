#
# Copyright (c) 2013, Digium, Inc.
#

"""Swagger processing libraries.

More information on Swagger can be found `on the Swagger website
<https://developers.helloreverb.com/swagger/>`
"""

__all__ = ["client", "codegen", "processors", "swagger_model"]

# from swagger_model import load_file, load_json, load_url, Loader  # python 2.7
from swaggerpy.swagger_model import load_file, load_json, load_url, Loader  # python 3.7
# from processors import SwaggerProcessor, SwaggerError  # python 2.7
from swaggerpy.processors import SwaggerProcessor, SwaggerError  # python 3.7

import json

import allure
from allure_commons.types import AttachmentType
from loguru import logger


class Helper:
    """
    Helper class for logging and attaching request/response
    """
    @staticmethod
    def attach_response(response):
        """
        Attach response to allure report
        """
        response = json.dumps(response, indent=4)
        allure.attach(body=response, name="API Response", attachment_type=AttachmentType.JSON)

    @staticmethod
    def log(response, request_body=None):
        """
        Logging methode
        """
        logger.info(f"REQUEST METHOD: {response.request.method}")
        logger.info(f"REQUEST URL: {response.url}")
        logger.info(f"REQUEST HEADERS: {response.request.headers}")
        logger.info(f"REQUEST BODY: {request_body}")
        logger.info(f"STATUS CODE: {response.status_code}")
        logger.info(f"RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms")
        logger.info(f"RESPONSE HEADERS: {response.headers}")
        logger.info(f"RESPONSE BODY: {response.text}")

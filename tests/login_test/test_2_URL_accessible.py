import logging

from pages.login_page import LoginPage

logger = logging.getLogger(__name__)


def test_verify_home_url_is_accessible(page):
    lp = LoginPage(page)
    lp.open_url()

    assert lp.is_login_page_loaded(), "HomePage not Loaded"
    logger.info("Homepage url loaded successfully")

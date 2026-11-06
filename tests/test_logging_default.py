import logging

from flag_gems.logging_utils import configure_default_logging


def test_default_logging_is_info_with_debug_opt_in(monkeypatch):
    logger = logging.getLogger("flag_gems")
    previous = logger.level
    try:
        monkeypatch.delenv("FLAGGEMS_LOG_LEVEL", raising=False)
        configure_default_logging()
        assert logger.level == logging.INFO

        monkeypatch.setenv("FLAGGEMS_LOG_LEVEL", "DEBUG")
        configure_default_logging()
        assert logger.level == logging.DEBUG
    finally:
        logger.setLevel(previous)

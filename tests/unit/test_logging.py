import os
import sys
import logging
import tempfile

# Add src to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.utils.logging import setup_logger

def test_setup_logger_default_level():
    logger = setup_logger('test')
    assert logger.level == logging.INFO
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)

def test_setup_logger_custom_level():
    logger = setup_logger('test', logging.DEBUG)
    assert logger.level == logging.DEBUG

def test_setup_logger_env_level():
    os.environ['TARDIS_LOG_LEVEL'] = 'DEBUG'
    logger = setup_logger('test_env')
    assert logger.level == logging.DEBUG
    os.environ.pop('TARDIS_LOG_LEVEL', None)

def test_setup_logger_with_file():
    with tempfile.NamedTemporaryFile() as temp_file:
        logger = setup_logger('test_file', log_file=temp_file.name)
        test_message = "Test log message"
        logger.info(test_message)
        
        # Verify file content
        with open(temp_file.name, 'r') as f:
            log_content = f.read()
            assert test_message in log_content
            assert 'test_file' in log_content
            assert 'INFO' in log_content 
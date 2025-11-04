from loguru import logger

logger.add(
    'info.log',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
    level="INFO",
    rotation="10 MB",
    retention="30 days"
)


def main():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")


if __name__ == "__main__":
    main()



from loguru import logger


def division(a, b):
    return a / b


@logger.catch
def nested(c):
    division(1, c)


if __name__ == "__main__":
    nested(0)



**************************
from loguru import logger
from functools import wraps

def log(func):
    """
    A decorator function to log information about function calls and their results.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        The wrapper function that logs function calls and their results.
        """
        logging.info(f"Running {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Finished {func.__name__} with result: {result}")
        
        except Exception as e:
            logging.error(f"Error occurred in {func.__name__}: {e}")
            raise
        
        else:
            return result

    return wrapper

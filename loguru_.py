from loguru import logger

logger.add(
    'info.log',
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {module}:{function}:{line} - {message}",
    level="INFO",
    colorize=True
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

'''
Customizing Loguru
When using Python's logging module, you'll need to create custom handlers, formatters, and filters to customize a logger's formatting and output. Loguru simplifies this process by only using its add() method, which takes the following parameters:

sink: specifies a destination for each record produced bu the logger. By default, it is set to sys.stderr.
level: specifies the minimum log level for the logger.
format: useful for defining a custom format for your logs.
filter: used to determine whether a record should be logged or not.
colorize: takes a boolean value and determines whether or not terminal colorization should be enabled.
serialize: causes the log record to be presented in JSON format if set to True.
backtrace: determines whether the exception trace should extend beyond the point where the error is captured, making it easier to debug.
diagnose: determines whether the variable values should be displayed in the exception trace. You should set it to False in the production environment to avoid leaking sensitive information.
enqueue: enabling this option places the log records in a queue to avoid conflicts when multiple processes are logging to the same destination.
catch: if an unexpected error happens when logging to the specified sink, you can catch that error by setting this option to True. The error will be printed to the standard error.


from loguru import logger
import sys

logger.remove(0)
logger.add(sys.stderr, level="INFO")

logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")




logger.add(sys.stderr, format="{time:MMMM D, YYYY > HH:mm:ss} | {level} | {message}")

When sink is pointing to a file, the add() method provides a few more options for customizing how the log file should be handled:

rotation: specifies a condition in which the current log file will be closed and a new file will be created. This condition can be an int, datetime or str, and str is recommended since it is more human-readable.
retention: specifies how log each log file will be retained before it is deleted from the filesystem.
compression: the log file will be converted to the specified compression format if this option is set.
delay: if set to True, the creation of a new log file will be delayed until the first log message is pushed.
mode, buffering, encoding: These parameters will be passed to Python's open() function which determines how Python will open the log files.
When rotation has an int value, it corresponds to the maximum number of bytes the current file is allowed to hold before a new one is created. When it has a datetime.timedelta value, it indicates the frequency of each rotation, while datetime.time specifies the time of the day each rotation should occur. And finally, rotation can also take a str value, which is the human-friendly variant of the aforementioned types.


'''
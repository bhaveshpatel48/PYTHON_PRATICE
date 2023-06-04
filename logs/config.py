# Create a dictionary with logger settings
LOGGER_SETTINGS = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'colored',
            'stream': 'ext://sys.stdout'
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console']
    },
    'formatters': {
        'colored': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(asctime)s - %(name)s - %(log_color)s%(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'log_colors': {
                'DEBUG': 'blue',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_yellow',
            }
        }
    }
}

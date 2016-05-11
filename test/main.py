import logging

logging.basicConfig(level=logging.INFO)


def log(sql, args=()):
    logging.info('SQL: %s' % sql)


logging.debug("fvawfew")

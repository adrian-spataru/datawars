import logging
from db import db

logger = logging.getLogger(__name__)


def save_record(record):
    try:
        db.session.add(record)
        db.session.commit()
    except Exception as err:
        logger.error(err)

def delete_record(record):
    try:
        db.session.delete(record)
        db.session.commit()
    except Exception as err:
        logger.error(err)

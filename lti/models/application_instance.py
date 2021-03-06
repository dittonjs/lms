import sqlalchemy as sa
import secrets
from sqlalchemy.orm import relationship
from lti.db import BASE

# TODO we should figure out a more standard place to set this
lti_key = "Hypothesis"

class ApplicationInstance(BASE):
    """Class to represent a single lti install"""

    __tablename__ = 'application_instances'

    id = sa.Column(sa.Integer, autoincrement=True, primary_key=True)
    consumer_key = sa.Column(sa.String)
    shared_secret = sa.Column(sa.String)
    lms_url = sa.Column(sa.String(2048))

    def config_xml():
        pass

    def __repr__(self):
      return str.format("id: {}, consumer_key: {}, lms_url: {}", self.id,
               self.consumer_key, self.lms_url)

def build_shared_secret():
    return secrets.token_hex(64)

def build_unique_key():
  return lti_key + secrets.token_hex(16)

def build_from_lms_url(lms_url):
    return ApplicationInstance(
      consumer_key=build_unique_key(),
      shared_secret=build_shared_secret(),
      lms_url=lms_url
    )

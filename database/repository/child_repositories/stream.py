from sqlalchemy.orm import Session, class_mapper

from database.models import Stream


class StreamRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        stream = Stream(name=name)
        self.session.add(stream)
        self.session.flush()

    def bulk_create(self, streams_data):
        self.session.bulk_insert_mappings(class_mapper(Stream), streams_data)
        self.session.flush()
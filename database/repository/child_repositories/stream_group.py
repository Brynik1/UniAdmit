from sqlalchemy.orm import Session, class_mapper

from database.models import StudyGroup,StreamGroup


class StreamGroupRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, group_id: int, stream_id: int):
        stream_group = StreamGroup(group_id=group_id, stream_id=stream_id)
        self.session.add(stream_group)
        self.session.flush()

    def bulk_create(self, stream_groups_data):
        self.session.bulk_insert_mappings(class_mapper(StreamGroup), stream_groups_data)
        self.session.flush()

    def get_count(self):
        return self.session.query(StudyGroup).count()
from project.db import BaseEntity, db
from project.models import UserEntity, LogEntity, ThreadEntity, BugEntity, CommentEntity

BaseEntity.metadata.create_all(bind=db)
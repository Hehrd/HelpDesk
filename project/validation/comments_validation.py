from project.error.comment_not_found_exception import CommentNotFoundException


def validate_comment(comment):
    if comment is None:
        raise CommentNotFoundException("Comment not found")


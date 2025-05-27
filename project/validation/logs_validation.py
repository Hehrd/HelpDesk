from project.error.log_not_found_exception import LogNotFoundException


def validate_log(log):
    if log is None:
        raise LogNotFoundException()
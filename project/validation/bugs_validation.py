from project.error.bug_not_found_exception import BugNotFoundException


def validate_bug(bug):
    if bug is None:
        raise BugNotFoundException("Bug not found!")



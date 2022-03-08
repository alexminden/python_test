def get_coordinate(record):
    """
    get coordinate
    """
    return record[-1]
def convert_coordinate(coordinate):
    """
    convert coordinate
    """
    return tuple(coordinate)
def compare_records(azara_record, rui_record):
    """
    compare records
    """
    return tuple(azara_record[1]) in rui_record
def create_record(azara_record, rui_record):
    """
    create record
    """
    return sum((azara_record, rui_record), ()) if compare_records(azara_record, rui_record) is True else "not a match"
def clean_up(combined_record_group):
    """
    clean up
    """
    combined_records = tuple(tuple([i[0]])+i[2:] for i in combined_record_group)
    report = "\n".join(str(record) for record in combined_records) + "\n"
    return report
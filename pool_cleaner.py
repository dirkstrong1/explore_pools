import json


def parse_row(row, fields):
    """Returns a well-formed JSON row containing interesting fields."""
    output = {}
    for index, field_name in fields.items():
        output[field_name] = row[index]
    return output


def main():
    """Clean the pools data."""
    #TODO(Miles): accept input/output filenames as command line arguments
    with open('pools.json') as f:
        raw_data = json.load(f)
    data = raw_data['data']
    fields = {
        10: 'name',
        11: 'address',
        12: 'city',
        13: 'zip',
        14: 'phone'
    }
    clean_data = [parse_row(row, fields) for row in data]
    with open('pools_clean.json', 'w') as f:
        json.dump(clean_data, f)


if __name__ == "__main__":
    main()

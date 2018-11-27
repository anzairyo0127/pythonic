import json
UNDEFINED = object()


def divide_json(path):
    handle = open(path, 'r+')  # IOError起こすかも
    try:
        data = open(path, 'r+')  # UnicodeDecodeErrorを起こすかも
        op = json.loads(data)  # ValueErrorを起こすかも
        value = (
            op['numerator'] /
            op['denominator'])

    except ZeroDivisionError as e:
        raise UNDEFINED

    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return value
    finally:
        handle.close()

import json

import pytest

@pytest.mark.test1
def jsonfile(filepath)
 with open(filepath) as f:
    formatteddate=json.load(f)
    return formatteddate
from typing import Dict

from oaipmh.data.oai_errors import OAIBadArgument
from oaipmh.data.oai_properties import OAIParams
from oaipmh.serializers.output_formats import Response


def get_record(params: Dict[str, str]) -> Response:
    """used to get data on a particular record in a particular metadata format"""

    # get parameters
    expected_params={OAIParams.ID, OAIParams.META_PREFIX, OAIParams.VERB}
    if set(params.keys()) != expected_params:
        raise OAIBadArgument
    identifier=params[OAIParams.ID]
    meta_type=params[OAIParams.META_PREFIX]

    #TODO rest of function

    return "<a>b</a>", 200, {}

def list_records(params: Dict[str, str]) -> Response:
    """used to harvest records from a repository with support for selective harvesting"""

    token=None
    #get parameters
    given_params=set(params.keys())
    if OAIParams.RES_TOKEN in given_params:
        if given_params != {OAIParams.RES_TOKEN, OAIParams.VERB}: #resumption token is exclusive
            raise OAIBadArgument
        token=params[OAIParams.RES_TOKEN]
    else:
        if OAIParams.META_PREFIX not in given_params:
            raise OAIBadArgument
        allowed_params={OAIParams.VERB,OAIParams.META_PREFIX, OAIParams.FROM, OAIParams.UNTIL, OAIParams.SET }
        if given_params-allowed_params: #no extra keys allowed
            raise OAIBadArgument

        meta_type=params[OAIParams.META_PREFIX]
        from_str=params.get(OAIParams.FROM)
        until_str=params.get(OAIParams.UNTIL)
        set_str=params.get(OAIParams.SET)
    #TODO rest of function

    return "<a>b</a>", 200, {}

def list_identifiers(params: Dict[str, str]) -> Response:
    """retrieves headers of all records matching certain parameters"""
    token=None

    #get parameters
    given_params=set(params.keys())
    if OAIParams.RES_TOKEN in given_params:
        if given_params != {OAIParams.RES_TOKEN, OAIParams.VERB}: #resumption token is exclusive
            raise OAIBadArgument
        token=params[OAIParams.RES_TOKEN]
    else:
        if OAIParams.META_PREFIX not in given_params:
            raise OAIBadArgument
        allowed_params={OAIParams.VERB,OAIParams.META_PREFIX, OAIParams.FROM, OAIParams.UNTIL, OAIParams.SET }
        if given_params-allowed_params: #no extra keys allowed
            raise OAIBadArgument

        meta_type=params[OAIParams.META_PREFIX]
        from_str=params.get(OAIParams.FROM)
        until_str=params.get(OAIParams.UNTIL)
        set_str=params.get(OAIParams.SET)

    #TODO rest of function
        
    return "<a>b</a>", 200, {}

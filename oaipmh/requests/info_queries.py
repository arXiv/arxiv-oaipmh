from typing import Dict

from oaipmh.data.oai_errors import OAIBadArgument
from oaipmh.data.oai_properties import OAIParams, OAIVerbs
from oaipmh.serializers.output_formats import Response
from oaipmh.processors.create_set_list import produce_set_list
from oaipmh.requests.param_processing import process_identifier

def identify(params: Dict[str, str]) -> Response:
    """used to retrieve information about the repository"""
    query_data: Dict[OAIParams, str]={OAIParams.VERB : OAIVerbs.IDENTIFY}
    if set(params.keys()) != {OAIParams.VERB}:
        raise OAIBadArgument

    #TODO 
    return "<a>b</a>", 200, {}

def list_metadata_formats(params: Dict[str, str]) -> Response:
    """used to retrieve the metadata formats available from a repository.
    An optional argument restricts the request to the formats available for a specific item.
    """
    query_data: Dict[OAIParams, str]={OAIParams.VERB : OAIVerbs.LIST_META_FORMATS}

    given_params=set(params.keys())
    if OAIParams.ID in given_params: #give formats for one item
        if given_params != {OAIParams.VERB, OAIParams.ID}:
            raise OAIBadArgument
        
        identifier_str=params[OAIParams.ID]
        arxiv_id=process_identifier(identifier_str)
        query_data[OAIParams.ID]=identifier_str

        #TODO get formats for an item
        return "<a>b</a>", 200, {}

    else: #give formats repository supports
        if given_params != {OAIParams.VERB}:
            raise OAIBadArgument
        #TODO get formats for repository
        return "<a>b</a>", 200, {}

def list_sets(params: Dict[str, str]) -> Response:
    """used to retrieve the set structure of a repository"""

    query_data: Dict[OAIParams, str]={OAIParams.VERB:OAIVerbs.LIST_SETS}
    given_params=set(params.keys())
    if OAIParams.RES_TOKEN in given_params:
        if given_params != {OAIParams.RES_TOKEN, OAIParams.VERB}: #resumption token is exclusive
            raise OAIBadArgument
        token_str=params[OAIParams.RES_TOKEN]
        #TODO token validation/processing
        query_data[OAIParams.RES_TOKEN]=token_str
        #TODO will we ever hit this, or will we always return our set structure in full?
    else:
        if given_params != {OAIParams.VERB}: 
            raise OAIBadArgument

    return produce_set_list(query_data)


from datetime import datetime

from arxiv.taxonomy.definitions import CATEGORIES

from oaipmh.serializers.create_records import Header, dcRecord, arXivRawRecord, arXivRecord, arXivOldRecord

def test_create_header():
    date= datetime(2010,1,1)
    header=Header("1234.5678",date, [CATEGORIES['hep-lat'], CATEGORIES['math.GN'] ] )
    assert header.date == date
    assert header.id=="oai:arXiv.org:1234.5678"
    assert header.sets==['physics:hep-lat', 'math:math:GN']

def test_create_arXivRecord(metadata_object2):
    record=arXivRecord(metadata_object2)
    assert record.categories==[CATEGORIES['cs.AI'], CATEGORIES['hep-lat']]
    assert record.current_meta==metadata_object2
    assert record.header==Header("1234.56789", datetime(2023,3,1,15,7,8), [CATEGORIES['cs.AI'], CATEGORIES['hep-lat']])
    assert record.authors==[['Doe', 'John', ''], ['Smith', 'Jane', '']]

def test_create_arXivRawRecord(metadata_object1, metadata_object2):
    record=arXivRawRecord([metadata_object1, metadata_object2])
    assert record.categories==[CATEGORIES['cs.AI'], CATEGORIES['hep-lat']]
    assert record.current_meta==metadata_object2
    assert record.header==Header("1234.56789", datetime(2023,3,1,15,7,8), [CATEGORIES['cs.AI'], CATEGORIES['hep-lat']])
    assert record.versions[0].version==1
    assert record.versions[0].submitted_date==datetime(2023,1,1,10,3,6)
    assert record.versions[0].size_kilobytes==1
    assert record.versions[0].source_flag==None
    assert record.versions[0].source_format=="pdf"
    assert record.versions[1].version==2
    assert record.versions[1].submitted_date==datetime(2023,2,1,10,3,6)
    assert record.versions[1].size_kilobytes==2
    assert record.versions[1].source_flag==None
    assert record.versions[1].source_format=="pdf"

def test_create_arXivOldRecord(metadata_object2):
    record=arXivOldRecord(metadata_object2)
    assert record.categories==[CATEGORIES['cs.AI'], CATEGORIES['hep-lat']]
    assert record.current_meta==metadata_object2
    assert record.header==Header("1234.56789", datetime(2023,3,1,15,7,8), [CATEGORIES['cs.AI'], CATEGORIES['hep-lat']])

def test_create_dcRecord(metadata_object1, metadata_object2):
    record=dcRecord([metadata_object1, metadata_object2])
    assert record.categories==[CATEGORIES['cs.AI'], CATEGORIES['hep-lat']]
    assert record.current_meta==metadata_object2
    assert record.header==Header("1234.56789", datetime(2023,3,1,15,7,8), [CATEGORIES['cs.AI'], CATEGORIES['hep-lat']])
    assert record.current_version_date==datetime(2023,2,1,10,3,6)
    assert record.initial_date==datetime(2023,1,1,10,3,6)

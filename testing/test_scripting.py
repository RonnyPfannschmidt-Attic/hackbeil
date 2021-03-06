from hackbeil.branchreplay import BranchReplay
from hackbeil.scripting.convert import convert_all
from mock import Mock

def test_convert():

    replay = BranchReplay.from_json({
        'rev':200,
        'tag_prefixes':[],
        'required_path': None,
        'history': [
            {
                'path': 'trunk',
                'start': 1,
                'end': None,
                'changesets': [2,3,4],
                'source_branch': None,
                'source_rev': None,
            },
            {
                'path': 'branch/test',
                'start': 5,
                'end': None,
                'changesets': [ 6,7],
                'source_branch': 'trunk',
                'source_rev': 4,
            },
        ],
    })

    mock = Mock()

    convert_all(mock.ui, replay, mock.convert, 'test', 'test')
    assert mock.convert.call_count==2


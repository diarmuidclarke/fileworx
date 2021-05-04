"""
Extract file meta data

For a set of supported file types
- extract meta data from Windows File System attributes
- MS Office metadata - e.g. custom XML
- MS Office document content - e.g. structured information from the front page of a report
"""



def get_file_meta(filepath):
    filemeta = {}

    # fake it for now
    filemeta['series'] = 'J301'
    filemeta['id'] = '0294'
    filemeta['issue'] = '4'
    filemeta['title'] = 'Thoughts on Inter-Dimensional Transposition of Key Staff'
    filemeta['auto_review_result'] = 'Some of these folk on circulation no longer exist on this plane of existence'
    
    return filemeta
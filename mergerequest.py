import requests, json

gitlabAccessToken = ''
sourceBranch = ''
targetBranch = ''
title = ''
description = ''
assigneeid = ''

projectidList = [1, 2, 3]
for id in projectidList:
    print(id)
    mrurl = ''
    mrurl = 'base-url' + '/api/v4/projects/' + str(id) + '/merge_requests'
    print(mrurl)
    header = {'PRIVATE-TOKEN' : gitlabAccessToken}
    params = {
            'id'            : str(id),
            'title'         : title, 
            'assignee_id'   : assigneeid,
            'source_branch' : sourceBranch, 
            'target_branch' : targetBranch
            }
    reply = requests.post(mrurl, data=params, headers=header)
    status = json.loads(reply.text)
    print(id)

def lambda_handler(event, context):
  # ruleid: tainted-html-string
    foobar(f"<div>{event['input']}</div>")
    response = {}
    link1 = '<a href="http://external/abc/%s">Check link href</a>'
    response['html1'] = link1 % event['input']
    response['html2'] = '<a href="http://external/abc/' + event['input'] + '">Check link 
    href</a>'
    link2 = '<a href="http://external/abc/{}">Check link href</a>'
    response['html3'] = link2.format(event['input'])
    print(f"<div>{event['input']}</div>")
    link_ok = '<a href="http://external/abc/{}">Check link href</a>'
    response['html3'] = link_ok.format("123")
    response['message'] = 'Data: [' + event['input'] + ']'
    result = {
        "statusCode": 200,
        "body": response
    }
    return result

import json

def lambda_handler(event, context):
  """Extracts the CloudFront-Viewer-Country header from the event and returns it."""

  headers = event['headers']
  viewer_country = headers.get('CloudFront-Viewer-Country')
  if viewer_country:
    return json.dumps({'viewer_country': viewer_country})
  else:
    return json.dumps({'viewer_country': None})

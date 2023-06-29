# request-country
Using CloudFront-Viewer-Country and Lambda to return the origin country

# deploy
`serverless deploy`

# query
`curl -X GET https://<API_GATEWAY_ENDPOINT>/`

The response will be a JSON object with a `viewer_country` key that contains the country code of the viewer.

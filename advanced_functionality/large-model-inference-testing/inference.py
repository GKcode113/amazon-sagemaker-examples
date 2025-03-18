import json

def inference(client, endpoint_name:str, data: dict):
    body = json.dumps(data).encode("utf-8")
    response = client.invoke_endpoint(EndpointName=endpoint_name, 
                                        ContentType="application/json", 
                                        Accept="application/json", Body=body)
    body = response["Body"].read()
    result = json.loads( body.decode("utf-8"))
    return result

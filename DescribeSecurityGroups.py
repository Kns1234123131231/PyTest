import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.vpc.v20170312 import vpc_client, models

try:
    # Required steps:
    # Instantiate an authentication object. The Tencent Cloud account key pair `secretId` and `secretKey` need to be passed in as the input parameters
    # This example uses the way to read from the environment variable, so you need to set these two values in the environment variable in advance
    # You can also write the key pair directly into the code, but be careful not to copy, upload, or share the code to others
    # Query the CAM key: https://console.cloud.tencent.com/cam/capi
    cred = credential.Credential("IKIDhCRP7YhaIFwMVO0LPDk0yf6G9l6BzWno", "lGVTAajcEZcQwB9qOffOr3yczA4g2Xmk")
    # Instantiate an HTTP option (optional; skip if there are no special requirements)
    httpProfile = HttpProfile()
    httpProfile.endpoint = "vpc.tencentcloudapi.com"

    # Optional steps:
    # Instantiate a client configuration object. You can specify the timeout period and other configuration items
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    # Instantiate an client object
    # The second parameter is the region information. You can directly enter the string "ap-guangzhou" or import the preset constant
    client = vpc_client.VpcClient(cred, "ap-seoul", clientProfile)

    # Instantiate a request object. You can further set the request parameters according to the API called and actual conditions
    req = models.DescribeSecurityGroupsRequest()
    params = {
        "SecurityGroupId": "sg-fsy7po8t"
    }
    req.from_json_string(json.dumps(params))

    # The returned "resp" is an instance of the DescribeSecurityGroupsResponse class which corresponds to the request object
    resp = client.DescribeSecurityGroups(req)
    # A string return packet in JSON format is output
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)

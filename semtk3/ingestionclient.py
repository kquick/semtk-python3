#
# Copyright 2019-20 General Electric Company
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from . import semtkasyncclient
import json

class IngestionClient(semtkasyncclient.SemTkAsyncClient):
    
    def __init__(self, serverURL, status_client, results_client):
        ''' servierURL string - e.g. http://machine:8099
            status_client 
            results_client 
        '''
        super(IngestionClient, self).__init__(serverURL, "ingestion", status_client, results_client)
    
    def exec_from_csv_using_class_template(self, class_uri, csv_str, conn_json_str,  id_regex=None):
        ''' execute a create_nodegroup
            thorws: exception otherwise
        '''
        payload = {}
        payload["connection"] = conn_json_str
        payload["classURI"] = class_uri
        payload["data"] = csv_str;
        if id_regex:
            payload["idRegex"] = id_regex
    
     
        res = self.post_async_to_record_process("fromCsvUsingClassTemplate", payload)
        
        return res
    
    def exec_get_class_template_csv(self, class_uri, conn_json_str, id_regex=None):
        ''' execute a create_nodegroup
            thorws: exception otherwise
        '''
        payload = {}
        payload["connection"] = conn_json_str
        payload["classURI"] = class_uri
        if id_regex:
            payload["idRegex"] = id_regex
        res = self.post_to_simple("getClassTemplateAndCsv", payload)
        
        return res["csv"]
    
    def exec_get_class_template(self, class_uri, conn_json_str, id_regex=None):
        ''' execute a create_nodegroup
            thorws: exception otherwise
        '''
        payload = {}
        payload["connection"] = conn_json_str
        payload["classURI"] = class_uri
        if id_regex:
            payload["idRegex"] = id_regex
            
        res = self.post_to_simple("getClassTemplateAndCsv", payload)
        
        return json.dumps(res["sgjson"])
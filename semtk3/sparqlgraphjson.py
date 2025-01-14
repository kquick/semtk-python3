#
# Copyright 2021 General Electric Company
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
from . import plotspecs

#
# Encapsulate the JSON format of a nodegroup
#
class SparqlGraphJson:
        
    def __init__(self, json):
        self.json = json
        if "plotSpecs" in json:
            self.plot_specs = plotspecs.PlotSpecs(json["plotSpecs"])
        else:
            self.plot_specs = plotspecs.PlotSpecs([])            
   
    def get_plot_specs(self):
        return self.plot_specs
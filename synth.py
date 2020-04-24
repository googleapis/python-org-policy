# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import synthtool as s
import synthtool.gcp as gcp
from synthtool import tmp
from synthtool.languages import python
from synthtool.sources import git

versions = ["v1"]

gapic = gcp.GAPICBazel()

for version in versions:
    library = gapic.py_library(
        service="orgpolicy",
        version=version,
        proto_path=f"google/cloud/orgpolicy/{version}",
        bazel_target=f"//google/cloud/orgpolicy/{version}:orgpolicy-{version}-py",
    )
    # only copy _pb2_grpc and _pb2.py files
    s.copy(
        library / "google/cloud/orgpolicy_v1/proto/*pb2*",
        "google/cloud/orgpolicy/v1",
        excludes=["google/cloud/orgpolicy_v1/proto/__init__.py"],
    )

# ----------------------------------------------------------------------------
#  Add templated files
# ----------------------------------------------------------------------------
common = gcp.CommonTemplates()
templated_files = common.py_library()
s.move(
    templated_files, excludes=["noxfile.py", ".coveragerc", ".gitignore",],
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)

# Add license headers
python.fix_pb2_headers()
python.fix_pb2_grpc_headers()

#!/usr/bin/env python

# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This sample provides a quickstart for creating and deleting a Dataproc
# Metastore service as well as attaching a Dataproc cluster to it, all
# using the Python client library.
#
# This script can be run on its own:
#   python quickstart.py ${PROJECT_ID} ${REGION} ${SERVICE_ID}


import sys


# [START metastore_quickstart_create_service]
def create_service(project_id, region, metastore_service_id):
    """This sample walks a user through creating a Dataproc Metastore Service
    using the Python client library.
    Args:
        project_id (string): Project to use for creating resources.
        region (string): Region where the resources should live.
        metastore_service_id (string): Name of the Metastore service.
    """
    from google.cloud import metastore_v1beta as metastore

    # Create a client with the endpoint set to the desired service region.
    client = metastore.DataprocMetastoreClient()

    parent = f"projects/{project_id}/locations/{region}"

    # Create the service
    operation = client.create_service(
        request={
            "parent": parent, "service_id": metastore_service_id, "service": {}
        }
    )

    result = operation.result()
    # Output a success message.
    print(f"Service created successfully at {result.name}")
    # [END metastore_quickstart_create_service]


# [START metastore_quickstart_create_cluster]
def create_cluster(project_id, region, cluster_name, metastore_service_id):
    """This sample walks a user through creating a Dataproc cluster attached
       to a Metastore serviceusing the Python client library.

        Args:
            project_id (string): Project to use for creating resources.
            region (string): Region where the resources should live.
            cluster_name (string): Name of the Dataproc cluster.
            metastore_service_id(string): Name of the Metastore service.
    """
    from google.cloud import dataproc_v1 as dataproc

    # Create a client with the endpoint set to the region of your metastore
    # service. This is where the Dataproc cluster will be created.
    cluster_client = dataproc.ClusterControllerClient(
        client_options={"api_endpoint": f"{region}-dataproc.googleapis.com:443"}
    )

    dataproc_metastore_service = (f"projects/{project_id}/locations/{region}"
                                  "/services/{metastore_service_id}")

    # Create the cluster config.
    cluster = {
        "project_id": project_id,
        "cluster_name": cluster_name,
        "config": {
            "metastore_config": {"dataproc_metastore_service": dataproc_metastore_service},
        },
    }

    # Create the cluster.
    operation = cluster_client.create_cluster(
        request={"project_id": project_id, "region": region, "cluster": cluster}
    )
    result = operation.result()

    # Output a success message.
    print(f"Cluster created successfully: {result.cluster_name}")
    # [END metastore_quickstart_create_cluster]


# [START metastore_quickstart_delete_service]
def delete_service(project_id, region, metastore_service_id):
    """This sample walks a user through creating a Cloud Dataproc cluster
       using the Python client library.
       Args:
           project_id (string): Project to use for creating resources.
           region (string): Region where the resources should live.
           metastore_service_id (string): Name to use for creating the service.
    """
    from google.cloud import metastore_v1beta as metastore

    # Create a client with the endpoint set to the desired service region.
    client = metastore.DataprocMetastoreClient()

    dataproc_metastore_service = (f"projects/{project_id}/locations/{region}"
                                  "/services/{metastore_service_id}")

    # Delete the cluster.
    operation = client.delete_service(
        request={"name": dataproc_metastore_service}
    )

    operation.result()
    print(f"Metastore service {metastore_service_id} successfully deleted.")
# [END metastore_quickstart_delete_service]


def quickstart(project_id, region, cluster_name, metastore_service_id):
    create_service(project_id, region, metastore_service_id)
    create_cluster(project_id, region, cluster_name, metastore_service_id)
    delete_service(project_id, region, metastore_service_id)


if __name__ == "__main__":
    if len(sys.argv) < 5:
        sys.exit(("python quickstart.py project_id"
                  "region cluster_name metastore_service_id"))

    project_id = sys.argv[1]
    region = sys.argv[2]
    service_id = sys.argv[3]
    quickstart(project_id, region, service_id)

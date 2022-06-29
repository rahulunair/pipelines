# Copyright 2021 The Kubeflow Authors. All Rights Reserved.
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
"""Classes for ML Metadata input/output Artifacts for tracking Google resources."""

from typing import Dict, Optional
from kfp.v2 import dsl
import json

# The artifact property key for the resource name
ARTIFACT_PROPERTY_KEY_RESOURCE_NAME = 'resourceName'

class VertexModel(dsl.Artifact):
  """An artifact representing a Vertex Model."""
  TYPE_NAME = 'google.VertexModel'

  def __init__(self, name: str, uri: str, model_resource_name: str):
    """Args:

         name: The artifact name.
         uri: the Vertex Model resource uri, in a form of
         https://{service-endpoint}/v1/projects/{project}/locations/{location}/models/{model},
         where
         {service-endpoint} is one of the supported service endpoints at
         https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints
         model_resource_name: The name of the Model resource, in a form of
         projects/{project}/locations/{location}/models/{model}. For
         more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.models/get
    """
    super().__init__(
        uri=uri,
        name=name,
        metadata={ARTIFACT_PROPERTY_KEY_RESOURCE_NAME: model_resource_name})


class VertexEndpoint(dsl.Artifact):
  """An artifact representing a Vertex Endpoint."""
  TYPE_NAME = 'google.VertexEndpoint'

  def __init__(self, name: str, uri: str, endpoint_resource_name: str):
    """Args:

         name: The artifact name.
         uri: the Vertex Endpoint resource uri, in a form of
         https://{service-endpoint}/v1/projects/{project}/locations/{location}/endpoints/{endpoint},
         where
         {service-endpoint} is one of the supported service endpoints at
         https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints
         endpoint_resource_name: The name of the Endpoint resource, in a form of
         projects/{project}/locations/{location}/endpoints/{endpoint}. For
         more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/get
    """
    super().__init__(
        uri=uri,
        name=name,
        metadata={ARTIFACT_PROPERTY_KEY_RESOURCE_NAME: endpoint_resource_name})


class VertexBatchPredictionJob(dsl.Artifact):
  """An artifact representing a Vertex BatchPredictionJob."""
  TYPE_NAME = 'google.VertexBatchPredictionJob'

  def __init__(self,
               name: str,
               uri: str,
               job_resource_name: str,
               bigquery_output_table: Optional[str] = None,
               bigquery_output_dataset: Optional[str] = None,
               gcs_output_directory: Optional[str] = None):
    """Args:

         name: The artifact name.
         uri: the Vertex Batch Prediction resource uri, in a form of
         https://{service-endpoint}/v1/projects/{project}/locations/{location}/batchPredictionJobs/{batchPredictionJob},
         where {service-endpoint} is one of the supported service endpoints at
         https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints
         job_resource_name: The name of the batch prediction job resource,
         in a form of
         projects/{project}/locations/{location}/batchPredictionJobs/{batchPredictionJob}.
         For more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs/get
         bigquery_output_table: The name of the BigQuery table created, in
         predictions_<timestamp> format, into which the prediction output is
         written. For more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs#outputinfo
         bigquery_output_dataset: The path of the BigQuery dataset created, in
         bq://projectId.bqDatasetId format, into which the prediction output is
         written. For more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs#outputinfo
         gcs_output_directory: The full path of the Cloud Storage directory
         created, into which the prediction output is written. For more details,
         see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs#outputinfo
    """
    super().__init__(
        uri=uri,
        name=name,
        metadata={
            ARTIFACT_PROPERTY_KEY_RESOURCE_NAME: job_resource_name,
            'bigqueryOutputTable': bigquery_output_table,
            'bigqueryOutputDataset': bigquery_output_dataset,
            'gcsOutputDirectory': gcs_output_directory
        })


class VertexDataset(dsl.Artifact):
  """An artifact representing a Vertex Dataset."""
  TYPE_NAME = 'google.VertexDataset'

  def __init__(self, name: str, uri: str, dataset_resource_name: str):
    """Args:

         name: The artifact name.
         uri: the Vertex Dataset resource uri, in a form of
         https://{service-endpoint}/v1/projects/{project}/locations/{location}/datasets/{datasets_name},
         where
         {service-endpoint} is one of the supported service endpoints at
         https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints
         dataset_resource_name: The name of the Dataset resource, in a form of
         projects/{project}/locations/{location}/datasets/{datasets_name}. For
         more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.datasets/get
    """
    super().__init__(
        uri=uri,
        name=name,
        metadata={ARTIFACT_PROPERTY_KEY_RESOURCE_NAME: dataset_resource_name})


class BQMLModel(dsl.Artifact):
  """An artifact representing a BQML Model."""
  TYPE_NAME = 'google.BQMLModel'

  def __init__(self, name: str, project_id: str, dataset_id: str,
               model_id: str):
    """Args:

         name: The artifact name.
         project_id: The ID of the project containing this model.
         dataset_id: The ID of the dataset containing this model.
         model_id: The ID of the model.

         For more details, see
         https://cloud.google.com/bigquery/docs/reference/rest/v2/models#ModelReference
    """
    super().__init__(
        uri=f'https://www.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/models/{model_id}',
        name=name,
        metadata={
            'projectId': project_id,
            'datasetId': dataset_id,
            'modelId': model_id
        })


class BQTable(dsl.Artifact):
  """An artifact representing a BQ Table."""
  TYPE_NAME = 'google.BQTable'

  def __init__(self, name: str, project_id: str, dataset_id: str,
               table_id: str):
    """Args:

         name: The artifact name.
         project_id: The ID of the project containing this table.
         dataset_id: The ID of the dataset containing this table.
         table_id: The ID of the table.

         For more details, see
         https://cloud.google.com/bigquery/docs/reference/rest/v2/TableReference
    """
    super().__init__(
        uri=f'https://www.googleapis.com/bigquery/v2/projects/{project_id}/datasets/{dataset_id}/tables/{table_id}',
        name=name,
        metadata={
            'projectId': project_id,
            'datasetId': dataset_id,
            'tableId': table_id
        })


class ClassificationMetrics(dsl.Metrics):
  """An artifact representing evaluation Classification Metrics."""
  TYPE_NAME = 'google.ClassificationMetrics'

  def __init__(self,
               name: str,
               uri: str,
               au_prc: Optional[float] = None,
               au_roc: Optional[float] = None,
               log_loss: Optional[float] = None):
    """Args:

         name: The artifact name.
         uri: The GCS location where the complete metrics are stored.
         au_prc: The Area Under Precision-Recall Curve metric. Micro-averaged
         for the overall evaluation.
         au_roc: The Area Under Receiver Operating Characteristic curve metric.
         Micro-averaged for the overall evaluation.
         log_loss: The Log Loss metric.
    """
    super().__init__(uri=uri, name=name)
    if au_prc is not None:
      self.log_metric('auPrc', au_prc)
    if au_roc is not None:
      self.log_metric('auRoc', au_roc)
    if log_loss is not None:
      self.log_metric('logLoss', log_loss)


class RegressionMetrics(dsl.Metrics):
  """An artifact representing evaluation Regression Metrics."""
  TYPE_NAME = 'google.RegressionMetrics'

  def __init__(self,
               name: str,
               uri: str,
               root_mean_squared_error: Optional[float] = None,
               mean_absolute_error: Optional[float] = None,
               mean_absolute_percentage_error: Optional[float] = None,
               r_squared: Optional[float] = None,
               root_mean_squared_log_error: Optional[float] = None):
    """Args:

         name: The artifact name.
         uri: The GCS location where the complete metrics are stored.
         root_mean_squared_error: Root Mean Squared Error (RMSE).
         mean_absolute_error: Mean Absolute Error (MAE).
         mean_absolute_percentage_error: Mean absolute percentage error.
         Infinity when there are zeros in the ground truth.
         r_squared: Coefficient of determination as Pearson correlation
         coefficient. Undefined when ground truth or predictions are constant or
         near constant.
         root_mean_squared_log_error: Root mean squared log error. Undefined
         when there are negative ground truth values or predictions.
    """
    super().__init__(uri=uri, name=name)
    if root_mean_squared_error is not None:
      self.log_metric('rootMeanSquaredError', root_mean_squared_error)
    if mean_absolute_error is not None:
      self.log_metric('meanAbsoluteError', mean_absolute_error)
    if mean_absolute_percentage_error is not None:
      self.log_metric('meanAbsolutePercentageError',
                      mean_absolute_percentage_error)
    if r_squared is not None:
      self.log_metric('rSquared', r_squared)
    if root_mean_squared_log_error is not None:
      self.log_metric('rootMeanSquaredLogError', root_mean_squared_log_error)


class ForecastingMetrics(dsl.Metrics):
  """An artifact representing evaluation Forecasting Metrics."""
  TYPE_NAME = 'google.ForecastingMetrics'

  def __init__(
      self,
      name: str,
      uri: str,
      root_mean_squared_error: Optional[float] = None,
      mean_absolute_error: Optional[float] = None,
      mean_absolute_percentage_error: Optional[float] = None,
      r_squared: Optional[float] = None,
      root_mean_squared_log_error: Optional[float] = None,
      weighted_absolute_percentage_error: Optional[float] = None,
      root_mean_squared_percentage_error: Optional[float] = None,
      symmetric_mean_absolute_percentage_error: Optional[float] = None):
    """Args:

         name: The artifact name.
         uri: The GCS location where the complete metrics are stored.
         root_mean_squared_error: Root Mean Squared Error (RMSE).
         mean_absolute_error: Mean Absolute Error (MAE).
         mean_absolute_percentage_error: Mean absolute percentage error.
         Infinity when there are zeros in the ground truth.
         r_squared: Coefficient of determination as Pearson correlation
         coefficient. Undefined when ground truth or predictions are constant or
         near constant.
         root_mean_squared_log_error: Root mean squared log error. Undefined
         when there are negative ground truth values or predictions.
         weighted_absolute_percentage_error: Weighted Absolute Percentage Error.
         Does not use weights, this is just what the metric is called. Undefined
         if actual values sum to zero. Will be very large if actual values sum
         to a very small number.
         root_mean_squared_percentage_error: Root Mean Square Percentage Error.
         Square root of MSPE. Undefined/imaginary when MSPE is negative.
         symmetric_mean_absolute_percentage_error: Symmetric Mean Absolute
         Percentage Error.
    """
    super().__init__(uri=uri, name=name)
    if root_mean_squared_error is not None:
      self.log_metric('rootMeanSquaredError', root_mean_squared_error)
    if mean_absolute_error is not None:
      self.log_metric('meanAbsoluteError', mean_absolute_error)
    if mean_absolute_percentage_error is not None:
      self.log_metric('meanAbsolutePercentageError',
                      mean_absolute_percentage_error)
    if r_squared is not None:
      self.log_metric('rSquared', r_squared)
    if root_mean_squared_log_error is not None:
      self.log_metric('rootMeanSquaredLogError', root_mean_squared_log_error)
    if weighted_absolute_percentage_error is not None:
      self.log_metric('weightedAbsolutePercentageError',
                      weighted_absolute_percentage_error)
    if root_mean_squared_percentage_error is not None:
      self.log_metric('rootMeanSquaredPercentageError',
                      root_mean_squared_percentage_error)
    if symmetric_mean_absolute_percentage_error is not None:
      self.log_metric('symmetricMeanAbsolutePercentageError',
                      symmetric_mean_absolute_percentage_error)


class UnmanagedContainerModel(dsl.Artifact):
  """An artifact representing an unmanaged container model."""
  TYPE_NAME = 'google.UnmanagedContainerModel'

  def __init__(self, predict_schemata: Dict, container_spec: Dict):
    """Args:

         predict_schemata: Contains the schemata used in Model's predictions and
         explanations via PredictionService.Predict, PredictionService.Explain
         and BatchPredictionJob. For more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/PredictSchemata
         container_spec: Specification of a container for serving predictions.
         Some fields in this message correspond to fields in the Kubernetes
         Container v1 core specification. For more details, see
         https://cloud.google.com/vertex-ai/docs/reference/rest/v1/ModelContainerSpec
    """
    super().__init__(metadata={
        'predictSchemata': predict_schemata,
        'containerSpec': container_spec
    })

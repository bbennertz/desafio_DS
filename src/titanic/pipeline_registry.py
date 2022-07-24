"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline
from titanic.pipelines import data_processing
from titanic.pipelines import data_science as ds
from titanic.pipelines import predict

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """
    data_processing_pipeline =  data_processing.create_pipeline()
    data_science_pipeline = ds.create_pipeline()
    predict_pipeline = predict.create_pipeline()

    return {"dp": data_processing_pipeline,
            "ds": data_science_pipeline,
            "pred": predict_pipeline,
            "__default__": data_processing_pipeline + data_science_pipeline + predict_pipeline}

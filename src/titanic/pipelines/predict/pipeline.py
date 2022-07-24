"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from titanic.pipelines.predict.nodes import batch_predict


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=batch_predict,
            name="batch_predict",
            inputs=['model_classifier','preprocessed_test'],
            outputs='predictions'
        )
    ])

"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.data_processing.nodes import preprocess_train
from titanic.pipelines.data_processing.nodes import preprocess_test


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=preprocess_train,
            inputs="train",
            outputs="preprocessed_train",
            name="pre_processed_train_node"
        ),

        node(
            func=preprocess_test,
            inputs="test",
            outputs="preprocessed_test",
            name="pre_processed_test_node"
        ),

    ])


"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline
from titanic.pipelines.data_science.nodes import fit_model, split_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func = split_data,
            inputs ='preprocessed_train',
            outputs=['X_train', 'X_test', 'y_train', 'y_test'],
            name = "split_data"
        ),
        node(
            func = fit_model,
            inputs= ['X_train', 'X_test', 'y_train', 'y_test'],
            outputs= 'model_classifier',
            name = "fit_model"

        )
    ])

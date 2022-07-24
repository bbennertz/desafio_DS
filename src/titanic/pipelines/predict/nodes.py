"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.1
"""

def batch_predict(model_artifact, dataset):
    """This function takes a pre-trained model
    and predicts an unknown dataset"""

    predictions = model_artifact.predict(dataset)

    final_predictions=dataset
    final_predictions['Survived']= predictions

    return final_predictions


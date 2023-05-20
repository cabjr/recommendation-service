from vowpalwabbit import pyvw
from .models import Item

# Initialize Vowpal Wabbit model
vw = pyvw.vw("--cb 2")

def train_example(item: Item):
    """
    Function to train the Vowpal Wabbit model on an example.
    """
    example = vw.example(f"{int(item.label)}:1:0.5 | {item.features}")
    vw.learn(example)
    example.finish()

def predict_example(item: Item):
    """
    Function to predict the label for an example using the Vowpal Wabbit model.
    """
    example = vw.example(f"| {item.features}")
    prediction = vw.predict(example)
    example.finish()
    return prediction

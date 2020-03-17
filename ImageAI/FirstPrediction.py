# Importing classing
from imageai.Prediction import ImagePrediction
import os

# INFO, WARNING, and ERROR messages are not printed
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Set execution path as variable so we can access algorithms and images
execution_path = os.getcwd()

def debugFile():
    # path = "/Users/Saif/Desktop/ImageAI/"
    # filepath = execution_path + "/" + "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"
    # print(execution_path + "/" + "inception_v3_weights_tf_dim_ordering_tf_kernels.h5")
    filepath = execution_path
    # path = os.path.join(filepath).replace(" ", "\\ ")
    files = os.listdir(filepath)
    for name in files:
        print(name)

filepath = execution_path + "/" + "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"
# print(execution_path + "/" + "inception_v3_weights_tf_dim_ordering_tf_kernels.h5")

# path = os.path.join(filepath).replace(" ", "\\ ")
# print(path)


def prediction():
    # Create instance of image prediction class
    prediction = ImagePrediction()

    # Set the model type of the prediction object and path - basically determines which algorithm we are using
    # prediction.setModelTypeAsResNet()
    prediction.setModelTypeAsInceptionV3()
    # prediction.setModelPath(execution_path + "/" + "resnet50_weights_tf_dim_ordering_tf_kernels.h5")
    # print(execution_path + "/" + "inception_v3_weights_tf_dim_ordering_tf_kernels.h5")
    # prediction.setModelPath(path)
    prediction.setModelPath(filepath)
    prediction.loadModel()

    # Return 2 array objects with the predictions (result_count) and the percentage probabilities
    global predictions
    predictions, percentage_probabilities = prediction.predictImage(execution_path + "/" + "pizza.jpg", result_count=5)
    # Iterate through objects and prints percentages per prediction
    for index in range(len(predictions)):
        print(predictions[index], " : ", percentage_probabilities[index])


debugFile()
prediction()

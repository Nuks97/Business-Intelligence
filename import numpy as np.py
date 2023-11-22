import numpy as np
import matplotlib.pyplot as plt

# Define the number of epochs and the corresponding metrics
epochs = [3, 5, 8]
train_loss = [0.2235, 0.1421, 0.0566]  # Replace with your actual training loss values
val_loss = [0.1647, 0.0843, 0.0267]  # Replace with your actual validation loss values
train_accuracy = [0.8129, 0.8475, 0.8816]  # Replace with your actual training accuracy values
val_accuracy = [0.8381, 0.8730, 0.8929]  # Replace with your actual validation accuracy values

# Create subplots for loss and accuracy
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
fig.suptitle('Training and Validation Metrics Over Epochs')

# Training Loss Bar Graph
axs[0, 0].bar(epochs, train_loss, color='skyblue')
axs[0, 0].set_title('Training Loss')
axs[0, 0].set_xlabel('Epochs')
axs[0, 0].set_ylabel('Loss')

# Validation Loss Bar Graph
axs[0, 1].bar(epochs, val_loss, color='lightcoral')
axs[0, 1].set_title('Validation Loss')
axs[0, 1].set_xlabel('Epochs')
axs[0, 1].set_ylabel('Loss')

# Training Accuracy Bar Graph
axs[1, 0].bar(epochs, train_accuracy, color='lightgreen')
axs[1, 0].set_title('Training Accuracy')
axs[1, 0].set_xlabel('Epochs')
axs[1, 0].set_ylabel('Accuracy')

# Validation Accuracy Bar Graph
axs[1, 1].bar(epochs, val_accuracy, color='lightcoral')
axs[1, 1].set_title('Validation Accuracy')
axs[1, 1].set_xlabel('Epochs')
axs[1, 1].set_ylabel('Accuracy')

# Adjust layout for better visualization
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
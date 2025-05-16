
import matplotlib.pyplot as plt

def plot_results(y_test, predictions):
    plt.figure(figsize=(10,5))
    plt.plot(y_test.values, label='Actual Water Level')
    plt.plot(predictions, label='Predicted Water Level')
    plt.title('Water Level Prediction')
    plt.xlabel('Test Sample')
    plt.ylabel('Water Level (m)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('water_level_prediction.png')
    plt.show()

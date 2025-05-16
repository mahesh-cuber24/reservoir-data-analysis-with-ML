
from src.preprocess import load_and_engineer_features
from src.train_model import train_model
from src.visualize import plot_results

def main():
    df = load_and_engineer_features('D:\Reservoir Data Anaylsis\data\synthetic_reservoir_data.csv')
    model, X_test, y_test, predictions = train_model(df)
    plot_results(y_test, predictions)

if __name__ == "__main__":
    main()

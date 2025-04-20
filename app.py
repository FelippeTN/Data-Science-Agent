import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataScienceAgent:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
    
    def summarize_data(self):
        """Exibe um resumo estatístico do conjunto de dados."""
        print("Resumo Estatístico:")
        print(self.data.describe())
        print("\nInformações do Dataset:")
        print(self.data.info())
    
    def visualize_data(self, column1, column2, plot_type="scatter"):
        """Cria visualizações básicas entre duas colunas."""
        if plot_type == "scatter":
            self.data.plot.scatter(x=column1, y=column2)
        elif plot_type == "histogram":
            self.data[column1].hist()
        elif plot_type == "boxplot":
            sns.boxplot(data=self.data, x=column1, y=column2)
        else:
            print("Tipo de gráfico não suportado.")
        plt.show()
    
    def find_missing_values(self):
        """Identifica valores ausentes no conjunto de dados."""
        missing = self.data.isnull().sum()
        print("Valores Ausentes por Coluna:")
        print(missing)

    def fill_missing_values(self, column, method="mean"):
        """Preenche valores ausentes em uma coluna específica."""
        if method == "mean":
            self.data[column].fillna(self.data[column].mean(), inplace=True)
        elif method == "median":
            self.data[column].fillna(self.data[column].median(), inplace=True)
        elif method == "mode":
            self.data[column].fillna(self.data[column].mode()[0], inplace=True)
        else:
            print("Método de preenchimento não suportado.") 
        
    def save_cleaned_data(self, output_path):
        """Salva o conjunto de dados limpo em um novo arquivo CSV."""
        self.data.to_csv(output_path, index=False)
        print(f"Dados salvos em {output_path}")
        
if __name__ == "__main__":
    agent = DataScienceAgent("seu_arquivo.csv")
    agent.summarize_data()
    agent.visualize_data("coluna1", "coluna2", plot_type="scatter")
    agent.find_missing_values()
    agent.fill_missing_values("coluna1", method="mean")
    agent.save_cleaned_data("dados_limpos.csv")         
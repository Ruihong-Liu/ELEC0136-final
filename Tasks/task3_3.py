from task3_1 import filter_stock_data,load_MongoDB_stock
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
stock_price=load_MongoDB_stock()
Filtered_data=filter_stock_data(stock_price)
def normalize_data(data):
    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns, index=data.index)
    return normalized_df
data_norm=normalize_data(Filtered_data)
print(data_norm)


def pca(filtered_data):
    # standardize the data and fit PCA function format
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(filtered_data)

    # apply PCA
    pca = PCA()
    pca.fit(scaled_data)

    # Variance explained rate
    explained_variance = pca.explained_variance_ratio_

    # sum of variance explained rate
    cumulative_explained_variance = explained_variance.cumsum()

    # threshold of 90% variance explained
    n_components = (cumulative_explained_variance < 0.90).sum() + 1

pca(data_norm)
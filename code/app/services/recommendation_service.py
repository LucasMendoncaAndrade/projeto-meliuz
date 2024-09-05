import pandas as pd
import numpy as np
from app.data.data_loader import load_csv_data


def get_5_recommendations(data_path):
    """Retorna os top produtos com base em sales_per_day."""
    products_df = load_csv_data(data_path)
    products_df['daily_income'] = products_df['product_price']*products_df['sales_per_day']
    products_df = products_df.sort_values(['daily_income'], ascending=[False]).drop_duplicates('product_id', keep='first').reset_index(drop = True)
    max_daily_income = products_df['daily_income'].max()
    min_daily_income = products_df['daily_income'].min()
    daily_income_bins = np.linspace(min_daily_income - 1e-6, max_daily_income + 1e-6, 6).tolist()
    products_df['daily_income_class'] = pd.cut(products_df['daily_income'], bins=daily_income_bins, labels=[1, 2, 3, 4, 5], right=False)
    products_df_grouped = products_df.groupby('daily_income_class', observed=False).apply(lambda x: x[['product_title', 'product_price', 'product_image_url', 'store_name']].sample(1))
    products = products_df_grouped.reset_index(drop=True)
    return products.to_dict(orient='index')
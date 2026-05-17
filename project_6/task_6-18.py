
import psycopg2
import pandas as pd

# ===== 1. ПОДКЛЮЧЕНИЕ =====
try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",               # твой порт
        user="postgres_task",      # твой пользователь
        password="student",        # твой пароль
        database="student"         # твоя БД
    )
    print("✅ Подключение к базе установлено")
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")
    exit()

# ===== 2. JOIN PRICES + PRODUCTS → DATAFRAME =====
query = """
    SELECT 
        p.name AS product_name,
        p.category,
        pr.price
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
"""
df = pd.read_sql(query, connection)
connection.close()

print(f"\n📊 Загружено записей: {len(df)}")
print("\n=== Первые 5 строк ===")
print(df.head())

# ===== 3. СТАТИСТИКА ПО ЦЕНЕ =====
print("\n=== Статистика по цене (руб.) ===")
print(f"Средняя цена:        {df['price'].mean():.2f} руб.")
print(f"Медиана:             {df['price'].median():.2f} руб.")
print(f"Стандартное отклонение: {df['price'].std():.2f} руб.")
print(f"Минимальная цена:    {df['price'].min():.2f} руб.")
print(f"Максимальная цена:   {df['price'].max():.2f} руб.")

# ===== 4. КВАРТИЛИ И ТОВАРЫ ВЫШЕ Q3 =====
Q1 = df['price'].quantile(0.25)
Q2 = df['price'].quantile(0.50)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1

print(f"\n=== Квартили ===")
print(f"Q1 (25%): {Q1:.2f} руб.")
print(f"Q2 (50%): {Q2:.2f} руб.")
print(f"Q3 (75%): {Q3:.2f} руб.")
print(f"IQR:      {IQR:.2f} руб.")

high_prices = df[df['price'] > Q3]
print(f"\n=== Товары с ценой выше Q3 ({len(high_prices)} записей) ===")
print(high_prices[['product_name', 'category', 'price']].to_string(index=False))

# ===== 5. ГРУППИРОВКА ПО КАТЕГОРИЯМ =====
grouped = df.groupby('category')['price'].agg(
    count='count',
    mean='mean',
    median='median',
    std='std'
).round(2).sort_values('mean', ascending=False)

print("\n=== Статистика по категориям ===")
print(grouped)

# ===== 6. РАЗБРОС ЦЕН ПО ТОВАРАМ =====
diff_df = df.groupby('product_name')['price'].agg(['min', 'max'])
diff_df['diff'] = diff_df['max'] - diff_df['min']
top5 = diff_df.nlargest(5, 'diff')

print("\n=== 5 товаров с наибольшим разбросом цен ===")
print(top5)
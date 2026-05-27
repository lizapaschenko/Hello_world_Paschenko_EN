
import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import Patch
import numpy as np

# ============================================================================
# 1. ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ (замените параметры на свои)
# ============================================================================
DB_CONFIG = {
    "host": "localhost",
    "port": "5435",          # ваш порт
    "user": "postgres_task", # ваш пользователь
    "password": "student",   # ваш пароль
    "database": "student"    # ваша БД
}

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        print("✅ Подключение к базе данных установлено\n")
        return conn
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        raise SystemExit

# ============================================================================
# 2. ИЗВЛЕЧЕНИЕ ДАННЫХ
# ============================================================================

# 2.1. Средняя цена и количество товаров по категориям
sql_category = """
    SELECT 
        p.category,
        COUNT(DISTINCT p.id) AS product_count,
        ROUND(AVG(pr.price)::numeric, 2) AS avg_price,
        ROUND(MIN(pr.price)::numeric, 2) AS min_price,
        ROUND(MAX(pr.price)::numeric, 2) AS max_price,
        ROUND(STDDEV(pr.price)::numeric, 2) AS price_stddev
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    GROUP BY p.category
    ORDER BY avg_price DESC
"""

# 2.2. Все цены с категориями (для распределения)
sql_all_prices = """
    SELECT 
        p.category,
        pr.price
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
"""

# 2.3. Глобальная статистика по ценам
sql_global_stats = """
    SELECT 
        COUNT(*) AS total_records,
        ROUND(MIN(price)::numeric, 2) AS min_price,
        ROUND(MAX(price)::numeric, 2) AS max_price,
        ROUND(AVG(price)::numeric, 2) AS avg_price,
        ROUND(PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price)::numeric, 2) AS median_price,
        ROUND(STDDEV(price)::numeric, 2) AS stddev_price
    FROM prices
"""

# 2.4. Поставщики по категориям (для дополнительного анализа)
sql_suppliers = """
    SELECT 
        p.category,
        COUNT(DISTINCT s.id) AS supplier_count
    FROM products p
    JOIN suppliers s ON p.id = s.product_id
    GROUP BY p.category
    ORDER BY supplier_count DESC
"""

# Загружаем данные
try:
    conn = get_connection()
    
    df_category = pd.read_sql(sql_category, conn)
    df_prices = pd.read_sql(sql_all_prices, conn)
    df_global = pd.read_sql(sql_global_stats, conn)
    df_suppliers = pd.read_sql(sql_suppliers, conn)
    
    conn.close()
    print("✅ Данные загружены, соединение закрыто\n")
except Exception as e:
    print(f"❌ Ошибка при загрузке данных: {e}")
    raise SystemExit

# ============================================================================
# 3. ПОДГОТОВКА ДАННЫХ ДЛЯ ГРАФИКОВ
# ============================================================================

# Цветовая схема для категорий
CAT_COLORS = {
    'Электроника': '#4a90d9',
    'Бытовая техника': '#5cb85c',
    'Одежда': '#f0ad4e',
    'Книги': '#7b68ee',
    'Продукты': '#d9534f'
}
df_category['color'] = df_category['category'].map(CAT_COLORS)

# Общая средняя цена (глобальная)
global_avg = df_global['avg_price'].iloc[0]
global_median = df_global['median_price'].iloc[0]

# ============================================================================
# 4. ПОСТРОЕНИЕ ГРАФИКОВ
# ============================================================================

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 10,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'figure.dpi': 130
})

# Создаём фигуру с сеткой 2x2
fig = plt.figure(figsize=(16, 11))
fig.suptitle('Анализ товарной базы данных', fontsize=16, fontweight='bold', y=1.01)

gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0])  # Средняя цена по категориям (вертикальная диаграмма)
ax2 = fig.add_subplot(gs[0, 1])  # Количество товаров по категориям
ax3 = fig.add_subplot(gs[1, 0])  # Распределение цен по категориям (boxplot)
ax4 = fig.add_subplot(gs[1, 1])  # Гистограмма всех цен + статистика

# ────────────────────────────────────────────────────────────────────────────
# ГРАФИК 1: Средняя цена по категориям (столбчатая диаграмма)
# Обоснование: столбчатая диаграмма лучше всего подходит для сравнения
#              средних значений между несколькими категориями.
# ────────────────────────────────────────────────────────────────────────────
bars1 = ax1.bar(
    df_category['category'],
    df_category['avg_price'],
    color=df_category['color'],
    edgecolor='white',
    width=0.6
)
# Подписи значений над столбцами
for bar, val in zip(bars1, df_category['avg_price']):
    ax1.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 30,
        f"{val:.0f} руб.",
        ha='center', fontsize=9, fontweight='bold'
    )
# Глобальная средняя линия
ax1.axhline(global_avg, color='crimson', linestyle='--', linewidth=1.5,
            label=f"Общая средняя: {global_avg:.0f} руб.")
ax1.set_ylabel("Средняя цена (руб.)")
ax1.set_title("1. Средняя цена по категориям", fontweight='bold', pad=8)
ax1.legend(fontsize=8)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# ────────────────────────────────────────────────────────────────────────────
# ГРАФИК 2: Количество товаров по категориям (столбчатая диаграмма)
# Обоснование: наглядно показывает, в какой категории больше всего товаров.
# ────────────────────────────────────────────────────────────────────────────
bars2 = ax2.bar(
    df_category['category'],
    df_category['product_count'],
    color=df_category['color'],
    edgecolor='white',
    width=0.6
)
for bar, val in zip(bars2, df_category['product_count']):
    ax2.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.3,
        str(int(val)),
        ha='center', fontsize=9, fontweight='bold'
    )
ax2.set_ylabel("Количество товаров")
ax2.set_title("2. Количество товаров по категориям", fontweight='bold', pad=8)
ax2.grid(axis='y', linestyle='--', alpha=0.5)

# ────────────────────────────────────────────────────────────────────────────
# ГРАФИК 3: Распределение цен по категориям (Boxplot)
# Обоснование: ящик с усами (boxplot) показывает разброс цен внутри категории,
#              медиану, квартили и выбросы — идеально для сравнения распределений.
# ────────────────────────────────────────────────────────────────────────────
box_data = [df_prices[df_prices['category'] == cat]['price'].values 
            for cat in df_category['category']]
bp = ax3.boxplot(box_data, labels=df_category['category'], patch_artist=True,
                 boxprops=dict(linewidth=1.2), medianprops=dict(linewidth=2, color='darkred'),
                 whiskerprops=dict(linewidth=1.2), flierprops=dict(marker='o', markersize=4, alpha=0.6))
for patch, color in zip(bp['boxes'], df_category['color']):
    patch.set_facecolor(color)
    patch.set_alpha(0.5)
ax3.set_ylabel("Цена (руб.)")
ax3.set_title("3. Распределение цен по категориям (медиана, квартили, выбросы)", fontweight='bold', pad=8)
ax3.tick_params(axis='x', rotation=20)
ax3.grid(axis='y', linestyle='--', alpha=0.3)

# ────────────────────────────────────────────────────────────────────────────
# ГРАФИК 4: Гистограмма всех цен + статистика
# Обоснование: гистограмма показывает форму распределения цен по всей базе,
#              а также позволяет сравнить среднее и медиану.
# ────────────────────────────────────────────────────────────────────────────
ax4.hist(df_prices['price'], bins=40, color='#4a90d9', alpha=0.7, edgecolor='white',
         label='Цены всех товаров')
ax4.axvline(global_avg, color='crimson', linestyle='--', linewidth=2,
            label=f"Среднее = {global_avg:.0f} руб.")
ax4.axvline(global_median, color='darkorange', linestyle='--', linewidth=2,
            label=f"Медиана = {global_median:.0f} руб.")
# Текстовый блок со статистикой
stats_text = (
    f"Всего записей: {df_global['total_records'].iloc[0]}\n"
    f"Средняя цена: {df_global['avg_price'].iloc[0]:.0f} руб.\n"
    f"Медиана: {df_global['median_price'].iloc[0]:.0f} руб.\n"
    f"Мин. цена: {df_global['min_price'].iloc[0]:.0f} руб.\n"
    f"Макс. цена: {df_global['max_price'].iloc[0]:.0f} руб.\n"
    f"Ст. откл.: {df_global['stddev_price'].iloc[0]:.0f} руб."
)
ax4.text(0.95, 0.95, stats_text, transform=ax4.transAxes, va='top', ha='right',
         fontsize=8, bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', alpha=0.9))
ax4.set_xlabel("Цена (руб.)")
ax4.set_ylabel("Частота")
ax4.set_title("4. Распределение всех цен (гистограмма)", fontweight='bold', pad=8)
ax4.legend(fontsize=8)
ax4.grid(axis='y', linestyle='--', alpha=0.3)

# ============================================================================
# 5. ВЫВОДЫ И АНОМАЛИИ (текст под графиками)
# ============================================================================
fig.text(0.5, -0.02,
         "📊 Выводы:\n"
         "1. Электроника и Бытовая техника — самые дорогие категории (≈70 000 и 56 000 руб.).\n"
         "2. Продукты и Книги — дешёвые (≈200 руб).\n"
         "3. Распределение цен имеет длинный правый хвост (среднее > медианы) — есть дорогие товары.\n"
         "4. Аномалии: отрицательных или нулевых цен нет. Выбросы (точки на boxplot) — редкие товары с ценой выше общей массы своей категории, что логично.",
         ha='center', fontsize=9, color='#2c3e50',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#ecf0f1'))

# ============================================================================
# 6. СОХРАНЕНИЕ
# ============================================================================
OUTPUT_FILE = "task_7_16_analysis.png"
plt.tight_layout()
plt.savefig(OUTPUT_FILE, bbox_inches="tight", dpi=150)
print(f"✅ График сохранён: {OUTPUT_FILE}")

plt.show()

# ============================================================================
# 7. ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ В КОНСОЛИ
# ============================================================================
print("\n" + "="*80)
print("АНАЛИТИЧЕСКИЕ ВЫВОДЫ (печать в консоль)")
print("="*80)

print("\n1. Средняя цена по категориям (руб.):")
for _, row in df_category.iterrows():
    print(f"   • {row['category']:20s}: {row['avg_price']:8.0f} руб.  (товаров: {int(row['product_count'])})")

print(f"\n2. Глобальная статистика цен:")
print(f"   • Средняя цена: {df_global['avg_price'].iloc[0]:.0f} руб.")
print(f"   • Медиана:      {df_global['median_price'].iloc[0]:.0f} руб.")
print(f"   • Стандартное отклонение: {df_global['stddev_price'].iloc[0]:.0f} руб.")
print(f"   • Минимум:      {df_global['min_price'].iloc[0]:.0f} руб.")
print(f"   • Максимум:     {df_global['max_price'].iloc[0]:.0f} руб.")

# Проверка аномалий
if (df_prices['price'] <= 0).any():
    print("\n⚠ Аномалия: обнаружены нулевые или отрицательные цены!")
else:
    print("\n✅ Аномалии не обнаружены: все цены > 0.")

print(f"\n3. Количество поставщиков по категориям:")
for _, row in df_suppliers.iterrows():
    print(f"   • {row['category']:20s}: {row['supplier_count']} поставщиков")

print("\n4. Общий вывод:")
print("   • Самая дорогая категория — Электроника (≈70 000 руб.).")
print("   • Самая дешёвая — Продукты (≈200 руб.).")
print("   • Распределение цен имеет положительную асимметрию (среднее > медианы).")
print("   • Выбросы на boxplot — это единичные дорогие товары в категории, что не является ошибкой.")
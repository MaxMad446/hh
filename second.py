from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

spark = SparkSession.builder.appName("product_category_pairs").getOrCreate()

# Создаем исходные датафреймы для продуктов и категорий
products = spark.createDataFrame([
    (1, "Product A"),
    (2, "Product B"),
    (3, "Product C")
], ["product_id", "product_name"])

categories = spark.createDataFrame([
    (1, "Category X"),
    (2, "Category Y"),
    (3, "Category Z")
], ["category_id", "category_name"])

# Создаем датафрейм для связей между продуктами и категориями
product_categories = spark.createDataFrame([
    (1, 1), # Product A - Category X
    (1, 2), # Product A - Category Y
    (2, 2), # Product B - Category Y
], ["product_id", "category_id"])

# Соединяем продукты с категориями и находим все пары "Имя продукта - Имя категории"
product_category_pairs = products.join(product_categories, "product_id") \
    .join(categories, products["category_id"] == categories["category_id"]) \
    .select("product_name", "category_name")

# Находим имена всех продуктов, у которых нет категорий
products_without_categories = products.join(product_categories, 
    products["product_id"] == product_categories["product_id"], "left_anti") \
    .select("product_name")

# Показываем результаты
print("Product - Category pairs:")
product_category_pairs.show()

print("Products without categories:")
products_without_categories.show()

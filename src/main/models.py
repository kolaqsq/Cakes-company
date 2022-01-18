from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    size = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Изделие'
        verbose_name_plural = 'Изделия'

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.IntegerField(verbose_name='Номер заказа', primary_key=True)
    date = models.DateField(verbose_name='Дата заказа', )
    name = models.CharField(verbose_name='Наименование заказа', max_length=100)
    product = models.ForeignKey(Product, verbose_name='Изделие', on_delete=models.CASCADE)
    customer = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE,
                                 related_name='customer')
    manager = models.ForeignKey(User, null=True, blank=True, verbose_name='Менеджер', on_delete=models.CASCADE,
                                related_name='manager')
    cost = models.IntegerField(verbose_name='Стоимость заказа', null=True, blank=True)
    completion_date = models.DateField(verbose_name='Дата выполнения заказа', null=True, blank=True)
    example_of_work = models.ImageField(verbose_name='Пример работы', null=True, blank=True)

    class Meta:
        unique_together = ('number', 'date')
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    type = models.CharField(verbose_name='Тип оборудования', max_length=100, primary_key=True)

    class Meta:
        verbose_name = 'Тип оборудования'
        verbose_name_plural = 'Тип оборудования'

    def __str__(self):
        return self.type


class Equipment(models.Model):
    marking = models.CharField(verbose_name='Маркировка оборудования', max_length=100, primary_key=True)
    equipment_type = models.ForeignKey(EquipmentType, verbose_name='Тип оборудования',
                                       on_delete=models.CASCADE)
    specification = models.CharField(verbose_name='Характеристика', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'

    def __str__(self):
        return self.marking


class OperationSpecification(models.Model):
    product = models.ForeignKey(Product, verbose_name='Изделие', on_delete=models.CASCADE)
    operation = models.CharField(verbose_name='Проводимая операция', max_length=100)
    order = models.IntegerField(verbose_name='Порядковый номер операции')
    type_equipment = models.CharField(verbose_name='Тип оборудования', max_length=100)
    time_for_surgery = models.CharField(verbose_name='Время на операцию', max_length=100)

    class Meta:
        unique_together = ('product', 'operation', 'order',)
        verbose_name = 'Спецификация операции'
        verbose_name_plural = 'Спецификации операций'

    def __str__(self):
        template = '{0.product}, {0.operation}'
        return template.format(self)


class SemiFinishedSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', related_name='product')
    semi_finished = models.ForeignKey(Product, verbose_name='Полуфабрикат', related_name='semi_finished',
                                      on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')

    class Meta:
        unique_together = ('product', 'semi_finished',)
        verbose_name = 'Спецификация полуфабриката'
        verbose_name_plural = 'Спецификации полуфабрикатов'

    def __str__(self):
        return self.semi_finished


class Supplier(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование поставщика')
    address = models.CharField(max_length=100, verbose_name='Адрес', blank=True, null=True)
    estimated_delivery_time = models.CharField(max_length=100, verbose_name='Срок доставки')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class CakeDecoration(models.Model):
    code = models.CharField(verbose_name='Артикул', max_length=100, primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=100)
    measure = models.CharField('Единица измерения', max_length=100)
    count = models.IntegerField(verbose_name='Количество ингридиентов')
    main_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Основной поставщик', blank=True,
                                      null=True)
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    type = models.CharField(verbose_name='Тип украшения для торта', max_length=100)
    price = models.CharField(max_length=100, verbose_name='Закупочная цена')
    weight = models.CharField(max_length=100, verbose_name='Вес')

    class Meta:
        verbose_name = 'Украшение для торта'
        verbose_name_plural = 'Украшения для тортов'

    def __str__(self):
        template = '{0.code}, {0.name}'
        return template.format(self)


class CakeDecorationSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', )
    cake_decoration = models.ForeignKey(CakeDecoration, verbose_name='Украшение для торта', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')

    class Meta:
        unique_together = ('product', 'cake_decoration',)
        verbose_name = 'Спецификация украшения для торта'
        verbose_name_plural = 'Спецификации украшений для тортов'

    def __str__(self):
        return self.cake_decoration


class Ingredient(models.Model):
    code = models.CharField(verbose_name='Артикул', max_length=100, primary_key=True)
    name = models.CharField(verbose_name='Наименование', max_length=100)
    measure = models.CharField('Единица измерения', max_length=100)
    count = models.IntegerField(verbose_name='Количество ингридиентов')
    main_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Основной поставщик', blank=True,
                                      null=True)
    image = models.ImageField(verbose_name='Изображение', blank=True, null=True)
    type = models.CharField(verbose_name='Тип ингридиента', max_length=100)
    standard = models.CharField(max_length=100, verbose_name='ГОСТ', blank=True, null=True)
    packaging = models.CharField(max_length=100, verbose_name='Фасовка', blank=True, null=True)
    desc = models.TextField(max_length=255, verbose_name='Характеристика', blank=True, null=True)

    class Meta:
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        template = '{0.code}, {0.name}'
        return template.format(self)


class IngredientSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Изделие', )
    ingredient = models.ForeignKey(Ingredient, verbose_name='Ингредиент', on_delete=models.CASCADE)
    count = models.IntegerField(verbose_name='Количество')

    class Meta:
        unique_together = ('product', 'ingredient',)
        verbose_name = 'Спецификация украшения для торта'
        verbose_name_plural = 'Спецификации украшений для тортов'

    def __str__(self):
        return self.ingredient

from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField('Фото', upload_to='avatars', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото пользователя'
        verbose_name_plural = 'Фото пользователей'

        


class Product(models.Model):
	name = models.CharField(max_length=100)
	size = models.CharField(max_length=100)

	class Meta:
		verbose_name = 'Изделие'
		verbose_name_plural = 'Изделия'

	def __str__(self):
		return self.name


class Order(models.Model):
	number = models.IntegerField(verbose_name='Номер заказа')
	date = models.DateField(verbose_name='Дата заказа')
	name_order = models.CharField(verbose_name='Наименование заказа', max_length=100)
	product = models.ForeignKey(Product, null=False, verbose_name='Изделие', on_delete=models.DO_NOTHING)
	customer = models.ForeignKey(User, null=False, verbose_name='Покупатель', on_delete=models.DO_NOTHING, related_name='customer')
	manager = models.ForeignKey(User, null=True, verbose_name='Менеджер', on_delete=models.DO_NOTHING, related_name='manager')
	cost = models.IntegerField(verbose_name='Стоимость заказа', null=True)
	completion_date = models.DateField(verbose_name='Дата выполнения заказа', null=True)
	example_of_work = models.ImageField(verbose_name='Пример работы', null=True)

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'

	def __str__(self):
		return self.name_order


class Equipment(models.Model):
	marking = models.CharField(verbose_name='Маркировка оборудования', max_length=100)
	type_equipment = models.ForeignKey('TypeEquipment', verbose_name='Тип оборудования', null=False, on_delete=models.DO_NOTHING)
	specification = models.CharField(verbose_name='Характеристика', max_length=100)

	class Meta:
		verbose_name = 'Оборудование'
		verbose_name_plural = 'Оборудования'

	def __str__(self):
		return self.marking


class TypeEquipment(models.Model):
	type_equipment = models.CharField(verbose_name='Тип оборудования', max_length=100)

	class Meta:
		verbose_name = 'Тип оборудования'
		verbose_name_plural = 'Тип оборудования'

	def __str__(self):
		return self.type_equipment


class OperationSpecification(models.Model):
	product = models.ForeignKey(Product, verbose_name='Изделие', on_delete=models.DO_NOTHING)
	operation = models.CharField(verbose_name='Проводимая операция', max_length=100)
	serial_number = models.IntegerField(verbose_name='Порядковый номер операции', null=False)
	type_equipment = models.CharField(verbose_name='Тип оборудования', max_length=100)
	time_for_surgery = models.CharField(verbose_name='Время на операцию', max_length=100)

	class Meta:
		verbose_name = 'Спецификация операции'
		verbose_name_plural = 'Спецификации операций'

	def __str__(self):
		return self.operation


class SemiFinishedSpecification(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Изделие')
	semi_finished = models.CharField(verbose_name='Полуфабрикат', max_length=100)
	count = models.IntegerField(verbose_name='Количество полуфабрикатов')

	class Meta:
		verbose_name = 'Полуфабрикат'
		verbose_name_plural = 'Полуфабрикаты'

	def __str__(self):
		return self.semi_finished


class CakeDecoration(models.Model):
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Изделие')
	cake_decoration = models.CharField(verbose_name='Украшение торта', max_length=100)
	count = models.IntegerField(verbose_name='Количество украшений')

	class Meta:
		verbose_name = 'Украшение торта'
		verbose_name_plural = 'Украшения тортов'

	def __str__(self):
		return self.cake_decoration


class Ingredients(models.Model):
	name = models.CharField(verbose_name='Наименование', max_length=100)
	main_supplier = models.ForeignKey('Supplier', on_delete=models.DO_NOTHING, verbose_name='Основной поставщик')
	image = models.ImageField(verbose_name='Изображение')
	type_ingredient = models.CharField(verbose_name='Тип ингридиента', max_length=100)
	GOST = models.CharField(max_length=100, verbose_name='ГОСТ')
	packaging = models.CharField(max_length=100, verbose_name='Фасовка')
	desc = models.CharField(max_length=100, verbose_name='Характеристика')
	product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, verbose_name='Изделие', null=True)
	count = models.IntegerField(verbose_name='Количество ингридиентов', default=1)
	semi_finished = models.ForeignKey(SemiFinishedSpecification, on_delete=models.DO_NOTHING, verbose_name='Полуфабрикат', null=True)

	class Meta:
		verbose_name = 'Ингридиент'
		verbose_name_plural = 'Ингридиенты'

	def __str__(self):
		return self.name


class Supplier(models.Model):
	name = models.CharField(max_length=100, verbose_name='Наименование поставщика')
	address = models.CharField(max_length=100, verbose_name='Адресс')
	estimated_delivery_time = models.CharField(max_length=100, verbose_name='Срок доставки')

	class Meta:
		verbose_name = 'Поставщик'
		verbose_name_plural = 'Поставщики'

	def __str__(self):
		return self.name

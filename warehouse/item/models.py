from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    item_photo = models.ImageField(upload_to='images', blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    wh = models.ForeignKey('Warehouse', on_delete=models.CASCADE)
    pos = models.ForeignKey('Position', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    units = models.ForeignKey('Units', on_delete=models.CASCADE, blank=True)
    amount = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return (str(self.id) + '. ' + self.title + ' [' + str(self.cat) + '/' + str(self.wh) + '/' + str(
            self.pos) + ']')


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return (self.title)


class Warehouse(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return (self.title)


class Position(models.Model):
    title = models.CharField(max_length=255)
    pos_photo = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return (self.title)


class Units(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return (self.title)

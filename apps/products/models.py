from django.db import models
from apps.accounts.models import AccountsUser as user
from PIL import Image

KEL_PRODUCTS =(('1','Hobi'),('2','Elektronik'),('3','Home Tools'),('4','Fashion'))
SIZE_FASHION = (('',''),('1','XL'),('2','XXL'),('3','L'),('4','M'),('5','S'))
WARNA_PRODUCTS = (('',''),('1','Merah'),('2','Kuning'),('3','Hijau'),('4','Biru'),('5','Kuning'),
    ('6','Abu-Abu'),('7','Putih'),('8','Gold'),('9','Hitam'))
STATUS_PRODUK = (('1','Aktif'),('2','Non Aktif'))


class Kelompok(models.Model):
    kelompok = models.CharField(choices=KEL_PRODUCTS,max_length=30,null=True)
    nama_perent = models.CharField(max_length=100)

    def __str__(self):
        return '%s %s' % (self.kelompok,self.nama_perent,)

class Jenis_Products(models.Model):
    kel = models.ForeignKey(Kelompok,on_delete=models.CASCADE,related_name='kel_fk',null=True)
    nama = models.CharField(max_length=100)
    cu = models.ForeignKey(user,on_delete=models.CASCADE,related_name='U_JP')
    mu = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Jenis_Products'

    def __str__(self):
        return '%s %s' % (self.nama,self.kel.kelompok)

class Brand(models.Model):
    nama = models.CharField(max_length=10)
    cu = models.ForeignKey(user,on_delete=models.CASCADE)
    mu = models.DateField(auto_now=True)

    def __str__(self):
        return self.nama

class Products(models.Model):
    prod = models.ForeignKey(Jenis_Products, on_delete=models.CASCADE,related_name='prod_fk')
    merk = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='merk_fk',null=True,blank=True)
    warna = models.CharField(choices=WARNA_PRODUCTS,max_length=50 ,blank=True)
    size = models.CharField(choices=SIZE_FASHION, max_length=50 ,blank=True)
    deskripsi = models.CharField(max_length=200)
    harga_jual = models.IntegerField()
    harga_beli = models.IntegerField()
    qt = models.IntegerField()
    img1 = models.ImageField(upload_to="product", blank= True,null=True)
    img2 = models.ImageField(upload_to="product", blank= True,null=True)
    img3 = models.ImageField(upload_to="product", blank= True,null=True)
    sku = models.CharField(max_length=20)
    status = models.CharField(choices=STATUS_PRODUK,default=1,max_length=20)
    cu = models.ForeignKey(user, on_delete=models.CASCADE,related_name='cu_fk_prod')
    mu = models.DateField(auto_now=True)

    class Meta:
        db_table = 'Products'

    def __str__(self):
        return ' %s %s %s ' % (self.prod,self.harga_jual,self.qt)

    def save(self):
        super().save()

        img = Image.open(self.img1.path) # Open image
        img2 = Image.open(self.img2.path)
        img3 = Image.open(self.img3.path)
        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (250, 250)
            img.thumbnail(output_size) # Resize image
            img.save(self.img1.path)

        if img2.height > 300 or img2.width > 300:
            output_size = (250, 250)
            img2.thumbnail(output_size) # Resize image
            img2.save(self.img2.path)

        if img3.height > 300 or img3.width > 300:
            output_size = (250, 250)
            img3.thumbnail(output_size) # Resize image
            img3.save(self.img3.path)

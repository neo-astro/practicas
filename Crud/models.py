from django.db import models


class tpi(models.Model):
    Nomt = models.CharField(max_length=50)

    def __str__(self):
        fila01 = "Tipo de Id: " + self.Nomt 
        return fila01

class carrera(models.Model):
    Nomc = models.CharField(max_length=150)


    def __str__(self):
        fila02 = "Nombre de Carrera: " + self.Nomc
        return fila02

class pais(models.Model):
    Nomp = models.CharField(max_length=50) 


    def __str__(self):
        fila02 = "Pais: " + self.Nomp
        return fila02

class provincia(models.Model):
    Nompai = models.ForeignKey(pais, on_delete=models.CASCADE) 
    Nomprov = models.CharField(max_length=50)   


    def __str__(self):
        fila03 = "Provincia: " + self.Nomprov
        return fila03


class ciudad(models.Model):
    Nomprov = models.ForeignKey(provincia, on_delete=models.CASCADE)
    Nomcant = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        fila04 = "Canton: " + self.Nomcant
        return fila04

class usuarios(models.Model):
    N_Identificacion = models.CharField(max_length=15, primary_key=True)
    T_Identificacion = models.ForeignKey(tpi, on_delete=models.CASCADE) 
    Nombre = models.CharField(max_length=50)
    Apellido_P = models.CharField(max_length=50)
    Apellido_M = models.CharField(max_length=50)
    Fecha_Nac = models.DateField()
    Usu_Django = models.CharField(max_length=50)
    Ciudad = models.ForeignKey(ciudad, on_delete=models.CASCADE)
    Telf_Celular = models.CharField(max_length=15)



    def __str__(self):
        fila1 = "N_Identificacion: " + self.N_Identificacion 
        return fila1


class profesores(models.Model):
    usup = models.ForeignKey(usuarios, on_delete=models.CASCADE) 
    Fecha_Inic = models.DateField()
    Estado = models.BooleanField(default=False)


class alumnos(models.Model):
    usua = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    Nom_carr = models.ForeignKey(carrera, on_delete=models.CASCADE)
    Fecha_Inici = models.DateField()





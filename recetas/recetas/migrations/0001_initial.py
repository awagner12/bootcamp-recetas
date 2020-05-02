# Generated by Django 3.0.5 on 2020-05-02 16:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=1)),
                ('explicacion', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasos', to='recetas.Receta')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField(default=1)),
                ('unidad', models.CharField(choices=[('unidades', 'Unidades'), ('litros', 'Litros'), ('mililitros', 'Mililitros'), ('chucharadas', 'Cucharadas'), ('gramos', 'Gramos'), ('kilos', 'Kilos')], default='unidades', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes', to='recetas.Receta')),
            ],
        ),
    ]
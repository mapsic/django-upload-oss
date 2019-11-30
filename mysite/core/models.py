from django.db import models
from django.contrib import admin
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


def user_directory_path(instance, filename):
    print("in user_directory_path: " + filename)
    return filename


class File(models.Model):
    # the file will be uploaded to MEDIA_ROOT
    file_name = models.CharField(max_length=256, null=False)
    myfile = models.FileField(upload_to=user_directory_path)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        print("in save():")
        print("  filename: " + self.myfile.name)
        count = File.objects.filter(myfile='%s' % self.myfile.name).count()
        print("  number  : %d" % count)
        #count = File.objects.get(myfile='%s' % self.myfile.name).count()
        if count > 0:
            File.objects.filter(myfile='%s' % self.myfile.name).delete()
            print("Remove already existing objects from DB")

        super(File, self).save(*args, **kwargs)


@receiver(pre_delete, sender=File)
def file_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    print(sender.myfile)
    print(instance)
    instance.myfile.delete(False)


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass

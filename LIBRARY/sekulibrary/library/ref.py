class Subject(models.Model):
    class Meta:
        verbose_name_plural = "Subject"
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.title

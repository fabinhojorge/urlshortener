from django.db import models
import rest_api.utils as utils


LINK_SIZE = 10


class Url(models.Model):
    link = models.CharField('Link', max_length=1000, null=False, blank=False, unique=True)
    link_short = models.CharField('Shortened Link', max_length=100, null=True, blank=True, unique=True)
    count_request = models.IntegerField('Amount of requests', default=1)
    count_clicked = models.IntegerField('Amount of requests', default=0)
    create_at = models.DateTimeField("Create at", auto_now_add=True)
    updated_at = models.DateTimeField("Update at", auto_now=True)

    def __str__(self):
        return self.link

    def increase_count_request(self):
        self.count_request = self.count_request + 1

    def increase_count_clicked(self):
        self.count_clicked = self.count_clicked + 1

    def get_url_redirect(self):
        url = self.link
        if '//' not in url:
            url = "//"+str(url)

        return url

    def save(self, *args, **kwargs):
        if self.link and not self.link_short:
            random_value = utils.random_link_generator(size=LINK_SIZE)
            while Url.objects.filter(link_short=random_value).exists():
                random_value = utils.random_link_generator(size=LINK_SIZE)
            self.link_short = random_value
        super(Url, self).save(*args, **kwargs)

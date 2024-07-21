import os


def update_sitemap_cron():
    os.system('py manage.py refresh_sitemap')

from django.contrib import admin
from django.contrib.auth.models import User, Group
from library.models import Author, Catalogue, Subject, Publisher, CheckOut, CallNumber
from datetime import date
from admin_interface.admin import Theme


class SekuLib(admin.AdminSite):
    site_header = "seku library admin"
    site_title = "Admin dashboard"
    index_title = "Admin dashboard"


class CatalogueAdmin(admin.ModelAdmin):
    date_hierarchy = 'year'
    list_display = ['title', 'isbn', 'callno', 'price', 'author', 'publisher']
    search_fields = ['isbn', 'title']
    list_filter = ['callno', 'publisher', 'author', 'year']


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name']


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CallNumberAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id']
    list_filter = ['name', 'id']


class CheckOutAdmin(admin.ModelAdmin):
    search_fields = ['book__title']
    list_display = ['book', 'CheckedIn',
                    'student', 'issuedate', 'duedate', 'fine']
    list_filter = ['CheckedIn', 'book', 'issuedate', 'duedate']
    actions = ['charge_fine']

    @admin.action(description="Charge fine for selected books")
    def charge_fine(self, request, queryset):
        for item in queryset:
            due = str(item.duedate).split('-')
            late = (date.today() -
                    date(int(due[0]), int(due[1]), int(due[2])))

            late = int(str(late).split(' ')[0])
            if late > 0:
                for bk in queryset:
                    queryset.update(fine=late * 10)


seku_admin = SekuLib()
seku_admin.register([User, Group, Subject])
seku_admin.register(Author, AuthorAdmin)
seku_admin.register(Catalogue, CatalogueAdmin)
seku_admin.register(Publisher, PublisherAdmin)
seku_admin.register(CheckOut, CheckOutAdmin)
seku_admin.register(CallNumber, CallNumberAdmin)
seku_admin.register(Theme)

from django.contrib import admin
from .models import Record
# Register your models here.

admin.site.register(Record)

# @admin.register(BookInstance)
# class BookInstanceAdmin(admin.ModelAdmin):
#     list_display = ('book', 'status', 'borrower', 'due_back', 'id')
#     list_filter = ('status', 'due_back')
#
#     fieldsets = (
#         (None, {
#             'fields': ('book','imprint', 'id')
#         }),
#         ('Availability', {
#             'fields': ('status', 'due_back','borrower')
#         }),
#     )
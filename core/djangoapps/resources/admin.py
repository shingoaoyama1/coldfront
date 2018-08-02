from django.contrib import admin

from core.djangoapps.resources.models import (AttributeType, Resource,
                                              ResourceAttribute,
                                              ResourceAttributeType,
                                              ResourceType)


@admin.register(AttributeType)
class AttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'modified', )
    search_fields = ('name', )


@admin.register(ResourceType)
class ResourceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created', 'modified', )
    search_fields = ('name', 'description',)


@admin.register(ResourceAttributeType)
class ResourceAttributeTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'attribute_type_name', 'required', 'created', 'modified', )
    search_fields = ('name', 'attribute_type__name', 'resource_type__name',)
    list_filter = ('required', 'attribute_type__name', 'name')

    def attribute_type_name(self, obj):
        return obj.attribute_type.name


class ResourceAttributeInline(admin.TabularInline):
    model = ResourceAttribute
    readonly_fields_change = ('resource_attribute_type', )
    fields_change = ('resource_attribute_type', 'value',)
    extra = 0

    def get_fields(self, request, obj):
        if obj is None:
            return super().get_fields(request)
        else:
            return self.fields_change

    def get_readonly_fields(self, request, obj):
        if obj is None:
            # We are adding an object
            return super().get_readonly_fields(request)
        else:
            return self.readonly_fields_change


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    readonly_fields_change = ('resource_type', )
    fields_change = ('resource_type', 'name', 'description', 'is_available',
                     'is_public', 'allowed_groups', 'allowed_users', )
    list_display = ('pk', 'name', 'description', 'resource_type_name',
                    'is_available', 'is_public', 'created', 'modified', )
    search_fields = ('name', 'description', 'resource_type__name')
    list_filter = ('resource_type__name', 'is_available', 'is_public', )
    inlines = [ResourceAttributeInline, ]
    filter_horizontal = ['allowed_groups', 'allowed_users', ]

    def resource_type_name(self, obj):
        return obj.resource_type.name

    def get_fields(self, request, obj):
        if obj is None:
            return super().get_fields(request)
        else:
            return self.fields_change

    def get_readonly_fields(self, request, obj):
        if obj is None:
            # We are adding an object
            return super().get_readonly_fields(request)
        else:
            return self.readonly_fields_change


@admin.register(ResourceAttribute)
class ResourceAttributeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'resource_name', 'value', 'resource_attribute_type_name', 'created', 'modified', )
    search_fields = ('resource__name', 'resource_attribute_type__name', 'value')
    list_filter = ('resource_attribute_type__name', )

    def resource_name(self, obj):
        return obj.resource.name

    def resource_attribute_type_name(self, obj):
        return obj.resource_attribute_type.name

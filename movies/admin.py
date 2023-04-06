from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Actor, Genre, Movie, MovieShots, RatingStar, Rating, Review

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .tasks import send_new_movie_notification_to_email


class MovieAdminForm(forms.ModelForm):
    desc = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Movie
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('name',)


class ReviewInline(admin.StackedInline):
    model = Review
    extra = 0
    readonly_fields = ('name', 'email', 'parent')


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 0
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100">')

    get_image.short_description = "Изображение"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'get_image', 'draft')
    list_display_links = ('title', 'category', 'url')
    readonly_fields = ('get_image',)
    list_filter = ('category', 'year')
    search_fields = ('title', 'category__name')
    inlines = (MovieShotsInline, ReviewInline)
    actions = ["publish", "unpublish"]
    form = MovieAdminForm
    save_on_top = True
    save_as = True
    list_editable = ('draft',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="150" height="150">')

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change',)

    get_image.short_description = "Изображение"

    def save_model(self, request, obj, form, change):
        send_new_movie_notification_to_email(form.cleaned_data['title'])
        return super().save_model(request, obj, form, change)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'parent', 'movie')
    list_display_links = ('email',)
    readonly_fields = ('name', 'email', 'movie', 'parent')
    search_fields = ('id', 'name', 'email', 'movie')


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    list_display_links = ('id', 'name', 'get_image')
    readonly_fields = ('get_image',)
    search_fields = ('id', 'name')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50">')

    get_image.short_description = "Изображение"


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
    list_display_links = ('id', 'name', 'url')
    search_fields = ('id', 'name', 'url')


@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'movie', 'get_image')
    list_display_links = ('id', 'title', 'movie')
    readonly_fields = ('get_image',)
    search_fields = ('id', 'title', 'movie')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="50">')

    get_image.short_description = "Изображение"


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value')
    search_fields = ('id', 'value')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'star', 'movie')
    list_display_links = ('id', 'ip', 'star', 'movie')
    search_fields = ('id', 'ip', 'star', 'movie')


admin.site.site_title = 'Админка сайта Movie'
admin.site.site_header = 'Админка сайта Movie'

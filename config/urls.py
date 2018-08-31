from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from wishlist import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    # USER INFO API
    path('current_user', views.get_user_info),
    # WISHLIST API
    # Get a specific wishlist with wishlistId
    path('wishlist/get/<int:wish_list_id>', views.get_wish_list_items),
    # Get all wishlists owned by userId passed in
    path('wishlist/get_all/<int:user_id>', views.get_wish_list_ids),
    # Make a new wishlist owned by userId passed in
    path('wishlist/new/<int:user_id>', views.new_wish_list),
    # Update wishlist with wishlistId
    path('wishlist/update/<int:wish_list_id>', views.update_wish_list),
    # Delete wishlist with wishlistId
    path('wishlist/delete/<int:wish_list_id>', views.remove_wish_list),
    # TODO: PLEDGE API

    path(
        "about/",
        TemplateView.as_view(template_name="pages/about.html"),
        name="about",
    ),
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path(
        "users/",
        include("open_pledge.users.urls", namespace="users"),
    ),
    path("accounts/", include("allauth.urls")),
    # Your stuff: custom urls includes go here
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns

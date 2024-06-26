JAZZMIN_SETTINGS = {


    "site_brand": "Booster School",

    "welcome_sign": "Welcome to the library",

    "copyright": "Acme Library Ltd",

    "search_model": ["app_courses.Course", "app_courses.CourseTeacher"],
    ############
    # Top Menu #
    ############

    "topmenu_links": [

        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"model": "app_courses.CourseTeacher"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "books"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        # {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
        # {"model": "app_users.CustomUser"},
    ],

    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)

    # Custom links to append to app groups, keyed on app name
    # "custom_links": {
    #     "books": [{
    #         "name": "Make Messages", 
    #         "url": "make_messages", 
    #         "icon": "fas fa-comments",
    #         "permissions": ["app_users.view_book"]
    #     }]
    # },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "app_users.CustomUser": "fas fa-user",
        "app_articles.Articles": "fas fa-newspaper",
        "app_articles.ImageArticles": "fas fa-images",
        "app_events.Events": "fas fa-calendar-week",
        "app_reviews.Reviews": "fas fa-comment",

        "app_courses.Course": "fas fa-laptop-code",
        "app_courses.CourseProgram": "fas fa-list-alt",
        "app_courses.TopicProgram": "fas fa-file-alt",
        "app_courses.CourseDirection": "fas fa-code",
        "app_courses.MajorBenefit": "fas fa-plus-circle",
        "app_courses.EducationBenefit": "fas fa-plus-circle",
        "app_courses.CourseTeacher": "fas fa-graduation-cap",
        "app_courses.AboutProfession": "fas fa-user-tie",
        "app_courses.TeacherTechnology": "fas fa-network-wired",
        "app_courses.ClassGoingTopik": "fas fa-question-circle",
        "app_courses.ClassesGoing": "fas fa-question",

        "app_miscellaneous.FAQ": "fas fa-comments",
        "app_miscellaneous.Gallery": "fas fa-images",
        "app_miscellaneous.ContactUs": "fas fa-address-book",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to link font from fonts.googleapis.com (use custom_css to supply font otherwise)
    "use_google_fonts_cdn": True,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    # "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
}


#===================================================================================================================================================================================

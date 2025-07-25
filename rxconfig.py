import reflex as rx

config = rx.Config(
    app_name="HarvardFinal",
    show_built_with_reflex=False,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)
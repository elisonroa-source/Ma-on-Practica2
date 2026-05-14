import reflex as rx

config = rx.Config(
    app_name="manon_practica_2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_overview(data, template_dir="templates", output_file="overview.html"):
    env = Environment(
        loader=FileSystemLoader(template_dir), autoescape=select_autoescape()
    )
    template = env.get_template("overview.html")
    rendered = template.render(**data)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(rendered)

    print(f"[INFO] Overview written to {output_file}")

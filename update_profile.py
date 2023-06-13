from datetime import date
from jinja2 import Environment, FileSystemLoader

# Calculate the number of days since a specific start date
start_date = date(2023, 6, 10)  # Replace with your desired start date
current_date = date.today()
num_days = (current_date - start_date).days

# Load the markdown template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('profile_template.md')

# Render the template with the updated value
rendered_content = template.render(days=num_days)

# Write the rendered content to the output file
with open('README.md', 'w') as file:
    file.write(rendered_content)

import os

def create_vue_component(component_name):
    # Make sure the component name is valid for a file
    component_name = component_name.strip().capitalize()

    # Define the content for the Vue component
    vue_component = f"""
<template>
  <div class="{component_name}">
    <h1>{component_name} Component</h1>
    <!-- Your content here -->
  </div>
</template>

<script>
export default {{
  name: '{component_name}'
}}
</script>

<style scoped>
.{component_name} {{
  /* Your styles here */
}}
</style>
    """

    # Define the file path
    file_path = f"./src/components/{component_name}.vue"

    # Create the components folder if it doesn't exist
    if not os.path.exists('./src/components'):
        os.makedirs('./src/components')

    # Write the Vue component to a file
    with open(file_path, 'w') as file:
        file.write(vue_component)

    print(f"Component {component_name}.vue has been created successfully!")

# Ask the user for the component name
if __name__ == "__main__":
    component_name = input("Enter the component name (e.g., MyComponent): ")
    create_vue_component(component_name)

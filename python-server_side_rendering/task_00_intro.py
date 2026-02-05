import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and a list of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): List of dictionaries containing attendee data.

    Returns:
        None
    """
    
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    
    # Check if template is empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    # Check if all items in attendees are dictionaries
    for i, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print(f"Error: Item at index {i} is not a dictionary.")
            return
    
    # Process each attendee
    for i, attendee in enumerate(attendees, start=1):
        # Start with the template
        processed_template = template
        
        # Define all possible placeholders
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        # Replace each placeholder with the value from the attendee dictionary
        for placeholder in placeholders:
            # Get the value, use "N/A" if missing or None
            value = attendee.get(placeholder)
            if value is None or value == "":
                value = "N/A"
            
            # Replace the placeholder in the template
            processed_template = processed_template.replace(f"{{{placeholder}}}", str(value))
        
        # Create output filename
        filename = f"output_{i}.txt"
        
        # Write to file
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(processed_template)
            print(f"Created: {filename}")
        except Exception as e:
            print(f"Error writing file {filename}: {e}")


# Test the function (optional - remove or comment out for submission)
if __name__ == "__main__":
    # Read the template from a file
    try:
        with open('template.txt', 'r', encoding='utf-8') as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: template.txt file not found.")
        # Use a default template for testing
        template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""

    # List of attendees for testing
    attendees = [
        {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
        {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco o"},
        {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"},
        {"name": "David", "event_title": "Tech Meetup", "event_location": "Chicago"},  # Missing event_date
        {"event_title": "No Name Event", "event_date": "2023-09-10", "event_location": "Seattle"}  # Missing name
    ]

    # Call the function with the template and attendees list
    generate_invitations(template_content, attendees)

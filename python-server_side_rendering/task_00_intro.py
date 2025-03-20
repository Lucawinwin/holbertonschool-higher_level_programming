def generate_invitations(template, attendees):
    """
    Generate personalized invitation files based on a template and attendee data.
    
    Args:
        template (str): A string containing placeholders for name, event_title, 
                        event_date, and event_location.
        attendees (list): A list of dictionaries containing attendee information.
    
    Returns:
        None: Function writes output to files named output_X.txt.
    """
    # Check input types
    if not isinstance(template, str):
        print(f"Error: Template must be a string, received {type(template).__name__}")
        return
    
    if not isinstance(attendees, list):
        print(f"Error: Attendees must be a list, received {type(attendees).__name__}")
        return
    
    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, 1):
        # Check if attendee is a dictionary
        if not isinstance(attendee, dict):
            print(f"Error: Attendee at index {index-1} is not a dictionary, skipping")
            continue
        
        # Create a copy of the template
        personalized_invitation = template
        
        # Replace placeholders with attendee data or "N/A" if missing
        placeholders = ["name", "event_title", "event_date", "event_location"]
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            personalized_invitation = personalized_invitation.replace(f"{{{{{placeholder}}}}}", str(value))
        
        # Write the processed template to an output file
        output_filename = f"output_{index}.txt"
        with open(output_filename, "w") as file:
            file.write(personalized_invitation)
        
        print(f"Generated {output_filename}")

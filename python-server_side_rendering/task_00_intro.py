import os

def generate_invitations(template, attendees):
    # Check input types
    if not isinstance(template, str):
        print("Error: The template should be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: The attendees should be a list of dictionaries.")
        return
    
    # Check for empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for idx, attendee in enumerate(attendees):
        # Replace placeholders with actual values or 'N/A' if missing
        invitation = template
        for key in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(key, 'N/A')
            if value is None:
                value = 'N/A'
            placeholder = f"{{{key}}}"
            invitation = invitation.replace(placeholder, value)
        
        # Generate output filename
        output_filename = f"output_{idx + 1}.txt"
        
        # Check if the file already exists
        if os.path.exists(output_filename):
            print(f"Error: File {output_filename} already exists. Skipping this invitation.")
            continue
        
        try:
            # Write the invitation to an output file
            with open(output_filename, 'w') as output_file:
                output_file.write(invitation)
            print(f"Invitation for attendee {idx + 1} written to {output_filename}")
        except Exception as e:
            print(f"Error writing to file {output_filename}: {e}")
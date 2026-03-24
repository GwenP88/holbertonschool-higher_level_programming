def generate_invitations(template, attendees):
    """Generate personalized invitation files
    from a template and a list of attendees."""

    if not isinstance(template, str):
        print("Template must be a string")
        return
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if not isinstance(attendees, list):
        print("Attendees must be a list of dictionaries")
        return
    if attendees == []:
        print("No data provided, no output files generated.")
        return
    for index, data in enumerate(attendees, start=1):
        if not isinstance(data, dict):
            print("Attendees must be a list of dictionaries")
            return
        template_cpy = template
        name = data.get("name")
        if name is None:
            name = "N/A"
        else:
            name = str(name)
        event_title = data.get("event_title")
        if event_title is None:
            event_title = "N/A"
        else:
            event_title = str(event_title)
        event_date = data.get("event_date")
        if event_date is None:
            event_date = "N/A"
        else:
            event_date = str(event_date)
        event_location = data.get("event_location")
        if event_location is None:
            event_location = "N/A"
        else:
            event_location = str(event_location)
        template_cpy = template_cpy.replace("{name}", name)
        template_cpy = template_cpy.replace("{event_title}", event_title)
        template_cpy = template_cpy.replace("{event_date}", event_date)
        template_cpy = template_cpy.replace("{event_location}", event_location)
        with open("output_" + str(index) + ".txt", "w") as f:
            f.write(template_cpy)

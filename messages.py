def ci_failure_message():
    project = 'project'
    build_number = 120
    job_name = 'job'
    
    return {
        "description": f'''Project: `{project}`\nPipeline #{build_number} Has Failed at Job `{job_name}`.''',
        "title": 'Failure',
        "url": "https://github.com/maged1995",
        "color": 0x992d22
    }

def ci_success_message():
    project = 'project'
    build_number = 120

    return {
        "description": f'''Project: `{project}`\nPipeline #{build_number} Has Succeeded''',
        "title": 'Success',
        "url": "https://github.com/maged1995",
        "color": 0x6aa84f
    }
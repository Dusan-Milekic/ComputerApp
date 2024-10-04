import psutil
import webbrowser
import os

# Counter process
counter_p = 0
# To store all process
process_list = []

# Show all processes in PC
def run_cmd_program():
    global counter_p  # Declare global var for process
    global process_list  # Declare global var

    process_list.clear()  # Clear the previous data
    counter_p = 0  # Reset the counter

    print("\nPlease wait to load all processes.....\n")
    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            process_list.append([process.info['pid'], process.info['name'], process.info['username']])
            counter_p += 1  # Increment counter

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Now create the HTML file
    create_html(process_list, counter_p)

    # Open the generated HTML file in the browser
    webbrowser.open("processes.html")

# Function to create the HTML file with process data
def create_html(process_list, counter_p):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="newstyletest.css">
        <title>Process List</title>
        <style>
            table {{
                width: 100%;  
                border-collapse: collapse;
            }}
            table, th, td {{
                border: 1px solid black;
            }}
            th, td {{
                padding: 10px;
                text-align: left;
            }}
        </style>
    </head>
    <body>
        <h1>Running Processes</h1>
        <p>Total Processes: {counter_p}</p>
        <table>
            <thead>
                <tr>
                    <th>PID</th>
                    <th>Process Name</th>
                    <th>User</th>
                </tr>
            </thead>
            <tbody>
    """
    for process in process_list:
        html_content += f"""
            <tr>
                <td>{process[0]}</td>
                <td>{process[1]}</td>
                <td>{process[2]}</td>
            </tr>
        """

    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    # Write the content to an HTML file
    with open("processes.html", "w") as file:
        file.write(html_content)


import html


def export_history_report(
    filename,
    rows
):

    content = """
<!DOCTYPE html>
<html>

<head>

<title>Forensix Report</title>

<style>

body {

    background: #0f172a;
    color: white;
    font-family: Arial;
    padding: 20px;
}

table {

    width: 100%;
    border-collapse: collapse;
}

th, td {

    border: 1px solid #334155;
    padding: 10px;
    text-align: left;
}

th {

    background: #1e293b;
}

tr:nth-child(even) {

    background: #111827;
}

.url {

    color: #38bdf8;
    word-break: break-all;
}

</style>

</head>

<body>

<h1>Chrome History Report</h1>

<table>

<tr>
<th>No</th>
<th>Title</th>
<th>URL</th>
<th>Visit Count</th>
</tr>
"""

    for index, row in enumerate(rows, start=1):

        content += f"""

<tr>

<td>{index}</td>

<td>{html.escape(str(row['title']))}</td>

<td class="url">
{html.escape(str(row['url']))}
</td>

<td>{row['visit_count']}</td>

</tr>
"""

    content += """

</table>

</body>
</html>
"""

    with open(filename, "w") as file:

        file.write(content)


def export_timeline_report(
    filename,
    timeline_data
):

    content = """
<!DOCTYPE html>
<html>

<head>

<title>Forensix Timeline Report</title>

<style>

body {

    background: #020617;
    color: white;
    font-family: Arial;
    padding: 30px;
}

h1 {

    color: #38bdf8;
}

.timeline {

    border-left: 4px solid #38bdf8;
    margin-top: 30px;
    padding-left: 20px;
}

.card {

    background: #111827;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
}

.type {

    font-weight: bold;
    margin-bottom: 10px;
}

.history {

    color: #38bdf8;
}

.download {

    color: #22c55e;
}

.login {

    color: #facc15;
}

.content {

    word-break: break-word;
}

</style>

</head>

<body>

<h1>Browser Activity Timeline</h1>

<div class="timeline">
"""

    for item in timeline_data:

        event_type = item["type"].lower()

        content += f"""

<div class="card">

<div class="type {event_type}">
[{html.escape(item['type'])}]
</div>

<div class="content">
{html.escape(item['content'])}
</div>

</div>
"""

    content += """

</div>

</body>
</html>
"""

    with open(filename, "w") as file:

        file.write(content)
import typer

from typing import Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from forensix.parsers.chrome import (
    parse_chrome_history,
    parse_chrome_downloads,
    parse_chrome_logins
)

from forensix.core.html_report import (
    export_history_report,
    export_timeline_report
)

app = typer.Typer(
    no_args_is_help=True
)

console = Console()


@app.command()
def chrome(
    history: str = typer.Argument(...),
    output: Optional[str] = typer.Option(
        None,
        "--output",
        "-o"
    )
):

    console.print(
        "\n[bold cyan]Chrome History Parser[/bold cyan]\n"
    )

    results = parse_chrome_history(
        history
    )

    table = Table(
        show_header=True,
        header_style="bold cyan",
        expand=True,
        show_lines=True
    )

    table.add_column(
        "No",
        width=5,
        style="yellow"
    )

    table.add_column(
        "Title",
        style="white"
    )

    table.add_column(
        "URL",
        style="cyan",
        overflow="fold"
    )

    table.add_column(
        "Visit Count",
        style="green"
    )

    for index, row in enumerate(results, start=1):

        table.add_row(
            str(index),
            str(row["title"]),
            str(row["url"]),
            str(row["visit_count"])
        )

    console.print(table)

    if output:

        export_history_report(
            output,
            results
        )

        console.print(
            f"\n[bold green][+] Report saved to {output}[/bold green]"
        )


@app.command()
def downloads(
    history: str = typer.Argument(...)
):

    console.print(
        "\n[bold green]Chrome Downloads Parser[/bold green]\n"
    )

    results = parse_chrome_downloads(
        history
    )

    table = Table(
        show_header=True,
        header_style="bold green",
        expand=True,
        show_lines=True
    )

    table.add_column(
        "No",
        width=5,
        style="yellow"
    )

    table.add_column(
        "Source URL",
        overflow="fold",
        style="cyan"
    )

    table.add_column(
        "Downloaded File",
        overflow="fold",
        style="white"
    )

    for index, row in enumerate(results, start=1):

        table.add_row(
            str(index),
            str(row["url"]),
            str(row["path"])
        )

    console.print(table)


@app.command()
def logins(
    database: str = typer.Argument(...)
):

    console.print(
        "\n[bold red]Chrome Login Data Parser[/bold red]\n"
    )

    results = parse_chrome_logins(
        database
    )

    table = Table(
        show_header=True,
        header_style="bold red",
        expand=True,
        show_lines=True
    )

    table.add_column(
        "No",
        width=5,
        style="yellow"
    )

    table.add_column(
        "Origin URL",
        overflow="fold",
        style="cyan"
    )

    table.add_column(
        "Username",
        style="white"
    )

    table.add_column(
        "Password",
        style="green"
    )

    for index, row in enumerate(results, start=1):

        table.add_row(
            str(index),
            str(row["url"]),
            str(row["username"]),
            str(row["password"])
        )

    console.print(table)


@app.command()
def timeline(
    history: str = typer.Argument(...),
    logins: str = typer.Argument(...),
    output: Optional[str] = typer.Option(
        None,
        "--output",
        "-o"
    )
):

    console.print(
        "\n[bold magenta]Browser Activity Timeline[/bold magenta]\n"
    )

    history_results = parse_chrome_history(
        history
    )[:10]

    download_results = parse_chrome_downloads(
        history
    )[:10]

    login_results = parse_chrome_logins(
        logins
    )[:10]

    timeline_data = []

    for item in history_results:

        entry = {

            "type": "HISTORY",
            "content": item["url"]
        }

        timeline_data.append(entry)

    for item in download_results:

        entry = {

            "type": "DOWNLOAD",
            "content": item["path"]
        }

        timeline_data.append(entry)

    for item in login_results:

        entry = {

            "type": "LOGIN",
            "content": f"{item['url']} -> {item['username']}"
        }

        timeline_data.append(entry)

    for entry in timeline_data:

        console.print(

            Panel(
                f"[bold]{entry['type']}[/bold]\n\n{entry['content']}",
                border_style="magenta"
            )
        )

    if output:

        export_timeline_report(
            output,
            timeline_data
        )

        console.print(
            f"\n[bold green][+] Timeline report saved to {output}[/bold green]"
        )


if __name__ == "__main__":
    app()
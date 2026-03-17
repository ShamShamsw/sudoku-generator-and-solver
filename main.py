"""
main.py - Entry point for Project 29: Sudoku Generator And Solver
==================================================================

Thin-controller module that only orchestrates calls to:
    - operations.py for puzzle generation and solving workflow logic
    - display.py for presentation formatting
    - storage.py for persistence setup
    - models.py for configuration records
"""

from display import format_header, format_startup_guide, format_run_report
from models import create_generator_config
from operations import load_generator_profile, run_core_flow
from storage import ensure_data_dirs


def main() -> None:
    """Run one complete Sudoku generation and solving session.

    Workflow:
        1. Ensure data directories exist.
        2. Print header banner.
        3. Build generator config and startup profile.
        4. Print startup guide.
        5. Run puzzle generator and solver pipeline (operations.run_core_flow).
        6. Print final session report.

    Returns:
        None

    TODO: Implement any additional orchestration needs for advanced CLI options.
    """
    # Prepare directories before any file operations.
    ensure_data_dirs()

    # Print session header.
    print(format_header())

    # Build generator configuration.
    config = create_generator_config()

    # Build startup profile for display.
    profile = load_generator_profile()

    # Print startup guide.
    print(format_startup_guide(config, profile))

    # Run puzzle generator and solver workflow.
    summary = run_core_flow()

    # Print final report.
    print(format_run_report(summary))


if __name__ == '__main__':
    main()

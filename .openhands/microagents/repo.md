---
name: gringo
type: repo
version: 1.0.0
agent: CodeActAgent
---

# Gringo Project

A Python-based web scraping and data management system focused on efficient data collection and storage.

## Project Structure

```
gringo/
├── models/      # SQLAlchemy ORM models
├── scrapers/    # Web scraping components
├── migrations/  # Alembic migration scripts
├── tests/       # Test suites and fixtures
└── utils/       # Utility functions and helpers
```

## Development Guidelines

### Database Infrastructure
- Use SQLAlchemy 2.0 style with type annotations
- All models must be defined in `models/` directory
- Create Alembic migrations for all schema changes
- Use meaningful table and column names
- Include proper indexes for frequently queried fields

### Web Scraping
- Implement scrapers using requests and BeautifulSoup4
- Include proper rate limiting and retry logic
- Handle errors gracefully with appropriate logging
- Store raw responses before parsing when appropriate
- Follow robots.txt guidelines

### Testing Requirements
- Write tests before implementing features (TDD)
- All new functionality must have corresponding tests
- Use pytest fixtures for reusable test data
- Mock external services in tests
- Maintain test coverage above 80%

### Code Style
- Use black for code formatting
- Include type hints for all function parameters and return values
- Follow PEP 8 guidelines
- Write clear docstrings for public functions and classes

## Setup Instructions

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Initialize database:
   ```bash
   poetry run alembic upgrade head
   ```

3. Run tests:
   ```bash
   poetry run pytest
   ```

## Dependencies

Core dependencies are managed through Poetry:
- Python 3.12+
- SQLAlchemy 2.0+ for ORM
- Alembic for migrations
- requests for HTTP
- BeautifulSoup4 for HTML parsing
- pytest for testing
- black for formatting
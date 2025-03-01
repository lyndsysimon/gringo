# Gringo

A War Thunder vehicle data assistant that provides quick, accurate information about in-game vehicles through multiple interface options.

## Overview

Gringo is designed to make accessing War Thunder vehicle specifications quick and convenient. It collects and processes vehicle data from the War Thunder wiki into a structured format, then uses a retrieval-augmented generation (RAG) system to provide accurate answers to specific questions about vehicle characteristics.

Example query:
> "What is the combat flap rip speed of the F-14B?"

The system will retrieve and provide the exact specification from its processed dataset.

## Development Environment

All development on this project is done using [OpenHands](https://app.all-hands.dev/), an AI-powered development environment. This ensures consistency in development practices and enables efficient collaboration through a standardized environment.

## Features

- Data collection from War Thunder wiki
- Structured data storage in CSV format
- RAG-based query system for accurate information retrieval
- Multiple interface options:
  - Web-based chat interface
  - Discord bot
  - Twitch chat integration
  - Voice interaction

## Development Roadmap

### Phase 1: Core Infrastructure
- [ ] Set up data collection system
- [ ] Implement data processing pipeline
- [ ] Create structured data storage
- [ ] Develop RAG query system

### Phase 2: Interfaces
- [ ] Web-based chat interface
  - Basic chat UI
  - API endpoints
  - Response formatting
- [ ] Discord bot integration
- [ ] Twitch chat bot
- [ ] Voice interface implementation

### Phase 3: Enhancements
- [ ] Expand vehicle database
- [ ] Improve response accuracy
- [ ] Add support for complex queries
- [ ] Performance optimizations

## Changelog

### [Unreleased]
- Initial project setup

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup

(Development setup instructions will be added as the project infrastructure is established)

### Code Style

- Follow PEP 8 guidelines for Python code
- Write clear commit messages
- Include tests for new features

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
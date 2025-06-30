# Contributing to TechStyle E-Commerce

## Code Quality Standards

### Formatting
- Use `black` for code formatting: `black .`
- Use `isort` for import sorting: `isort .`

### Linting
- Code must pass `flake8` checks
- Maintain pylint score above 8.0

### Testing
- All new features require tests
- Maintain test coverage above 80%

### Pre-commit Setup
```bash
pip install pre-commit
pre-commit install
```

## Development Workflow
1. Create feature branch
2. Make changes
3. Run local tests: `pytest`
4. Run linting: `flake8 .`
5. Format code: `black .`
6. Commit and push
7. Create Pull Request